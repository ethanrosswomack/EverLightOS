/**
 * Unit tests for DOM selector utilities
 */

import { JSDOM } from 'jsdom';
import { findChecklistTable, findEligibleCheckboxes, getWorkOrderNumber, isChecklistPage } from '../../src/automation/dom_selectors';

describe('DOM Selectors', () => {
  let dom: JSDOM;
  let document: Document;

  beforeEach(() => {
    dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');
    document = dom.window.document;
    global.document = document;
  });

  describe('findChecklistTable', () => {
    test('finds table with checklist headers', () => {
      document.body.innerHTML = `
        <table>
          <thead>
            <tr><th>Item</th><th>Checklist</th><th>Result</th></tr>
          </thead>
          <tbody>
            <tr><td>Item 1</td><td>Check motor</td><td><input type="checkbox"></td></tr>
          </tbody>
        </table>
      `;

      const table = findChecklistTable(document);
      expect(table).toBeTruthy();
      expect(table?.tagName).toBe('TABLE');
    });

    test('returns null when no checklist table found', () => {
      document.body.innerHTML = `
        <table>
          <thead>
            <tr><th>Name</th><th>Value</th></tr>
          </thead>
        </table>
      `;

      const table = findChecklistTable(document);
      expect(table).toBeNull();
    });

    test('selects table with highest score', () => {
      document.body.innerHTML = `
        <table id="small">
          <thead><tr><th>Checklist</th></tr></thead>
          <tbody><tr><td>Item</td></tr></tbody>
        </table>
        <table id="large">
          <thead><tr><th>Checklist</th><th>Result</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Item 1</td><td><input type="checkbox"></td><td></td></tr>
            <tr><td>Item 2</td><td><input type="checkbox"></td><td></td></tr>
            <tr><td>Item 3</td><td><input type="checkbox"></td><td></td></tr>
          </tbody>
        </table>
      `;

      const table = findChecklistTable(document);
      expect(table?.id).toBe('large');
    });
  });

  describe('findEligibleCheckboxes', () => {
    let table: HTMLTableElement;

    beforeEach(() => {
      document.body.innerHTML = `
        <table>
          <tbody id="test-tbody"></tbody>
        </table>
      `;
      table = document.querySelector('table')!;
    });

    test('finds visible enabled checkboxes', () => {
      document.getElementById('test-tbody')!.innerHTML = `
        <tr style="display: block;">
          <td>Item 1</td>
          <td><input type="checkbox" /></td>
        </tr>
        <tr style="display: block;">
          <td>Item 2</td>
          <td><input type="checkbox" /></td>
        </tr>
      `;

      // Mock offsetParent for visibility check
      const checkboxes = table.querySelectorAll('input[type="checkbox"]');
      checkboxes.forEach(cb => {
        Object.defineProperty(cb, 'offsetParent', { value: document.body });
      });

      const eligible = findEligibleCheckboxes(table);
      expect(eligible).toHaveLength(2);
    });

    test('skips rows with text inputs', () => {
      document.getElementById('test-tbody')!.innerHTML = `
        <tr style="display: block;">
          <td>Item 1</td>
          <td><input type="checkbox" /></td>
        </tr>
        <tr style="display: block;">
          <td>Item 2</td>
          <td><input type="text" /></td>
          <td><input type="checkbox" /></td>
        </tr>
      `;

      // Mock offsetParent for visibility
      const inputs = table.querySelectorAll('input');
      inputs.forEach(input => {
        Object.defineProperty(input, 'offsetParent', { value: document.body });
      });

      const eligible = findEligibleCheckboxes(table);
      expect(eligible).toHaveLength(1);
    });

    test('skips disabled checkboxes', () => {
      document.getElementById('test-tbody')!.innerHTML = `
        <tr style="display: block;">
          <td>Item 1</td>
          <td><input type="checkbox" /></td>
        </tr>
        <tr style="display: block;">
          <td>Item 2</td>
          <td><input type="checkbox" disabled /></td>
        </tr>
      `;

      // Mock offsetParent for visibility
      const checkboxes = table.querySelectorAll('input[type="checkbox"]:not([disabled])');
      checkboxes.forEach(cb => {
        Object.defineProperty(cb, 'offsetParent', { value: document.body });
      });

      const eligible = findEligibleCheckboxes(table);
      expect(eligible).toHaveLength(1);
    });

    test('skips hidden rows', () => {
      document.getElementById('test-tbody')!.innerHTML = `
        <tr style="display: block;">
          <td>Item 1</td>
          <td><input type="checkbox" /></td>
        </tr>
        <tr style="display: none;">
          <td>Item 2</td>
          <td><input type="checkbox" /></td>
        </tr>
      `;

      // Mock offsetParent - null for hidden elements
      const visibleCheckbox = table.querySelector('tr[style="display: block;"] input');
      const hiddenCheckbox = table.querySelector('tr[style="display: none;"] input');
      
      Object.defineProperty(visibleCheckbox, 'offsetParent', { value: document.body });
      Object.defineProperty(hiddenCheckbox, 'offsetParent', { value: null });

      const eligible = findEligibleCheckboxes(table);
      expect(eligible).toHaveLength(1);
    });

    test('handles rows with no checkboxes', () => {
      document.getElementById('test-tbody')!.innerHTML = `
        <tr style="display: block;">
          <td>Item 1</td>
          <td>No checkbox here</td>
        </tr>
        <tr style="display: block;">
          <td>Item 2</td>
          <td><input type="checkbox" /></td>
        </tr>
      `;

      const checkbox = table.querySelector('input[type="checkbox"]');
      Object.defineProperty(checkbox, 'offsetParent', { value: document.body });

      const eligible = findEligibleCheckboxes(table);
      expect(eligible).toHaveLength(1);
    });
  });

  describe('getWorkOrderNumber', () => {
    test('extracts work order from URL', () => {
      Object.defineProperty(document, 'location', {
        value: { href: 'https://example.com/apm?wo=10038554138' },
        writable: true
      });

      const wo = getWorkOrderNumber(document);
      expect(wo).toBe('10038554138');
    });

    test('extracts work order from title', () => {
      Object.defineProperty(document, 'location', {
        value: { href: 'https://example.com/apm' },
        writable: true
      });
      Object.defineProperty(document, 'title', {
        value: 'Work Order 10038554139 - Maintenance',
        writable: true
      });

      const wo = getWorkOrderNumber(document);
      expect(wo).toBe('10038554139');
    });

    test('returns unknown when no work order found', () => {
      Object.defineProperty(document, 'location', {
        value: { href: 'https://example.com/apm' },
        writable: true
      });
      Object.defineProperty(document, 'title', {
        value: 'APM Dashboard',
        writable: true
      });

      const wo = getWorkOrderNumber(document);
      expect(wo).toBe('unknown');
    });
  });

  describe('isChecklistPage', () => {
    test('identifies checklist page by URL', () => {
      Object.defineProperty(document, 'location', {
        value: { href: 'https://example.com/apm/checklist' },
        writable: true
      });

      const isChecklist = isChecklistPage(document);
      expect(isChecklist).toBe(true);
    });

    test('identifies checklist page by title', () => {
      Object.defineProperty(document, 'location', {
        value: { href: 'https://example.com/apm' },
        writable: true
      });
      Object.defineProperty(document, 'title', {
        value: 'APM Checklist - Work Order',
        writable: true
      });

      const isChecklist = isChecklistPage(document);
      expect(isChecklist).toBe(true);
    });

    test('identifies checklist page by table presence', () => {
      Object.defineProperty(document, 'location', {
        value: { href: 'https://example.com/apm' },
        writable: true
      });
      Object.defineProperty(document, 'title', {
        value: 'APM Dashboard',
        writable: true
      });

      document.body.innerHTML = `
        <table>
          <thead><tr><th>Checklist Item</th><th>Result</th></tr></thead>
          <tbody><tr><td>Check motor</td><td><input type="checkbox"></td></tr></tbody>
        </table>
      `;

      const isChecklist = isChecklistPage(document);
      expect(isChecklist).toBe(true);
    });

    test('returns false for non-checklist pages', () => {
      Object.defineProperty(document, 'location', {
        value: { href: 'https://example.com/dashboard' },
        writable: true
      });
      Object.defineProperty(document, 'title', {
        value: 'Dashboard',
        writable: true
      });

      document.body.innerHTML = '<div>Regular content</div>';

      const isChecklist = isChecklistPage(document);
      expect(isChecklist).toBe(false);
    });
  });
});