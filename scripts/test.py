import os
import autogen  # noqa: E402

llm_config = {
    "config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}],
}

assistant = autogen.AssistantAgent(name="assistant", llm_config=llm_config)