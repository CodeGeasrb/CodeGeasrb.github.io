from app.chat import chat
from app.data import create_DB
from app.utils import welcome, options, pinecone_access
import os


def run_app():
    # welcome message
    welcome()

    # Connect to a pinecone DB
    API_KEY_PINECONE, INDEX_NAME_PINECONE = pinecone_access()
    
    # app menu manager logic
    option = None
    while option is None:
        # display options menu
        option = options()

        if option == 1:
            chat(API_KEY_PINECONE, INDEX_NAME_PINECONE)
        elif option == 2:
            create_DB()
        else:
            break

        option = None
        os.system('cls')


