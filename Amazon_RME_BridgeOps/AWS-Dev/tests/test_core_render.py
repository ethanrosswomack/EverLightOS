from everlight_apm_assistant.core import Session, Header


def test_render_empty_items():
    s = Session(Header(date="2025-09-23"))
    out = s.render_text()
    assert "(No PM items recorded)" in out


def test_add_and_render():
    s = Session(Header(date="2025-09-23", site="TPA4"))
    s.add_item(equipment_id="Charger-36", component="filter", action="cleaned", result="pass")
    out = s.render_text()
    assert "Charger-36" in out
