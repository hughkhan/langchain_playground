import cohere

co = cohere.Client("E4cEjzBhadaqJDnKhv9rHIgw9t1gni9PJq2zoCRX")
def reranked_documents():
    docs = [
        "Custom Computer Programming Services"
        "Software Publishers"
        "Computer Systems Design Services"
        "Computer Training"
        "Other Computer Related Services"
    ]

    response = co.rerank(
        model="rerank-english-v3.0",
        query="NAICS classification for business which Develops software products",
        documents=docs,
        top_n=3,
    )
    #return response["documents"]
    print(response)