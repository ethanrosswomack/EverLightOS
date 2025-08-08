import os
from datetime import date

def init_daily_notebook():
    today = date.today().isoformat()
    path = f"notebooks/{today}_field_log.ipynb"
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(f"# Field Log — {today}\n\n## Observations\n\n## Actions Taken\n\n## Follow-ups\n")
    print(f"Notebook created: {path}")

init_daily_notebook()
