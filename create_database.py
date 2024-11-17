import json
from langchain.schema import Document
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
import shutil

# Path definitions
CHROMA_PATH = "chroma_code-immo"
DATA_PATH = "docs_lois_immo"

# HuggingFace Embeddings model
embeddings_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

def load_json_data(file_path: str):
    """Charge le fichier JSON contenant les articles"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_to_chroma(chunks: list[str], metadata: list[dict]):
    """Sauvegarde les chunks dans la base de données Chroma"""
    # Clear out the database first
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    print("Start embedding")

    # Convertir les chaînes de caractères en objets Document
    documents = [
        Document(page_content=text, metadata=meta) for text, meta in zip(chunks, metadata)
    ]
    
    # Créer une nouvelle base de données à partir des documents
    db = Chroma.from_documents(
        documents, embeddings, persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

# Fonction pour extraire les chunks et les métadonnées depuis le JSON
def prepare_chunks_from_json(data: list[dict]):
    """Prépare les chunks et les métadonnées à partir du JSON"""
    chunks = []
    metadata = []
    
    for entry in data:
        # Contenu de l'article
        content = entry.get("content", "")
        # Métadonnée avec le numéro d'article
        article_number = entry.get("article", "")
        
        # Ajouter le contenu et les métadonnées
        chunks.append(content)
        metadata.append({"article": article_number})
    
    return chunks, metadata

# Exemple d'utilisation
data = load_json_data("articles_test.docx.json")  # Remplace par le chemin de ton fichier JSON
chunks, metadata = prepare_chunks_from_json(data)
save_to_chroma(chunks, metadata)
