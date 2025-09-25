import json
import pytest
from pathlib import Path

from everlight_apm_assistant.schema import SESSION_SCHEMA

def get_validator():
    try:
        import jsonschema
        from jsonschema import Draft202012Validator
        return Draft202012Validator(SESSION_SCHEMA, format_checker=jsonschema.FormatChecker())
    except ImportError:
        raise RuntimeError("jsonschema package required for tests")

def load_sample():
    p = Path(__file__).parent.parent / "examples" / "sample_session.json"
    return json.loads(p.read_text(encoding="utf-8"))

def test_valid_sample_session():
    validator = get_validator()
    data = load_sample()
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    assert not errors, f"Unexpected errors: {[e.message for e in errors]}"

def test_missing_required_header_fields():
    validator = get_validator()
    data = load_sample()
    for field in ["site", "area", "shift", "tech_name", "manager_on_duty"]:
        bad = json.loads(json.dumps(data))
        del bad["header"][field]
        errors = list(validator.iter_errors(bad))
        assert errors, f"Missing required field '{field}' should fail."
        assert any(field in str(e.message) for e in errors)

def test_empty_required_item_fields():
    validator = get_validator()
    data = load_sample()
    for field in ["equipment_id", "component", "action", "result"]:
        bad = json.loads(json.dumps(data))
        bad["items"][0][field] = ""
        errors = list(validator.iter_errors(bad))
        assert errors, f"Empty {field} should fail."
        assert any("must not be empty" in str(e.message) for e in errors)

def test_time_spent_min_wrong_type():
    validator = get_validator()
    data = load_sample()
    bad = json.loads(json.dumps(data))
    bad["items"][0]["time_spent_min"] = "five"
    errors = list(validator.iter_errors(bad))
    assert errors
    assert any("Time spent must be an integer" in str(e.message) for e in errors)

def test_time_spent_min_out_of_range():
    validator = get_validator()
    data = load_sample()
    bad = json.loads(json.dumps(data))
    bad["items"][0]["time_spent_min"] = 0
    errors = list(validator.iter_errors(bad))
    assert errors
    assert any("at least 1 minute" in str(e.message) for e in errors)
    bad["items"][0]["time_spent_min"] = 1000
    errors = list(validator.iter_errors(bad))
    assert errors
    assert any("less than 600 minutes" in str(e.message) for e in errors)

def test_missing_items_array():
    validator = get_validator()
    data = load_sample()
    bad = json.loads(json.dumps(data))
    del bad["items"]
    errors = list(validator.iter_errors(bad))
    assert errors
    assert any("Items list is required" in str(e.message) for e in errors)