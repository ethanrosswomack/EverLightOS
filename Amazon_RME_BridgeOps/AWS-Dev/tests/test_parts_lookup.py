from src.parts_lookup import get_adapter

def test_stub_lookup():
    adapter = get_adapter("stub")
    result = adapter.lookup("123")
    assert result["part_number"] == "123"
    assert "Stub" in result["name"]