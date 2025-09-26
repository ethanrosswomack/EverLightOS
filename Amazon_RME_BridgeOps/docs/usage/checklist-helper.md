# APM Checklist Helper - Usage Guide

## Overview

The APM Checklist Helper automates the tedious process of clicking through 200+ checklist items in the APM web application. It provides safe, auditable automation for **post-work attestation** only.

## Installation

### Tampermonkey Userscript (Primary Method)

1. Install [Tampermonkey](https://www.tampermonkey.net/) browser extension
2. Copy the contents of `userscripts/apm-checklist-helper.user.js`
3. Create new userscript in Tampermonkey and paste the code
4. Save and enable the script

### CLI Tool (Development/Testing)

```bash
npm install playwright
npx playwright install chromium
node src/cli/apm.ts checklist:dryrun --url <apm-url>
```

## Usage

### Userscript Interface

When on an APM checklist page, the helper panel appears in the top-right corner:

- **Dry Run** - Highlights eligible checkboxes (no changes made)
- **Check All** - Bulk checks eligible items with rate limiting
- **Undo** - Restores previous checkbox states
- **Show Logs** - Displays audit log for copying
- **×** - Close panel

### Keyboard Shortcuts

- `Ctrl+Shift+A` - Execute bulk check
- `Ctrl+Shift+Z` - Undo last operation

### CLI Commands

```bash
# Dry run analysis
node src/cli/apm.ts checklist:dryrun --url "https://your-apm-url"

# Bulk check (requires --confirm)
node src/cli/apm.ts checklist:bulk --url "https://your-apm-url" --confirm

# Show recent logs
node src/cli/apm.ts log:show
```

## Safety Features

### Automatic Skipping

The tool automatically skips rows that contain:
- Required text inputs or textareas
- Disabled checkboxes
- Hidden elements
- Follow-up action flags

### Rate Limiting

- 35ms delay between checkbox clicks
- Prevents UI freezing and event flooding
- Configurable via `RATE_LIMIT_MS` setting

### Audit Logging

Every action is logged with:
- Timestamp
- Work Order number (if detectable)
- Action type (dry-run, bulk-check, undo)
- Count of eligible vs changed items
- Page URL
- User identifier

### Undo Capability

- Snapshots checkbox states before bulk operations
- One-click restoration of previous states
- Logged undo actions for audit trail

## Configuration

Edit these constants in the userscript:

```javascript
const CONFIG = {
    SKIP_ROWS_WITH_TEXT_INPUTS: true,  // Skip rows requiring manual input
    RATE_LIMIT_MS: 35,                 // Delay between clicks
    HIGHLIGHT_CLASS: 'apm-highlight',  // CSS class for dry-run highlighting
    STORAGE_KEY: 'apm_checklist_logs'  // LocalStorage key for logs
};
```

## Troubleshooting

### "No checklist table found"
- Ensure you're on the correct APM checklist page
- Page may still be loading - wait and try again
- Table structure may have changed - contact support

### Checkboxes not clicking
- Some checkboxes may be disabled by business rules
- Required text fields in the same row prevent auto-checking
- Rate limiting may make the process appear slow

### Logs not saving
- Check browser's localStorage permissions
- Clear old logs if storage is full
- Ensure script has proper permissions

## Best Practices

1. **Always run Dry Run first** to verify eligible items
2. **Complete actual work before using the tool** - this is attestation only
3. **Review highlighted items** during dry run for accuracy
4. **Keep audit logs** for compliance and troubleshooting
5. **Test undo functionality** before bulk operations
6. **Get manager approval** before first use on production systems

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review audit logs for error patterns
3. Contact RME BridgeOps team
4. Submit issue with log entries and page URL