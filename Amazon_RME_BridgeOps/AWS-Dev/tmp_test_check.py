import sys, pathlib
sys.path.insert(0, r"C:\Users\erwomack\Documents\Dev\EverLightOS\Amazon_RME_BridgeOps\AWS-Dev\src")
from everlight_apm_assistant.core import Session, Header

s = Session(Header(date="2025-09-23"))
out = s.render_text()
print('test_render_empty_items ->', "(No PM items recorded)" in out)

s2 = Session(Header(date="2025-09-23", site="TPA4"))
s2.add_item(equipment_id="Charger-36", component="filter", action="cleaned", result="pass")
out2 = s2.render_text()
print('test_add_and_render ->', "Charger-36" in out2)

if ("(No PM items recorded)" in out) and ("Charger-36" in out2):
    print('ALL_PASS')
    sys.exit(0)
else:
    print('FAIL')
    sys.exit(2)
