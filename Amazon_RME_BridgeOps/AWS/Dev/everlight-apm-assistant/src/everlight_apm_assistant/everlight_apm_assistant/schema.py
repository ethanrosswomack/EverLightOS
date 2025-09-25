# Stricter JSON Schema for validating session payloads

SESSION_SCHEMA = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "header": {
      "type": "object",
      "properties": {
        "date": {
          "type": "string",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
          "minLength": 10,
          "errorMessage": {
            "type": "Date must be a string in YYYY-MM-DD format.",
            "pattern": "Date must match YYYY-MM-DD."
          }
        },
        "site": {
          "type": "string",
          "minLength": 1,
          "errorMessage": {
            "minLength": "Site is required and must not be empty."
          }
        },
        "area": {
          "type": "string",
          "minLength": 1,
          "errorMessage": {
            "minLength": "Area is required and must not be empty."
          }
        },
        "shift": {
          "type": "string",
          "minLength": 1,
          "errorMessage": {
            "minLength": "Shift is required and must not be empty."
          }
        },
        "tech_name": {
          "type": "string",
          "minLength": 1,
          "errorMessage": {
            "minLength": "Tech name is required and must not be empty."
          }
        },
        "manager_on_duty": {
          "type": "string",
          "minLength": 1,
          "errorMessage": {
            "minLength": "Manager on duty is required and must not be empty."
          }
        },
        "notes": {
          "type": "string"
        }
      },
      "required": ["date", "site", "area", "shift", "tech_name", "manager_on_duty"],
      "additionalProperties": False
    },
    "items": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "properties": {
          "equipment_id": {
            "type": "string",
            "minLength": 1,
            "errorMessage": {
              "minLength": "Equipment ID is required and must not be empty."
            }
          },
          "component": {
            "type": "string",
            "minLength": 1,
            "errorMessage": {
              "minLength": "Component is required and must not be empty."
            }
          },
          "action": {
            "type": "string",
            "minLength": 1,
            "errorMessage": {
              "minLength": "Action is required and must not be empty."
            }
          },
          "result": {
            "type": "string",
            "minLength": 1,
            "errorMessage": {
              "minLength": "Result is required and must not be empty."
            }
          },
          "time_spent_min": {
            "type": "integer",
            "minimum": 1,
            "maximum": 600,
            "errorMessage": {
              "type": "Time spent must be an integer.",
              "minimum": "Time spent must be at least 1 minute.",
              "maximum": "Time spent must be less than 600 minutes."
            }
            # Type coercion: If your validator supports, allow string->int
          },
          "work_order": {
            "type": "string"
          },
          "notes": {
            "type": "string"
          }
        },
        "required": [
          "equipment_id", "component", "action", "result", "time_spent_min"
        ],
        "additionalProperties": False
      },
      "errorMessage": {
        "minItems": "At least one item must be present."
      }
    }
  },
  "required": ["header", "items"],
  "additionalProperties": False,
  "errorMessage": {
    "required": {
      "header": "Header section is required.",
      "items": "Items list is required."
    }
  }
}