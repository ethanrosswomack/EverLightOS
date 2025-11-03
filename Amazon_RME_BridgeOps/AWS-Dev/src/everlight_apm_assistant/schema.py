SESSION_SCHEMA = {
    "type": "object",
    "properties": {
        "header": {"type": "object"},
        "items": {"type": "array"}
    },
    "required": ["header", "items"]
}
"""Data schema for EverLight APM assistant - placeholder."""

SAMPLE_SCHEMA = {
    'id': 'string',
    'timestamp': 'string',
    'metrics': 'object'
}
