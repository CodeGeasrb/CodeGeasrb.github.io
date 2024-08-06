from app.utils import process_and_upsert_documents
import pinecone
import os

def create_DB(API_KEY_PINECONE, INDEX_NAME_PINECONE):
    # get documents path
    current_dir = os.getcwd()
    docs_path = os.path.join(current_dir, "documents")

    # Initialize pinecone DB
    try:
        pncDB = pinecone.Pinecone(api_key=API_KEY_PINECONE)
        index = pncDB.Index(INDEX_NAME_PINECONE)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    process_and_upsert_documents(docs_path=docs_path,pnc_index=index)




