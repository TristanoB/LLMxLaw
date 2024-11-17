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
        Reponse= "OUPS! une erreur est survenue "

    return Reponse

inputs_user_example = {"date_redaction" : None,
"coordonne_destinataire" : None,
"coordonne_expediteur" : None,
"bref_expose_litige" : None,
"reclamation" : None,
"delai" : None }

def make_final_prompt(liste_texte_loi, pb, inputs_user=inputs_user_example): 
    prompt= "Tu es un avocat dans le droit immobilier, tu connais parfaitement le droit, et on te fournira des textes les plus pertinents pour répondre à ce dont tu as besoin. Il est très important que tu respectes les consignes pour satisfaire ton client."
    prompt+="j'ai un problème de droit immobilier. Voici mon problème : \n"
    prompt+= pb + "\n"
    prompt+= "J'aimerais que tu me fasses un courrier d'avocat en utilisant les textes de lois suivants si tu les trouves pertinent,\n "
    prompt+= "N'hesite pas à bien développé tes arguments et à citer les texte avec des tirets \n "
    prompt+= f"Vérifie si cette mise en demeure est conforme à la législation française en vigueur et introduit les valeurs des termes suivant, en les reformulant si besoin : la date de rédaction {inputs_user["date_redaction"]} ; les coordonnées du destinataire - valeur : {inputs_user["coordonne_destinataire"]} ; les coordonnées de l'expéditeur - valeur : {inputs_user["coordonne_expediteur"]} ; un bref exposé du litige - valeur : {inputs_user["bref_expose_litige"]} : il est important de décrire clairement les circonstances qui ont donné naissance au litige pour éviter toute mauvaise compréhension de la part du destinataire ; la mention mise en demeure  : cette mention indique au destinataire qu'il s'agit de la première étape d'une procédure qui vous permettra ensuite de saisir le juge si vous n'obtenez pas de réponse satisfaisante ; la réclamation, soit ce que doit effectuer le destinataire afin de régler le litige - valeur : {inputs_user["reclamation"]}; un délai précis et raisonnable durant lequel le destinataire devra régler le litige, compris le plus souvent entre 8 et 15 jours selon la nature du litige - valeur : {inputs_user["delai"]} ; la signature de l'expéditeur."
    prompt+= " Voici les textes de lois : \n"

    for text in liste_texte_loi:
        prompt+= text + "\n"

    prompt+= "\n" + "Fais moi uniquement la lettre et ne mets pas en gras ou en itallique. Je veux absolument que tu mettes cette phrase: 'Par ailleurs, je vous informe que la présente mise en demeure fait courir des intérêts au taux légal conformément aux dispositions de l’article 1344-1 du Code civil.'"

    return prompt 

def is_ok(lettre, liste_texte_loi):
    prompt = "Voici un courrier d'avocat: \n" + lettre + "\n et voici un ensemble de texte de lois: \n" + "\n".join(liste_texte_loi) + "\n Je veux que tu compares ce qui est cité dans la lettre et dans la liste. Si il y a un fondement juridique qui est dans la lettre et pas dans la liste, renvoie toujours FALSE, sinon renvoie toujours TRUE, renvoie UNIQUEMENT CETTE VALEUR, RIEN DE PLUS SINON ÇA VA BUGGER"
    return appel_mistral(prompt)


#prend la lettre et un fondement en entrée, et retourne la lettre re rédigée sans les fondements énoncés
def enlever_fondement_nul(lettre, fondement):
    prompt = "Je vais te donner un courrier d'avocat, le voici:\n" + lettre + "\n Je veux que tu enlèves ces fondements juridiques en particulier, il est très important que tu ne rajoutes pas d'autres fondements, réécris juste la lettre sans ce fondement en particulier, car l'avocat référrent et sénior considère que ce n'est pas nécessaire. Je parle de ce fondement là:\n"+ "\n".join(fondement) + "\nje veux que tu renvoies UNIQUEMENT la lettre, rien d'autre, pas d'intro ni de conclusion"
    return appel_mistral(prompt)

if __name__ == '__main__':

    liste_texte_loi=["Art. 1er  (Ord. no 2019-1101 du 30 oct. 2019, art. 2, en vigueur le 1er juin 2020)  'I. — La présente loi régit tout immeuble bâti ou groupe d'immeubles bâtis à usage total ou partiel d'habitation dont la propriété est répartie par lots entre plusieurs personnes' ", 
                    "(L. no 2018-1021 du 23 nov. 2018, art. 206)  'Le lot de copropriété comporte obligatoirement une partie privative et une quote-part de parties communes, lesquelles sont indissociables.'Ce lot peut être un lot transitoire. Il est alors formé d'une partie privative constituée d'un droit de construire précisément défini quant aux constructions qu'il permet de réaliser et d'une quote-part de parties communes correspondante.' 'La création et la consistance du lot transitoire sont stipulées dans le règlement de copropriété.'"
    ]

    pb=" Mon propriétaire indique dans mon contrat de location que le salon fait partie de la partie privée de ma colocataire et qu'il n'y a pas de partie commune"

    texte =make_final_prompt(liste_texte_loi, pb)
    lettre =  appel_mistral(texte)
    
    while is_ok(lettre, liste_texte_loi) == "FALSE" :
        

        lettre = appel_mistral(texte + "Cite uniquement les citations que je t'ai donné et vraiment rien d'autre, c'est très très important")
       


    prompt = "Je vais te donner un courrier d'avocat, j'ai besoin que tu m'extraies toutes les citations juridiques (uniquement les articles et jurisprudences, pas les textes en tant que tel stp, JE VEUX UNIQUEMENT LA RÉFÉRENCE) de cette lettre. Voici la lettre :\n" + lettre + "\n je veux que tu me le fasses absolument sous le format suivant, c'est très important: [FONDEMENT]référence n°1[/FONDEMENT][FONDEMENT]référence n°2[/FONDEMENT][FONDEMENT]référence n°3[/FONDEMENT]etc..."
    fondements = appel_mistral(prompt)
    fondements_liste = []
    for f in fondements.split("[FONDEMENT]"):
        if "[/FONDEMENT]" in f:
            fondements_liste.append(f.split("[/FONDEMENT]")[0] )
            
    

