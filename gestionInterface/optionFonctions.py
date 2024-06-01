"""
@auteur:  HELOU Komlan Mawulé
@but: Ce fichier contient les fonctions permettants de géré les options
@date: 01/06/2024
"""

#importation des modules de python
import customtkinter as ctk
from tkinter import messagebox, filedialog

def importerFichier(editeur: ctk.CTkTextbox):
    # Liste des types de fichiers autorisés
    liste_des_types_de_fichier = [("Fichiers texte", "*.txt"), ("Fichiers PDF", "*.pdf"), ("Fichiers Word", "*.docx")]

    # Ouvrir une boîte de dialogue pour sélectionner un fichier
    fichier = filedialog.askopenfile(filetypes=liste_des_types_de_fichier)

    # Vérifier si un fichier a été sélectionné
    if fichier:
        # Lire le contenu du fichier
        contenu = fichier.read()
        # Afficher le contenu dans l'éditeur
        editeur.insert("end", contenu)
    else:
        # Afficher un message si aucun fichier n'a été sélectionné
        messagebox.showwarning("Aucun fichier sélectionné", "Aucun fichier n'a été sélectionné.")
