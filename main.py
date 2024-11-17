from requete_mistral import *
from docx import Document
import tkinter as tk
from tkinter import filedialog
from hybrid_search import *
from tkinter import ttk

out_put_path="C:/Users/Utilisateur/Downloads/lettre_jurydique.docx"


def save_letter_to_word(letter_text, output_path):
    document = Document()
    document.add_paragraph(letter_text)
    document.save(output_path)
    print('fichier bien enregistré')


# Fonction qui sera exécutée lorsque le bouton est cliqué
def envoyer():

    texte = entree_texte.get("1.0", tk.END) 
    afficher_texte("Recherche texte loi...")
    liste_texte_loi=hybrid_search(texte)
    afficher_texte("Rédaction de la lettre...")
    texte_final=make_final_prompt(liste_texte_loi, texte)
    reponse=appel_mistral(texte_final)
    afficher_texte(reponse)

# Fonction pour afficher un texte donné
def afficher_texte(texte_a_afficher):
    # Supprime le contenu précédent dans la zone d'affichage
    zone_affichage.delete("1.0", tk.END)
    # Affiche le texte fourni
    zone_affichage.insert(tk.END, texte_a_afficher)
    
def enregistrer():
# Récupère le texte dans la zone d'affichage
    texte_a_sauvegarder = zone_affichage.get("1.0", tk.END).strip()
    if not texte_a_sauvegarder:
        return  # Ne rien faire si la zone d'affichage est vide

    # Ouvre une boîte de dialogue pour choisir l'emplacement du fichier
    fichier_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
    )
    if fichier_path:  # Si un fichier est sélectionné
        document = Document()
        document.add_paragraph(texte_a_sauvegarder)
        document.save(fichier_path)


if __name__ == '__main__':

    #pb=" Mon propriétaire indique dans mon contrat de location que le salon fait partie de la partie privée de ma colocataire et qu'il n'y a pas de partie commune"
    # Création de la fenêtre principale
   # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("LAITRE")

    # Définition du style avec ttk
    style = ttk.Style(fenetre)
    style.theme_use("clam")  # Vous pouvez changer le thème si vous le souhaitez

    # Cadre principal
    main_frame = ttk.Frame(fenetre, padding=(20, 10))
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Création d'une zone de texte pour un paragraphe
    entree_label = ttk.Label(main_frame, text="Quel est votre problème ? ", font=("Helvetica", 12))
    entree_label.pack(anchor='w', pady=(0, 5))

    entree_texte = tk.Text(main_frame, height=10, width=80, font=("Helvetica", 11))
    entree_texte.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

    # Cadre pour organiser les boutons horizontalement
    cadre_boutons = ttk.Frame(main_frame)
    cadre_boutons.pack(pady=10)

    # Création du bouton "Envoyer"
    bouton_envoyer = ttk.Button(cadre_boutons, text="Envoyer", command=envoyer)
    bouton_envoyer.pack(side=tk.LEFT, padx=5)

    # Création du bouton "Download"
    bouton_download = ttk.Button(cadre_boutons, text="Download", command=enregistrer)
    bouton_download.pack(side=tk.LEFT, padx=5)

    # Zone pour afficher le texte fourni (affichée en dessous)
    label_affichage = ttk.Label(main_frame, text="Lettre:", font=("Helvetica", 12))
    label_affichage.pack(anchor='w', pady=(20, 5))

    zone_affichage = tk.Text(main_frame, height=15, width=80, font=("Helvetica", 11))
    zone_affichage.config(state='normal', bg='#f0f0f0')
    zone_affichage.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

    # Ajustement de la taille minimale de la fenêtre
    fenetre.minsize(800, 600)

    # Centrer la fenêtre sur l'écran
    fenetre.update_idletasks()
    width = fenetre.winfo_width()
    height = fenetre.winfo_height()
    x = (fenetre.winfo_screenwidth() // 2) - (width // 2)
    y = (fenetre.winfo_screenheight() // 2) - (height // 2)
    fenetre.geometry(f'{width}x{height}+{x}+{y}')

    # Lancement de la boucle principale de l'interface graphique
    fenetre.mainloop()

    