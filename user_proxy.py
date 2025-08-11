from autogen.agentchat import UserProxyAgent

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config=False,
    llm_config=False,
)

from autogen.agentchat import AssistantAgent
 
llm_config = {

    "config_list": [{"model": "gpt-4o", "api_key": "sk-xxx"}],

    "seed": 42,

    "temperature": 0,

}
 
assistant = AssistantAgent(

    name="assistant",

    system_message="You are a helpful assistant.",

    llm_config=llm_config,

)

 