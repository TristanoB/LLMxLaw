from requete_mistral import *
from docx import Document
import tkinter as tk
from tkinter import filedialog
from hybrid_search import *

out_put_path="C:/Users/Utilisateur/Downloads/lettre_jurydique.docx"





def save_letter_to_word(letter_text, output_path):
    document = Document()
    document.add_paragraph(letter_text)
    document.save(output_path)
    print('fichier bien enregistré')


# Fonction qui sera exécutée lorsque le bouton est cliqué
def envoyer():
    texte = entree_texte.get("1.0", tk.END) 
    liste_texte_loi=hybrid_search(texte)
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


    