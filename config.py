import os
#OPENAI_API_KEY = "sk-proj-zJ5BH1s5cz7b92Su4SHdT3BlbkFJNMpNA1yb9Jx35a1rjClv"
OPENAI_API_KEY = "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"     #Directly through OpenAI
HUGGINGFACEHUB_API_TOKEN="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"
WOLFRAM_ALPHA_APPID = "5VQ5RQ-GG2PK3XYTA"
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_API_KEY = "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"
AIMLAPI_KEY = "4c217676012e44e8958e8984aa839903"        #Through https://aimlapi.com/.  Access to various other llm providers 
VENDOR_URL = "https://api.aimlapi.com/v1/"


# I'm omitting all other keys
def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "OPENAI_API_KEY" in key or "ID" in key:
            os.environ[key] = value
        if "HUGGINGFACEHUB_API_TOKEN" in key or "ID" in key:
            os.environ[key] = value
        if "WOLFRAM_ALPHA_APPID" in key or "ID" in key:
            os.environ[key] = value
        if "LANGCHAIN_TRACING_V2" in key or "ID" in key:
            os.environ[key] = value
        if "LANGCHAIN_API_KEY" in key or "ID" in key:
            os.environ[key] = value
        if "AIMLAPI_KEY" in key or "ID" in key:
            os.environ[key] = value
        if "VENDOR_URL" in key:
            os.environ[key] = value
