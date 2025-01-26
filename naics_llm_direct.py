from langchain_openai import ChatOpenAI
import os

def get_naics_llm_direct():

    #llm = ChatOpenAI(model="gpt-4o", temperature=0)
    llm = ChatOpenAI(                       #Langchain OpenAI Model Wrapper but going through AIML.com
        openai_api_base=os.environ["VENDOR_URL"],
        openai_api_key=os.environ["AIMLAPI_KEY"],
        #model_name="Qwen/Qwen1.5-72B-Chat")
        #model_name="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo")
        #model_name="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
        #model_name="google/gemma-7b-it")
        #model_name="claude-3-sonnet-20240229")
        model_name="gpt-4o")
   
    query = input("Please enter your primary business activity: ")
    
    #resultfromllm = llm.invoke("input": f"Which of the following numbered NAICS classification titles best fits the business which developers software products:\n{}"})
    resultfromllm = llm.invoke (input=   f"You are an insurance underwriter. In order to properly assess the business risk you need to accuratly assess the business NAICS classification. " \
                                        f"Which NAICS classification code fits the best for a business which engages in {query}: \n " \
                                        f"Provide the result in JSON format {{'code': 'code', 'title': 'title', 'description': 'description'}} \n "\
                                        f"Pick the next three best matches and display them on the next line in the same JSONformat. \n " 
                                )
    print(resultfromllm.content)
    print(resultfromllm.response_metadata)