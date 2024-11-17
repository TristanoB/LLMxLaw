# LLMxLaw

# L.AI.T.T.R.E - drafting french demand letters



## Subject : 

Aiming to help french individuals and professionals with drafting demand letters (mises en demeure) in an accessible and user-friendly way, breaking down the complexity of the laws.

Simple and effective: our goal is to help french individuals and professionals draft demand letters that are well-documented and meet legal requirements. The user inputs the context and necessary data, and the tool generates a ready-to-use letter, including the relevant legal articles with explanations.                      If the user disagrees with any article, they can remove it, and the letter will be regenerated.                                                                     Conversely, if the user sees a relevant article from a list of suggested ones, the AI assesses its relevance and, if appropriate, updates the letter to include it.

## Implemented : 
the redaction of the letter, the summary of the law articles used, the removal of the law articles the user does not want to use, the user inputs


## To be implemented : brief explanation of law articles of the letter to the user, recommandation of other law articles that might also be used




## Pipeline : 

1. Création base de données utilisable pour RAG
    -> Appliquer sur un seul sujet précis pour base de donnée pas trop lourde : droit immobilier 
        -> Code civil, droit immo
    -> Vectoriser les documents 
2. Déploiement LLM, génération d'un courrier d'avocat 
    -> Prompt engineering pour avoir un bon template  
    -> Utilisation API Mistral
3. Extraction et modification des morceaux juridiques du courrier

LLM used  : Mistral Large 2 via MistralAPI
Method : prompt engineering + RAG of french law articles (chunked by article)
(new prompt is generated to remove or add a law article)
New relevant articles to add could be suggested and explained by AI, allowing the user to send the strongest demand letter  🦾 🚀
Our goal was to make the inputs simple to enter, by indicating what the user needs to add (name, reclamation...), making the process accesible for everyone 🤗



