import csv
from langchain_core.documents import Document

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
    