import re  # Importer le module re pour les expressions régulières
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Définir le modèle d'embedder
embeddings_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_function = HuggingFaceEmbeddings(model_name=embeddings_model_name)

# Chargement de la base de données avec Chroma (en utilisant langchain_chroma)
CHROMA_PATH_CCom = "chroma_code-immo"
db_CCom = Chroma(persist_directory=CHROMA_PATH_CCom, embedding_function=embedding_function)

# Fonction de recherche hybride
def hybrid_search(query, k=5, keyword_weight=0.3, semantic_weight=0.7):
    """
    Combine la recherche sémantique et par mots-clés pour renvoyer des résultats hybrides.
    :param database: Base de données Chroma
    :param query: Requête utilisateur
    :param k: Nombre de résultats à retourner
    :param keyword_weight: Poids de la recherche par mots-clés
    :param semantic_weight: Poids de la recherche sémantique
    """
    
    # Recherche sémantique (embeddings)
    semantic_results = db_CCom.similarity_search_with_relevance_scores(query, k=k)

    
    # Recherche par mots-clés
    keyword_results = keyword_search(query, k=k)


    # Fusionner les résultats avec pondération (ex. 70% sémantique, 30% mots-clés)
    combined_results = {}

    # Utilisation de l'index comme clé pour éviter l'erreur de type non hashable
    for idx, (doc, score) in enumerate(semantic_results):
        combined_results[idx] = combined_results.get(idx, 0) + semantic_weight * score

    for idx, (doc, score) in enumerate(keyword_results):
        combined_results[idx] = combined_results.get(idx, 0) + keyword_weight * score

    # Trier les résultats par score (du plus élevé au plus bas)
    sorted_results = sorted(combined_results.items(), key=lambda x: x[1], reverse=True)

    # Récupérer les documents correspondants, en vérifiant que les indices existent dans `semantic_results`
    final_results = [(semantic_results[idx][0].page_content) 
                     for idx, _ in sorted_results if idx < len(semantic_results)]

    return final_results[:k]

# Fonction de recherche par mots-clés
def keyword_search(query, k=5):
    """
    Recherche des documents contenant des mots-clés extraits de la requête.
    :param database: Base de données Chroma
    :param query: Requête utilisateur
    :param k: Nombre de résultats à retourner
    """
    keywords = query.split()  # Divise la requête en mots-clés simples

    
    #### EXTRACTION MOTS IMPORTANTS ####
    
    keyword_results = []
    
    # Recherche par mots-clés dans les documents
    for doc, _ in db_CCom.similarity_search_with_relevance_scores(query, k=k):
        score = 0
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', doc.page_content) and len(keyword) > 5:  # Correspondance exacte
                score += 1
        if score > len(keywords)/2:
            keyword_results.append((doc, score))
    
    return keyword_results

# Exemple de requête
query = "Un voisin de mon immeuble ne veut pas payer ses charges de copropriété"
results = hybrid_search(query)


# Affichage des résultats
if __name__== '__main__':
    print(results)