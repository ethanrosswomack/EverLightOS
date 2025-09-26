#!/usr/bin/env node
/**
 * APM CLI - Playwright automation for checklist operations
 */

import { chromium, Browser, Page } from 'playwright';
import * as fs from 'fs';
import * as path from 'path';
import { findChecklistTable, findEligibleCheckboxes, getWorkOrderNumber } from '../automation/dom_selectors';

interface LogEntry {
  ts: string;
  wo: string;
  action: string;
  eligible: number;
  changed: number;
  url: string;
  actor: string;
  mode: string;
}

class APMCli {
  private browser: Browser | null = null;
  private page: Page | null = null;

  async init(headless: boolean = true): Promise<void> {
    this.browser = await chromium.launch({ headless });
    this.page = await this.browser.newPage();
  }

  async cleanup(): Promise<void> {
    if (this.page) await this.page.close();
    if (this.browser) await this.browser.close();
  }

  private logAction(action: string, wo: string, eligible: number, changed: number, url: string): void {
    const logEntry: LogEntry = {
      ts: new Date().toISOString(),
      wo,
      action,
      eligible,
      changed,
      url,
      actor: process.env.USER || 'cli-user',
      mode: 'playwright'
    };

    const today = new Date().toISOString().split('T')[0];
    const logDir = path.join(process.cwd(), 'runs', 'logs');
    const logFile = path.join(logDir, `${today}.jsonl`);

    if (!fs.existsSync(logDir)) {
      fs.mkdirSync(logDir, { recursive: true });
    }

    fs.appendFileSync(logFile, JSON.stringify(logEntry) + '\n');
  }

  async dryRun(url: string): Promise<void> {
    if (!this.page) throw new Error('CLI not initialized');

    console.log(`🔍 Dry run on: ${url}`);
    await this.page.goto(url);
    await this.page.waitForLoadState('networkidle');

    const result = await this.page.evaluate(() => {
      // Import selector functions into page context
      const findChecklistTable = (doc: Document): HTMLTableElement | null => {
        const tables = Array.from(doc.querySelectorAll('table'));
        const scored = tables.map(t => {
          const head = (t.querySelector('thead')?.innerText || '').toLowerCase();
          const region = (t.closest('[role="region"]')?.textContent || '').toLowerCase();
          const score = 
            +(/checklist/.test(head + region)) + 
            +(/result|follow-?up|notes/.test(head)) + 
            t.querySelectorAll('tbody tr').length / 1000;
          return { t, score };
        });
        return scored.sort((a, b) => b.score - a.score)[0]?.t ?? null;
      };

      const findEligibleCheckboxes = (table: HTMLTableElement): HTMLInputElement[] => {
        const rows = Array.from(table.querySelectorAll('tbody tr'))
          .filter(r => r.offsetParent !== null);
        const out: HTMLInputElement[] = [];
        
        for (const tr of rows) {
          const inputs = Array.from(tr.querySelectorAll('input, textarea, select'));
          const hasText = inputs.some(i => 
            (i.tagName === 'TEXTAREA' || (i as HTMLInputElement).type === 'text') && 
            !i.disabled && 
            i.offsetParent
          );
          
          if (hasText) continue;
          
          const cbs = inputs.filter(i => 
            (i as HTMLInputElement).type === 'checkbox' && 
            !i.disabled && 
            i.offsetParent
          ) as HTMLInputElement[];
          
          if (cbs.length > 0) out.push(cbs[0]);
        }
        
        return out;
      };

      const getWorkOrderNumber = (): string => {
        const urlMatch = window.location.href.match(/wo[_=](\d+)/i);
        if (urlMatch) return urlMatch[1];
        
        const titleMatch = document.title.match(/(\d{10,})/);
        if (titleMatch) return titleMatch[1];
        
        return 'unknown';
      };

      const table = findChecklistTable(document);
      if (!table) return { error: 'No checklist table found' };

      const eligible = findEligibleCheckboxes(table);
      const wo = getWorkOrderNumber();

      return {
        wo,
        eligible: eligible.length,
        tableRows: table.querySelectorAll('tbody tr').length
      };
    });

    if ('error' in result) {
      console.error(`❌ ${result.error}`);
      return;
    }

    console.log(`✅ Found checklist table with ${result.tableRows} total rows`);
    console.log(`📋 ${result.eligible} eligible checkboxes found`);
    console.log(`🔢 Work Order: ${result.wo}`);

    this.logAction('dry-run', result.wo, result.eligible, 0, url);
  }

  async bulkCheck(url: string, confirm: boolean = false): Promise<void> {
    if (!this.page) throw new Error('CLI not initialized');
    if (!confirm) {
      console.log('❌ Use --confirm flag to execute bulk check');
      return;
    }

    console.log(`🚀 Bulk check on: ${url}`);
    await this.page.goto(url);
    await this.page.waitForLoadState('networkidle');

    const result = await this.page.evaluate(async () => {
      // Same selector functions as dry run
      const findChecklistTable = (doc: Document): HTMLTableElement | null => {
        const tables = Array.from(doc.querySelectorAll('table'));
        const scored = tables.map(t => {
          const head = (t.querySelector('thead')?.innerText || '').toLowerCase();
          const region = (t.closest('[role="region"]')?.textContent || '').toLowerCase();
          const score = 
            +(/checklist/.test(head + region)) + 
            +(/result|follow-?up|notes/.test(head)) + 
            t.querySelectorAll('tbody tr').length / 1000;
          return { t, score };
        });
        return scored.sort((a, b) => b.score - a.score)[0]?.t ?? null;
      };

      const findEligibleCheckboxes = (table: HTMLTableElement): HTMLInputElement[] => {
        const rows = Array.from(table.querySelectorAll('tbody tr'))
          .filter(r => r.offsetParent !== null);
        const out: HTMLInputElement[] = [];
        
        for (const tr of rows) {
          const inputs = Array.from(tr.querySelectorAll('input, textarea, select'));
          const hasText = inputs.some(i => 
            (i.tagName === 'TEXTAREA' || (i as HTMLInputElement).type === 'text') && 
            !i.disabled && 
            i.offsetParent
          );
          
          if (hasText) continue;
          
          const cbs = inputs.filter(i => 
            (i as HTMLInputElement).type === 'checkbox' && 
            !i.disabled && 
            i.offsetParent
          ) as HTMLInputElement[];
          
          if (cbs.length > 0) out.push(cbs[0]);
        }
        
        return out;
      };

      const getWorkOrderNumber = (): string => {
        const urlMatch = window.location.href.match(/wo[_=](\d+)/i);
        if (urlMatch) return urlMatch[1];
        
        const titleMatch = document.title.match(/(\d{10,})/);
        if (titleMatch) return titleMatch[1];
        
        return 'unknown';
      };

      const table = findChecklistTable(document);
      if (!table) return { error: 'No checklist table found' };

      const eligible = findEligibleCheckboxes(table);
      const wo = getWorkOrderNumber();
      let changed = 0;

      for (const cb of eligible) {
        if (!cb.checked) {
          cb.click();
          changed++;
          await new Promise(resolve => setTimeout(resolve, 35));
        }
      }

      return { wo, eligible: eligible.length, changed };
    });

    if ('error' in result) {
      console.error(`❌ ${result.error}`);
      return;
    }

    console.log(`✅ Bulk check complete`);
    console.log(`📋 ${result.eligible} eligible checkboxes`);
    console.log(`✓ ${result.changed} items checked`);
    console.log(`🔢 Work Order: ${result.wo}`);

    this.logAction('bulk-check', result.wo, result.eligible, result.changed, url);
  }

  showLogs(): void {
    const logDir = path.join(process.cwd(), 'runs', 'logs');
    if (!fs.existsSync(logDir)) {
      console.log('📝 No logs found');
      return;
    }

    const logFiles = fs.readdirSync(logDir).filter(f => f.endsWith('.jsonl'));
    if (logFiles.length === 0) {
      console.log('📝 No log files found');
      return;
    }

    console.log('📝 Recent logs:');
    logFiles.slice(-3).forEach(file => {
      const filePath = path.join(logDir, file);
      const content = fs.readFileSync(filePath, 'utf8');
      const lines = content.trim().split('\n').filter(Boolean);
      
      console.log(`\n📅 ${file}:`);
      lines.slice(-5).forEach(line => {
        const entry: LogEntry = JSON.parse(line);
        console.log(`  ${entry.ts} | WO:${entry.wo} | ${entry.action} | ${entry.changed}/${entry.eligible}`);
      });
    });
  }
}

// CLI Interface
async function main() {
  const args = process.argv.slice(2);
  const command = args[0];
  
  if (!command) {
    console.log('Usage: apm <command> [options]');
    console.log('Commands:');
    console.log('  checklist:dryrun --url <url>');
    console.log('  checklist:bulk --url <url> --confirm');
    console.log('  log:show');
    return;
  }

  const cli = new APMCli();

  try {
    switch (command) {
      case 'checklist:dryrun': {
        const urlIndex = args.indexOf('--url');
        if (urlIndex === -1 || !args[urlIndex + 1]) {
          console.error('❌ --url required');
          return;
        }
        await cli.init();
        await cli.dryRun(args[urlIndex + 1]);
        break;
      }

      case 'checklist:bulk': {
        const urlIndex = args.indexOf('--url');
        const confirm = args.includes('--confirm');
        if (urlIndex === -1 || !args[urlIndex + 1]) {
          console.error('❌ --url required');
          return;
        }
        await cli.init();
        await cli.bulkCheck(args[urlIndex + 1], confirm);
        break;
      }

      case 'log:show':
        cli.showLogs();
        break;

      default:
        console.error(`❌ Unknown command: ${command}`);
    }
  } finally {
    await cli.cleanup();
  }
}

if (require.main === module) {
  main().catch(console.error);
}