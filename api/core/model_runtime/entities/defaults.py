from core.model_runtime.entities.model_entities import DefaultParameterName

PARAMETER_RULE_TEMPLATE: dict[DefaultParameterName, dict] = {
    DefaultParameterName.TEMPERATURE: {
        "label": {
            "en_US": "Temperature",
        },
        "type": "float",
        "help": {
            "en_US": "Controls randomness. Lower temperature results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Higher temperature results in more random completions.",
        },
        "required": False,
        "default": 0.0,
        "min": 0.0,
        "max": 1.0,
        "precision": 2,
    },
    DefaultParameterName.TOP_P: {
        "label": {
            "en_US": "Top P",
        },
        "type": "float",
        "help": {
            "en_US": "Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.",
        },
        "required": False,
        "default": 1.0,
        "min": 0.0,
        "max": 1.0,
        "precision": 2,
    },
    DefaultParameterName.TOP_K: {
        "label": {
            "en_US": "Top K",
        },
        "type": "int",
        "help": {
            "en_US": "Limits the number of tokens to consider for each step by keeping only the k most likely tokens.",
        },
        "required": False,
        "default": 50,
        "min": 1,
        "max": 100,
        "precision": 0,
    },
    DefaultParameterName.PRESENCE_PENALTY: {
        "label": {
            "en_US": "Presence Penalty",
        },
        "type": "float",
        "help": {
            "en_US": "Applies a penalty to the log-probability of tokens already in the text.",
        },
        "required": False,
        "default": 0.0,
        "min": 0.0,
        "max": 1.0,
        "precision": 2,
    },
    DefaultParameterName.FREQUENCY_PENALTY: {
        "label": {
            "en_US": "Frequency Penalty",
        },
        "type": "float",
        "help": {
            "en_US": "Applies a penalty to the log-probability of tokens that appear in the text.",
        },
        "required": False,
        "default": 0.0,
        "min": 0.0,
        "max": 1.0,
        "precision": 2,
    },
    DefaultParameterName.MAX_TOKENS: {
        "label": {
            "en_US": "Max Tokens",
        },
        "type": "int",
        "help": {
            "en_US": "Specifies the upper limit on the length of generated results. If the generated results are truncated, you can increase this parameter.",
        },
        "required": False,
        "default": 64,
        "min": 1,
        "max": 2048,
        "precision": 0,
    },
    DefaultParameterName.RESPONSE_FORMAT: {
        "label": {
            "en_US": "Response Format",
        },
        "type": "string",
        "help": {
            "en_US": "Set a response format, ensure the output from llm is a valid code block as possible, such as JSON, XML, etc.",
        },
        "required": False,
        "options": ["JSON", "XML"],
    },
    DefaultParameterName.JSON_SCHEMA: {
        "label": {
            "en_US": "JSON Schema",
        },
        "type": "text",
        "help": {
            "en_US": "Set a response json schema will ensure LLM to adhere it.",
        },
        "required": False,
    },
}
