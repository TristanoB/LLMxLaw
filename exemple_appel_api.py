import numpy as np 
import os
from mistralai import Mistral

# Remplacez par votre clé API
api_key = "oqGYCnR0lAOWD4bjBdYqifD2snwaL38J"

# Nom du modèle (par exemple, "mistral-7b")
model_name = "mistral-large-2407"


# Créer un client pour interagir avec l'API
client = Mistral(api_key=api_key)

# Exemple de requête : une simple conversation
try:
    response = client.chat.complete(
        model=model_name,
        messages=[
            {"role": "user", "content": "quelle est la capital des USA "}
        ]
    )

    # Afficher la réponse
    print("Réponse de l'IA :", response.choices[0].message.content)

except Exception as e:
    print("Une erreur est survenue :", e)
