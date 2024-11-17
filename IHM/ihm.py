import tkinter as tk

# Fonction qui sera exécutée lorsque le bouton est cliqué
def envoyer():
    texte = entree_texte.get("1.0", tk.END)  # Récupère le texte de l'entrée
      # Appelle la fonction pour afficher ce texte

# Fonction pour afficher un texte donné
def afficher_texte(texte_a_afficher):
    # Supprime le contenu précédent dans la zone d'affichage
    zone_affichage.delete("1.0", tk.END)
    # Affiche le texte fourni
    zone_affichage.insert(tk.END, texte_a_afficher)


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Interface graphique avec entrée et affichage de texte")

# Création d'une zone de texte pour un paragraphe
entree_texte = tk.Text(fenetre, height=15, width=100)
entree_texte.pack(pady=10)

# Cadre pour organiser les boutons horizontalement
cadre_boutons = tk.Frame(fenetre)
cadre_boutons.pack(pady=10)

# Création du bouton "Envoyer"
bouton_envoyer = tk.Button(cadre_boutons, text="Envoyer", command=envoyer)
bouton_envoyer.pack(side=tk.LEFT, padx=5)

# Création du bouton "Download"
bouton_download = tk.Button(cadre_boutons, text="Download", command=enregistrer)
bouton_download.pack(side=tk.LEFT, padx=5)

# Zone pour afficher le texte fourni (affichée en dessous)
label_affichage = tk.Label(fenetre, text="Réponse du modèle :", anchor="w", justify="left")
label_affichage.pack(pady=5, anchor="w")  # Aligné à gauche

zone_affichage = tk.Text(fenetre, height=20, width=100, state="normal")
zone_affichage.pack(pady=10, anchor="w")  # Aligné à gauche

# Lancement de la boucle principale de l'interface graphique
fenetre.mainloop()
