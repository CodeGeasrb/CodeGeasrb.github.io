from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from pinecone import Vector
from tqdm import tqdm
import subprocess
import os


# SERVE CONFIGURATION FUNCTIONS
# Function to run commands in a python script
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}\n{stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))



# DATABASE CREATION FUNCTIONS
# Function to upload and process pdf documents into a vectorized Database
def process_and_upsert_documents(docs_path, pnc_index, embedding_model_name=None):
  # define embedding model
  if embedding_model_name is None:
    embedding_model_name = 'sentence-transformers/all-mpnet-base-v2'

  # initialize embedding model
  embedding_model = HuggingFaceBgeEmbeddings(model_name=embedding_model_name)

  # intialize text splitter
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

  # list of documents names
  docs_names = os.listdir(docs_path)

  # process documents
  for name in docs_names:
      if name.endswith('.pdf'):
          # create file paths
          file_path = os.path.join(docs_path, name)

          try:
              # upload pdf documents
              loader = PyMuPDFLoader(file_path)
              document = loader.load()

              # chunk documents
              chunks = text_splitter.split_documents(document)

              # create embedding vectors based on chunks
              vectors = []
              for i, chunk in enumerate(chunks):
                  vector_id = f"{name}-{i}"
                  vector_values = embedding_model.embed_documents([chunk.page_content])[0]
                  vector = Vector(
                      id=vector_id,
                      values=vector_values,
                      metadata=chunk.metadata
                  )
                  vectors.append(vector)

              # upsert vectors into the databse
              batch_size = 100
              total_vectors = len(vectors)
              for i in tqdm(range(0, total_vectors, batch_size), desc=f"Upserting {name}"):
                  batch = vectors[i:i+batch_size]
                  pnc_index.upsert(
                      vectors=batch,
                      namespace=name,
                      show_progress=False
                  )

              print(f'Document {name} was succesfully upload!')

          except Exception as e:
              print(f'Error in processing file: {name}: {e}')



# CHAT LOGIC FUNCTIONS
# Function to create memory in chat
def create_memory():
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    return memory 


# Function to create conversation chain
def create_qa(llm, vectorstore, memory):
    qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    memory=memory
)

    return qa



# CHAT DISPLAY FUNCTIONS
# header
def header():
    print("¡Hello, I am Boto, your personal AI-Assistant! (Type 'exit' to quit)")


# user
def user_input():
    return input("You: ")


# bot
def bot_response(response):
    print("🤖 Assistant:", response)

# exit message
def if_exit(user_input):
    if user_input.lower() == "exit":
        print("Goodbye!")
        return True



# APP DISPLAY FUNCTIONS
# Function to give a welcome message
def welcome():
    print(print("Welcome to your personal AI-Assistant app🤖"))


# Function to input pinecone info requirements
def pinecone_access():
    # input Api key for pinecone DB previous created
    API_KEY_PINECONE = input('Pinecone API Key: ')

    # input index name from a pinecone db
    INDEX_NAME_PINECONE = input('Pinecone index name: ')
    
    return API_KEY_PINECONE, INDEX_NAME_PINECONE


# Function to display an app menu
def options():
    options = ['Chat with Boto', 'Create a new DataBase', 'Exit']
    
    for number, option in enumerate(options, start=1):
        print(f'{number}. {option}')
    
    answer = None
    while answer is None:
        answer = input('What would you like to do?')
        try:
            answer = int(answer)
        except ValueError as e:
            print(f"{e}: Type (1) or (2) to select an option or (3) to exit")
        
        if answer == 1 or answer == 2 or answer == 3:
            os.system('cls')
            return answer
        else:
            print("Type (1) or (2) to select an option or (3) to exit")
    



