import tkinter as tk

# Fonction qui sera exécutée lorsque le bouton est cliqué
def envoyer():
    texte = entree_texte.get("1.0", tk.END)  # Récupère le texte de l'entrée
    print(f"Texte envoyé : {texte}")
    # Tu peux ajouter ici ton traitement ou ta fonction

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Interface graphique avec entrée de texte")

# Création d'une zone de texte pour un paragraphe
entree_texte = tk.Text(fenetre, height=10, width=50)
entree_texte.pack(pady=10)

# Création du bouton "Envoyer"
bouton_envoyer = tk.Button(fenetre, text="Envoyer", command=envoyer)
bouton_envoyer.pack()

# Lancement de la boucle principale de l'interface graphique
fenetre.mainloop()
