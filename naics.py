from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
import csv
import numpy as np
#from IPython.display import display, Markdown, Latex

def build_documents() -> list[Document]:
    csv_file_path = '/home/hughkhan/data/output.csv'

    with open(csv_file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='|')
        
        header = next(csv_reader)
        documentList = []
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Assuming the CSV has three columns
            sequence = row[0]
            code = row[1]
            title = row[2]
            description = row[3]
            documentList.append(Document(id=code, page_content=description, metadata={"title": title, "code": code}))

        return documentList

def get_naics_vectordb():
    #db = SQLDatabase.from_uri("postgresql://postgres:secret@172.26.224.1:5432/froid")


    # loader = CSVLoader(file_path='/home/hughkhan/data/output.csv',
    # csv_args={
    #     'delimiter': '|',
    #     'quotechar': '"',
    #     'fieldnames': ['Seq. No.', 'NAICS Code', 'Title', 'Description']
    # })

    # documents = loader.load()

    # print(documents[0].page_content[:100])
    # print(documents[0].metadata)

    vector_store = Chroma(
        collection_name="naics",
        embedding_function=OpenAIEmbeddings(),
        persist_directory="/home/hughkhan/data/naics",
        # other params...
    )


    # document_1 = Document(page_content="This industry comprises establishments primarily engaged in growing soybeans and/or producing soybean seeds.", metadata={"title": "Soybean Farming"})
    # document_2 = Document(page_content="This industry comprises establishments primarily engaged in growing fibrous oilseed producing plants and/or producing oilseed seeds, such as sunflower, safflower, flax, rape, canola, and sesame.", metadata={"title": "Oilseed (except Soybean) Farming"})
    # document_3 = Document(page_content="This industry comprises establishments primarily engaged in growing dry peas, beans, and/or lentils.", metadata={"title": "Dry Pea and Bean Farming"})

    # documents = [document_1, document_2, document_3]
    # ids = ["111110", "111120", "111130"]

    # documents = [
    #     {"id": "111110", "text": "This industry comprises establishments primarily engaged in growing soybeans and/or producing soybean seeds."},
    #     {"id": "111120", "text": "This industry comprises establishments primarily engaged in growing fibrous oilseed producing plants and/or producing oilseed seeds, such as sunflower, safflower, flax, rape, canola, and sesame."},
    #     {"id": "111130", "text": "This industry comprises establishments primarily engaged in growing dry peas, beans, and/or lentils."}
    # ]
    
    # texts = [doc["text"] for doc in documents]
    # ids = [doc["id"] for doc in documents]

    # vector_store.add_texts(texts=texts, ids=ids)

    if vector_store._collection.count() < 1:
        documents = build_documents()
        vector_store.add_documents(documents=documents)
   
    #embeddings = OpenAIEmbeddings()

    query = input("Please enter your primary business activity: ")
    #query_embedding = embeddings.embed_query(query)
    #results = vector_store.similarity_search_by_vector(query_embedding, k=11)
    #results = vector_store.similarity_search(query, k=11)
    results = vector_store.similarity_search_with_score(query, k=30)
    

    for result in results:
        #print(f"ID: {result.id}, Text: {result.page_content}, Metadata: {result.metadata}")
        #print(f"ID: {result.id},  Metadata: {result.metadata}")
        #print(f"{result[0].page_content} [{result[0].metadata}] {result[0].id} Score: {result[1]}")
        #print(f"[{result[0].metadata}] {result[0].id} Score: {result[1]}")
        print(f"{result[1]} [{result[0].metadata}]")

    scores = [result[1] for result in results]
    subScores = scores

    # std_dev = np.std(subScores)
    # print(f"Standard Deviation: {std_dev}")
    # print(f"Diff 0-1: {abs(scores[0] - scores[1])} --- Percentage of Standard Deviation: {abs(abs(scores[0] - scores[1]) - std_dev)/std_dev*100}")
    # print(f"Diff 1-2: {abs(scores[1] - scores[2])} --- Diff from Standard Deviation: {abs(abs(scores[1] - scores[2]) - std_dev)/std_dev*100}")
    # print(f"Diff 2-3: {abs(scores[2] - scores[3])} --- Diff from Standard Deviation: {abs(abs(scores[2] - scores[3]) - std_dev)/std_dev*100}")
    # print(f"Diff 3-4: {abs(scores[3] - scores[4])} --- Diff from Standard Deviation: {abs(abs(scores[3] - scores[4]) - std_dev)/std_dev*100}")
    # print(f"Diff 4-5: {abs(scores[4] - scores[5])} --- Diff from Standard Deviation: {abs(abs(scores[4] - scores[5]) - std_dev)/std_dev*100}")
    # print(f"Diff 5-6: {abs(scores[5] - scores[6])} --- Diff from Standard Deviation: {abs(abs(scores[5] - scores[6]) - std_dev)/std_dev*100}")
    # print(f"Diff 6-7: {abs(scores[6] - scores[7])} --- Diff from Standard Deviation: {abs(abs(scores[6] - scores[7]) - std_dev)/std_dev*100}")
    # print(f"Diff 7-8: {abs(scores[7] - scores[8])} --- Diff from Standard Deviation: {abs(abs(scores[7] - scores[8]) - std_dev)/std_dev*100}")
    # print(f"Diff 8-9: {abs(scores[8] - scores[9])} --- Diff from Standard Deviation: {abs(abs(scores[8] - scores[9]) - std_dev)/std_dev*100}")
    # print(f"Diff 9-10: {abs(scores[9] - scores[10])} --- Diff from Standard Deviation: {abs(abs(scores[9] - scores[10]) - std_dev)/std_dev*100}")

 
    mean = np.mean(subScores)
    std_dev = np.std(subScores)

    # Calculate the z-scores
    z_scores = [(x - mean) / std_dev for x in subScores]

    index_below_one = next((index for index, num in enumerate(z_scores) if num > -1), None)
    if index_below_one is not None:
        print(f"Data point {index_below_one} has a z-score above -1.0")
        sendbacklist = results[:index_below_one]
        sendbacklistmetadata = []
        for i in range(0,index_below_one): 
            sendbacklistmetadata.append(sendbacklist[i][0].metadata["code"] + ": " + sendbacklist[i][0].metadata["title"] + ", ")
            print(sendbacklistmetadata[i])

    llm = ChatOpenAI(                       #Langchain OpenAI Model Wrapper but going through AIML.com
        openai_api_base="https://api.aimlapi.com/v1/",
        openai_api_key="4c217676012e44e8958e8984aa839903",
        #model_name="Qwen/Qwen1.5-72B-Chat")
        #model_name="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo")
        #model_name="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
        model_name="google/gemma-7b-it")
    
    #resultfromllm = llm.invoke("input": f"Which of the following numbered NAICS classification titles best fits the business which developers software products:\n{}"})
    resultfromllm = llm.invoke(input=f"Which of the following coded NAICS classification titles best fits the business which engages in {query}: \n "\
                                        f"{sendbacklistmetadata}. \n Provide the answer in the format 'code: title'. Pick the next two best matches and display them on the next line in the same format")
    print(resultfromllm.content)



    # for i, z in enumerate(z_scores, 1):
    #     print(f"Z-score for data point {i}: {z}")1


    # zipped = list(zip(results, z_scores))
    # sendBack = []
    # for i, z in enumerate(zipped,0):
    #     print(f"datapoint {i}: {z[0][0].metadata} {z[0][1]} {z[1]}")

    #vector_store.persist()

    #vector_store.add_documents(documents=documents, ids=ids)

    # results = vector_store.similarity_search(query="we farm legumes", k=1)
    # for doc in results:
    #     print(f"* {doc.page_content} [{doc.metadata}] {doc.id}")