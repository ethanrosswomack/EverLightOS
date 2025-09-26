// ==UserScript==
// @name         APM Checklist Helper
// @namespace    http://tampermonkey.net/
// @version      1.0.0
// @description  Bulk checklist automation for APM with dry-run, undo, and audit logging
// @author       RME BridgeOps
// @match        *://*/COMMON*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Configuration
    const CONFIG = {
        SKIP_ROWS_WITH_TEXT_INPUTS: true,
        RATE_LIMIT_MS: 35,
        HIGHLIGHT_CLASS: 'apm-highlight',
        STORAGE_KEY: 'apm_checklist_logs'
    };

    let checkboxSnapshot = new Map();
    let isProcessing = false;

    // DOM Selector Functions
    function findChecklistTable() {
        const tables = Array.from(document.querySelectorAll('table'));
        const scored = tables.map(t => {
            const head = (t.querySelector('thead')?.innerText || '').toLowerCase();
            const region = (t.closest('[role="region"]')?.textContent || '').toLowerCase();
            const score = +(/checklist/.test(head + region)) + +(/result|follow-?up|notes/.test(head)) + t.querySelectorAll('tbody tr').length / 1000;
            return { t, score };
        });
        return scored.sort((a, b) => b.score - a.score)[0]?.t ?? null;
    }

    function findEligibleCheckboxes(table) {
        const rows = Array.from(table.querySelectorAll('tbody tr')).filter(r => r.offsetParent !== null);
        const eligible = [];
        
        for (const tr of rows) {
            const inputs = Array.from(tr.querySelectorAll('input, textarea, select'));
            const hasText = inputs.some(i => 
                (i.tagName === 'TEXTAREA' || i.type === 'text') && 
                !i.disabled && 
                i.offsetParent
            );
            
            if (CONFIG.SKIP_ROWS_WITH_TEXT_INPUTS && hasText) continue;
            
            const checkboxes = inputs.filter(i => 
                i.type === 'checkbox' && 
                !i.disabled && 
                i.offsetParent
            );
            
            if (checkboxes.length > 0) {
                eligible.push(checkboxes[0]);
            }
        }
        return eligible;
    }

    // Logging Functions
    function getWorkOrderNumber() {
        const urlMatch = window.location.href.match(/wo[_=](\d+)/i);
        if (urlMatch) return urlMatch[1];
        
        const titleMatch = document.title.match(/(\d{10,})/);
        if (titleMatch) return titleMatch[1];
        
        return 'unknown';
    }

    function logAction(action, eligible, changed) {
        const logEntry = {
            ts: new Date().toISOString(),
            wo: getWorkOrderNumber(),
            action: action,
            eligible: eligible,
            changed: changed,
            url: window.location.href,
            actor: 'userscript',
            mode: 'tampermonkey'
        };

        const logs = JSON.parse(localStorage.getItem(CONFIG.STORAGE_KEY) || '[]');
        logs.push(logEntry);
        localStorage.setItem(CONFIG.STORAGE_KEY, JSON.stringify(logs));
    }

    // Main Functions
    function highlightEligible() {
        const table = findChecklistTable();
        if (!table) {
            alert('No checklist table found');
            return;
        }

        const eligible = findEligibleCheckboxes(table);
        
        // Clear previous highlights
        document.querySelectorAll(`.${CONFIG.HIGHLIGHT_CLASS}`).forEach(el => {
            el.classList.remove(CONFIG.HIGHLIGHT_CLASS);
        });

        // Add CSS if not exists
        if (!document.getElementById('apm-helper-styles')) {
            const style = document.createElement('style');
            style.id = 'apm-helper-styles';
            style.textContent = `.${CONFIG.HIGHLIGHT_CLASS} { background-color: #ffeb3b !important; }`;
            document.head.appendChild(style);
        }

        // Highlight eligible rows
        eligible.forEach(cb => {
            cb.closest('tr')?.classList.add(CONFIG.HIGHLIGHT_CLASS);
        });

        alert(`Dry Run: Found ${eligible.length} eligible checkboxes`);
        logAction('dry-run', eligible.length, 0);
    }

    async function bulkCheck() {
        if (isProcessing) return;
        isProcessing = true;

        const table = findChecklistTable();
        if (!table) {
            alert('No checklist table found');
            isProcessing = false;
            return;
        }

        const eligible = findEligibleCheckboxes(table);
        
        // Take snapshot for undo
        checkboxSnapshot.clear();
        eligible.forEach((cb, index) => {
            checkboxSnapshot.set(index, cb.checked);
        });

        let changed = 0;
        for (let i = 0; i < eligible.length; i++) {
            const cb = eligible[i];
            if (!cb.checked) {
                cb.click();
                changed++;
                await new Promise(resolve => setTimeout(resolve, CONFIG.RATE_LIMIT_MS));
            }
        }

        alert(`Bulk Check Complete: ${changed} items checked`);
        logAction('bulk-check', eligible.length, changed);
        isProcessing = false;
    }

    function undoChanges() {
        const table = findChecklistTable();
        if (!table) {
            alert('No checklist table found');
            return;
        }

        const eligible = findEligibleCheckboxes(table);
        let restored = 0;

        eligible.forEach((cb, index) => {
            if (checkboxSnapshot.has(index)) {
                const originalState = checkboxSnapshot.get(index);
                if (cb.checked !== originalState) {
                    cb.click();
                    restored++;
                }
            }
        });

        alert(`Undo Complete: ${restored} items restored`);
        logAction('undo', eligible.length, restored);
        checkboxSnapshot.clear();
    }

    function showLogs() {
        const logs = JSON.parse(localStorage.getItem(CONFIG.STORAGE_KEY) || '[]');
        const logText = logs.map(log => JSON.stringify(log)).join('\n');
        
        const textarea = document.createElement('textarea');
        textarea.value = logText;
        textarea.style.cssText = 'position:fixed;top:10px;right:10px;width:400px;height:300px;z-index:10000;';
        document.body.appendChild(textarea);
        textarea.select();
        
        setTimeout(() => document.body.removeChild(textarea), 10000);
    }

    // UI Panel
    function createPanel() {
        const panel = document.createElement('div');
        panel.id = 'apm-helper-panel';
        panel.style.cssText = `
            position: fixed;
            top: 10px;
            right: 10px;
            background: white;
            border: 2px solid #333;
            padding: 10px;
            z-index: 10000;
            font-family: Arial, sans-serif;
            font-size: 12px;
        `;

        panel.innerHTML = `
            <div><strong>APM Checklist Helper</strong></div>
            <button id="apm-dry-run">Dry Run</button>
            <button id="apm-bulk-check">Check All</button>
            <button id="apm-undo">Undo</button>
            <button id="apm-logs">Show Logs</button>
            <button id="apm-close">×</button>
        `;

        document.body.appendChild(panel);

        // Event listeners
        document.getElementById('apm-dry-run').onclick = highlightEligible;
        document.getElementById('apm-bulk-check').onclick = bulkCheck;
        document.getElementById('apm-undo').onclick = undoChanges;
        document.getElementById('apm-logs').onclick = showLogs;
        document.getElementById('apm-close').onclick = () => panel.remove();
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.shiftKey && e.key === 'A') {
            e.preventDefault();
            bulkCheck();
        }
        if (e.ctrlKey && e.shiftKey && e.key === 'Z') {
            e.preventDefault();
            undoChanges();
        }
    });

    // Initialize
    if (window.location.href.includes('COMMON')) {
        setTimeout(createPanel, 2000);
    }
})();