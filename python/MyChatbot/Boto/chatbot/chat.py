from utils import run_command
from utils import create_memory, create_qa
from utils import header, user_input, bot_response, if_exit
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_pinecone import Pinecone
from langchain_community.llms import Ollama
import pinecone
import time


def chat(API_KEY_PINECONE, INDEX_NAME_PINECONE):
    # Install Ollama
    run_command("curl -fsSL https://ollama.com/install.sh | sh")

    # Start the Ollama server and redirect logs
    run_command("ollama serve > ollama.log 2>&1 &")

    # Wait for the server to start
    time.sleep(10)

    # Pull the llama3 model
    run_command("ollama pull llama3")

    # Initialize pinecone DB
    try:
        pncDB = pinecone.Pinecone(api_key=API_KEY_PINECONE)
        index = pncDB.Index(INDEX_NAME_PINECONE)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Initialize llama3 llm
    llm = Ollama(model="llama3", temperature=0.7)

    # Define an embedding model
    embedding_model_name = 'sentence-transformers/all-mpnet-base-v2'
    embedding_model = HuggingFaceBgeEmbeddings(model_name=embedding_model_name)

    # Initialize vector store
    vectorstore = Pinecone(index, embedding_model, "text")

    # Create chat memory
    memory = create_memory()

    # Create conversation chain in chat
    qa = create_qa(llm=llm, vectorstore=vectorstore, memory=memory)


    # Display header
    header()

    # Chat display
    while True:
        # user input
        input = user_input()
        
        # validate if user wants to exit
        exit = if_exit(user_input=user_input)
        if exit:
            break

        # get a bot responser
        result = qa({"question": user_input})
        response = result['answer']

        # display bot response
        bot_response(response=response)
        """
        if 'source_documents' in result:
            print("\nSources:")
            for doc in result['source_documents']:
                print(doc.page_content[:100] + "...")
        """
        print()






