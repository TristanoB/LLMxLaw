from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.vectorstores.chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.embeddings import GPT4AllEmbeddings

import os
import shutil
import nltk
import time

import ssl


import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"
embeddings_model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
gpt4all_embd = GPT4AllEmbeddings()





CHROMA_PATH = "chroma_code-civil_REPERTOIRE_HF"
DATA_PATH = "code-civil-repertoire-MD-FINAL"


def main():
    start_time = time.time()
    print("Temps début:", start_time, "secondes")
    generate_data_store()
    end_time = time.time()
    print("Temps total d'exécution:", end_time - start_time, "secondes")



def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=400,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)
    query_result = HuggingFaceEmbeddings(model_name=embeddings_model_name).embed_query(document.page_content)
    print(query_result)
    
    
    
    

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    print("start embbeding")
    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, HuggingFaceEmbeddings(model_name=embeddings_model_name), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()
