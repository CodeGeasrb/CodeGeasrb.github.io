# BOTO RAG SYSTEM

## Overview
The **BOTO RAG SYSTEM** is a Retrieval-Augmented Generation (RAG) system designed to power a chatbot using a Large Language Model (LLM). The primary purpose of this system is to generate text by extracting key information from PDF documents. The system operates by creating a database in Pinecone, utilizing the Ollama and Groq servers, all executed within a free Google Colab environment.

## How It Works
The BOTO RAG SYSTEM works as follows:
1. **Database Creation**: A database is created in Pinecone, where the necessary information from PDFs is stored and indexed.
2. **Text Generation**: The system uses the LLM to generate text based on the retrieved data.
3. **Server Connection**: The Ollama and Groq servers handle the heavy lifting, ensuring smooth operation and accurate information extraction.

## Getting Started
To apply this system with your own database, follow these steps:

1. **Pinecone Setup**:
   - Create an account on [Pinecone](https://www.pinecone.io/).
   - Obtain your API key and set up an index. The code comes with a predefined index name "test," which you should modify to suit your needs.
   - Replace the predefined API key in the code with your own.

2. **Groq Setup**:
   - Sign up on [Groq](https://wow.groq.com/) and obtain your API key. This is also free of charge.

3. **Run the System**:
   - Execute the code in Google Colab. The system will automatically connect to Pinecone and Groq, allowing you to start extracting and generating text from your PDFs.

## Troubleshooting
If you encounter the following error while working with this system:
ValueError: Error raised by inference endpoint: HTTPConnectionPool(host='localhost', port=11434): 
Max retries exceeded with url: /api/embeddings (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8a504c60e0>: 
Failed to establish a new connection: [Errno 111] Connection refused'))

Simply re-run the "connect servers" cell to re-establish the connection with the Ollama server.

## Conclusion
The **BOTO RAG SYSTEM** provides a powerful, accessible solution for extracting and generating text from PDFs using cutting-edge AI technology. With Pinecone and Groq, you can efficiently manage and scale your data processing needs, all within a free Google Colab environment.
