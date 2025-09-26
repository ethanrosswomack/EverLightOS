/**
 * DOM Selector utilities for APM checklist automation
 */

export interface ChecklistTable {
  table: HTMLTableElement;
  score: number;
}

export function findChecklistTable(doc: Document): HTMLTableElement | null {
  const tables = Array.from(doc.querySelectorAll('table'));
  const scored: ChecklistTable[] = tables.map(t => {
    const head = (t.querySelector('thead')?.innerText || '').toLowerCase();
    const region = (t.closest('[role="region"]')?.textContent || '').toLowerCase();
    const score = 
      +(/checklist/.test(head + region)) + 
      +(/result|follow-?up|notes/.test(head)) + 
      t.querySelectorAll('tbody tr').length / 1000;
    return { table: t, score };
  });
  
  return scored.sort((a, b) => b.score - a.score)[0]?.table ?? null;
}

export function findEligibleCheckboxes(table: HTMLTableElement): HTMLInputElement[] {
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
    
    if (!cbs.length) continue;
    
    // Prefer first enabled checkbox in the row
    out.push(cbs[0]);
  }
  
  return out;
}

export function getWorkOrderNumber(doc: Document): string {
  // Try URL first
  const urlMatch = doc.location.href.match(/wo[_=](\d+)/i);
  if (urlMatch) return urlMatch[1];
  
  // Try page title
  const titleMatch = doc.title.match(/(\d{10,})/);
  if (titleMatch) return titleMatch[1];
  
  // Try page content
  const contentMatch = doc.body.innerText.match(/work\s*order[:\s#]*(\d{10,})/i);
  if (contentMatch) return contentMatch[1];
  
  return 'unknown';
}

export function isChecklistPage(doc: Document): boolean {
  const url = doc.location.href.toLowerCase();
  const title = doc.title.toLowerCase();
  const content = doc.body.innerText.toLowerCase();
  
  return (
    url.includes('checklist') ||
    title.includes('checklist') ||
    content.includes('checklist') ||
    !!findChecklistTable(doc)
  );
}