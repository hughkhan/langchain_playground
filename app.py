
import json
import sys
import os
import logging

from langchain_community.llms import ollama
from naics import get_naics_vectordb
from naics_llm_direct import get_naics_llm_direct
from sql_query import run_sql_query
from rerank import reranked_documents
from get_values import get_value_description

sys.path.append("/home/hughkhan/github/langchain_playground")
from config import set_environment
set_environment()

#-------------------------------------------------------------------------------
def main():

    print("Please choose an option from the menu:")
    print("Option 1: NAICS Vector DB Search")
    print("Option 2: NAICS LLM Direct Search")
    print("Option 3: NLP based sql query")
    print("Option 4: Rerank documents")
    print("Option 5: Get Definitions")
    print("Option 6: Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        get_naics_vectordb()
    elif choice == '2':
        get_naics_llm_direct()
    elif choice == '3':
        run_sql_query()
    elif choice == '4':
        reranked_documents()
    elif choice == '5':
        get_value_description()
    elif choice == '6':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
    
    main()

#-------------------------------------------------------------------------------

#-----------------------------------------------------------------------------
    

if __name__== "__main__" :
    main()
