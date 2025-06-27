# utils/vector_utils.py

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings # or HuggingFaceEmbeddings
from langchain_core.documents import Document
import os

def create_vectorstore(transcript_text):
    # 1. Chunk the transcript
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(transcript_text)
    
    documents = [Document(page_content=chunk) for chunk in chunks]

    # 2. Create embeddings
    embeddings = OpenAIEmbeddings()  # You can replace with Gemini if needed
    
    # 3. Create FAISS vectorstore
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore