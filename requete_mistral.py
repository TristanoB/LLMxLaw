from mistralai import Mistral

api_key = "oqGYCnR0lAOWD4bjBdYqifD2snwaL38J"

model_name = "mistral-large-2407"

client = Mistral(api_key=api_key)

def appel_mistral(texte):
    try:
        response = client.chat.complete(
            model=model_name,
            messages=[
                {"role": "user", "content": texte}
            ]
        )


        Reponse= response.choices[0].message.content

    except Exception as e:
        Reponse= "ERREUR"

    return Reponse


def make_final_prompt(liste_texte_loi, pb): 
    prompt="Bonjour Mistral, j'ai un problème de droit immobilier. Voici mon problème : \n"
    prompt+= pb + "\n"
    prompt+= "J'aimerais que tu me fasses un courrier d'avocat en utilisant les textes de lois suivants si tu les trouves pertinent,\n "
    prompt+= "N'hesite pas à bien développé tes arguments et à citer les texte avec des tirets \n "
    prompt+= " Voici les textes de lois : \n"

    for text in liste_texte_loi:
        prompt+= text + "\n"

    prompt+= "\n" + "Fais moi uniquement la lettre et ne mets pas en gras ou en itallique"

    return prompt 


if __name__ == '__main__':

    liste_texte_loi=["Art. 1er  (Ord. no 2019-1101 du 30 oct. 2019, art. 2, en vigueur le 1er juin 2020)  'I. — La présente loi régit tout immeuble bâti ou groupe d'immeubles bâtis à usage total ou partiel d'habitation dont la propriété est répartie par lots entre plusieurs personnes' ", 
                    "(L. no 2018-1021 du 23 nov. 2018, art. 206)  'Le lot de copropriété comporte obligatoirement une partie privative et une quote-part de parties communes, lesquelles sont indissociables.'Ce lot peut être un lot transitoire. Il est alors formé d'une partie privative constituée d'un droit de construire précisément défini quant aux constructions qu'il permet de réaliser et d'une quote-part de parties communes correspondante.' 'La création et la consistance du lot transitoire sont stipulées dans le règlement de copropriété.'"
    ]

    pb=" Mon propriétaire indique dans mon contrat de location que le salon fait partie de la partie privée de ma colocataire et qu'il n'y a pas de partie commune"

    texte =make_final_prompt(liste_texte_loi, pb)

    print(appel_mistral(texte))




