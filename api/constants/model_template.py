import json

from models.model import AppMode

# TESTED ON 2024-10-19 21:26 GMT
default_app_templates = {
    # workflow default mode
    # TESTED ON 2024-10-19 21:33 GMT
    AppMode.WORKFLOW: {
        "app": {
            "mode": AppMode.WORKFLOW.value,
            "enable_site": True,
            "enable_api": True,
        }
    },
    # completion default mode
    # TESTED ON 2024-10-19 21:34 GMT
    AppMode.COMPLETION: {
        "app": {
            "mode": AppMode.COMPLETION.value,
            "enable_site": True,
            "enable_api": True,
        },
        "model_config": {
            "model": {
                "provider": "openai",
                "name": "gpt-4o",
                "mode": "chat",
                "completion_params": {},
            },
            "user_input_form": json.dumps(
                [
                    {
                        "paragraph": {
                            "label": "Query",
                            "variable": "query",
                            "required": True,
                            "default": "",
                        },
                    },
                ]
            ),
            "pre_prompt": "{{query}}",
        },
    },
    # chat default mode
    # TESTED ON 2024-10-19 21:35 GMT
    AppMode.CHAT: {
        "app": {
            "mode": AppMode.CHAT.value,
            "enable_site": True,
            "enable_api": True,
        },
        "model_config": {
            "model": {
                "provider": "openai",
                "name": "gpt-4o",
                "mode": "chat",
                "completion_params": {},
            },
        },
    },
    # advanced-chat default mode
    # TESTED ON 2024-10-19 21:36 GMT
    AppMode.ADVANCED_CHAT: {
        "app": {
            "mode": AppMode.ADVANCED_CHAT.value,
            "enable_site": True,
            "enable_api": True,
        },
    },
    # agent-chat default mode
    AppMode.AGENT_CHAT: {
        "app": {
            "mode": AppMode.AGENT_CHAT.value,
            "enable_site": True,
            "enable_api": True,
        },
        "model_config": {
            "model": {
                "provider": "openai",
                "name": "gpt-4o",
                "mode": "chat",
                "completion_params": {},
            },
        },
    },
}
