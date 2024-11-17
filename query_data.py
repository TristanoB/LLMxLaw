import argparse
from dataclasses import dataclass
from langchain.vectorstores.chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings

import openai


CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""
def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB.
    embedding_function = GPT4AllEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=9)
    if len(results) == 0:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    promptt = "Voici certains textes permettant de donner un certain contexte à ta réponse, il est très important que tu les utilises pour satisfaire le client:\n\n"+context_text+"\n\n De plus, le client a une question importante, la voici:\n\n" +query_text 
    print(promptt)
    
    from openai import OpenAI

    client = OpenAI()
    
    completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Tu es un avocat spécialisé dans le droit des affaires et des contrats. Tu sais absolument répondre avec toutes les données qu'on te fournira. Si besoin tu peux poser des questions pour plus de précision, pas plus."},
    {"role": "user", "content": promptt + "il est très important que tu répondes clairement et de manière complète à la question posée, réponds de manière précise\n\n"}
  ]
)

    print(completion.choices[0].message.content)
    print("\n")

    #model = ChatOpenAI()
    #response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    #formatted_response = f"Response: {response_text}\nSources: {sources}"
    #print(formatted_response)


if __name__ == "__main__":
    main()
