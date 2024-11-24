from langchain_openai import ChatOpenAI


def get_answer_from_llm(prompt: str, query: str) -> str:

    llm = ChatOpenAI(                       #Langchain OpenAI Model Wrapper but going through AIML.com
        openai_api_base="https://api.aimlapi.com/v1/",
        openai_api_key="4c217676012e44e8958e8984aa839903",
        #model_name="Qwen/Qwen1.5-72B-Chat")
        #model_name="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo")
        #model_name="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
        #model_name="google/gemma-7b-it")
        #model_name="claude-3-sonnet-20240229")
        #model_name="gpt-4o-2024-08-06")
        model_name="gpt-4o-mini-2024-07-18")
    
    
    
    #resultfromllm = llm.invoke("input": f"Which of the following numbered NAICS classification titles best fits the business which developers software products:\n{}"})
    resultfromllm = llm.invoke (input=  f"{prompt}: \n\n " \
                                        f"{query}. \n" )
    #print(resultfromllm.response_metadata)
    return (resultfromllm.content)
