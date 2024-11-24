from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain

def run_sql_query():
    #db = SQLDatabase.from_uri("postgresql://admin:secret@localhost:5432/chinook")
    db = SQLDatabase.from_uri("postgresql://postgres:secret@172.26.224.1:5432/froid")
    print(db.dialect)
    print(db.get_usable_table_names())
    #db.run("SELECT * FROM Artist LIMIT 10;")
    #results =db.run("SELECT * FROM member LIMIT 10;")

    #llm = ChatOpenAI(model="gpt-4o-mini")  #Langchain Model Wrapper

    llm = ChatOpenAI(                       #Langchain OpenAI Model Wrapper but going through AIML.com
        openai_api_base="https://api.aimlapi.com/v1/",
        openai_api_key="4c217676012e44e8958e8984aa839903",
        #model_name="Qwen/Qwen1.5-72B-Chat")
        #model_name="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo")
        #model_name="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
        #model_name="google/gemma-7b-it")
        #model_name="claude-3-sonnet-20240229")
        model_name="gpt-4o")
    
    
   
    #llm = ollama.Ollama(model="llama3.1") #Ollama Model Wrapper
    #llm = ollama.Ollama(model="mistral")  #Ollama Model Wrapper

    chain = create_sql_query_chain(llm, db)
    # chain.get_prompts()[0].pretty_print()

    context = db.get_context()
    #print(list(context))
    #print(context["table_info"])

    #response = chain.invoke({"question": "How many total tu are given to member, David Kelley?"})
    response = chain.invoke({"question": "List all tucomposites grouped by corporation.  Do not use the LIMIT clause."})
    #response = response.replace("\n", "")

    print(response)

    # index = response.find('SELECT')
    # response = response[index:]
    # index = response.find(';')
    # response = response[:index]

    # results = db.run(response)

    # print(results)


    # prompt_with_context = chain.get_prompts()[0].partial(table_info=context["table_info"])
    # print(prompt_with_context.pretty_repr()[:1500])
