def get_schema():
    key = "logger"
    schema = {
        "description": "Logger configuration",
        "type": "object",
        "properties": {
            "log-level": {
                "description": "Log level to be used.",
                "type": "string",
                "enum": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
            },
            "log-file": {
                "description": "File name for the logger.",
                "type": "string"
            }
        },
        "required": ["log-level", "log-file"]
    }

    return key, schema
