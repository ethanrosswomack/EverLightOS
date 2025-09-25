# JSON Schema for validating session payloads
SESSION_SCHEMA = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "header": {
      "type": "object",
      "properties": {
        "date": {"type": "string"},
        "site": {"type": "string"},
        "area": {"type": "string"},
        "shift": {"type": "string"},
        "tech_name": {"type": "string"},
        "manager_on_duty": {"type": "string"},
        "notes": {"type": "string"}
      },
      "required": ["date"]
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "equipment_id": {"type": "string"},
          "component": {"type": "string"},
          "action": {"type": "string"},
          "result": {"type": "string"},
          "time_spent_min": {"type": "integer"},
          "work_order": {"type": "string"},
          "notes": {"type": "string"}
        },
        "required": ["equipment_id","component","action","result"]
      }
    }
  },
  "required": ["header","items"]
}
