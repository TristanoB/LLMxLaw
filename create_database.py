from langchain.schema import Document
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
import shutil

# Path definitions
CHROMA_PATH = "chroma_code-immo"
DATA_PATH = "docs lois immo"

# HuggingFace Embeddings model
embeddings_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

def save_to_chroma(chunks: list[str]):
    # Clear out the database first
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    print("Start embedding")

    # Convert strings to Document objects
    documents = [Document(page_content=text) for text in chunks]
    
    # Create a new DB from the documents
    db = Chroma.from_documents(
        documents, embeddings, persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

# Example usage
save_to_chroma(["Voici un texte à embedder", "voici un deuxième texte à embedder"])
