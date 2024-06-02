"""
@auteur:  HELOU Komlan Mawulé
@but: Ce fichier contient les fonctions permettants de géré les options
@date: 01/06/2024
"""

#importation des modules de python
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog

def importerFichier(editeur: ctk.CTkTextbox):
    """
    Cette fonction permet de charger le pseudo code depuis son emplacement dans le mini éditeur.
    @param: editeur (la zone d'édition de pseudo code)
    @return: none
    """
    # Liste des types de fichiers autorisés
    liste_des_types_de_fichier = [("Fichiers texte", "*.txt"), ("Fichiers PDF", "*.pdf"), ("Fichiers Word", "*.docx")]

    # Ouvrir une boîte de dialogue pour sélectionner un fichier
    fichier = filedialog.askopenfile(filetypes=liste_des_types_de_fichier)

    # Vérifier si un fichier a été sélectionné
    if fichier:
        # Lire le contenu du fichier
        contenu = fichier.read()
        # Afficher le contenu dans l'éditeur
        editeur.configure(state= tk.NORMAL)
        editeur.delete("1.1", "end")
        editeur.insert("end", contenu)
        editeur.configure(state = "disabled")
    else:
        # Afficher un message si aucun fichier n'a été sélectionné
        messagebox.showwarning("Aucun fichier sélectionné", "Aucun fichier n'a été sélectionné.")

def saisirPseudoCode(editeur: ctk.CTkTextbox):
    """
    Cette donnée la possibilité à l'utilisateur d'éditer et pseudo code.
    @param: editeur (la zone d'édition de code)
    """
    editeur.configure(state = "disabled")
    editeur.configure(state = tk.NORMAL)
    
    code = editeur.get("1.0", "end-1c")
    
    if len(code) == 0:
        editeur.insert("1.0", "~")
    elif len(code)>1 :
        editeur.insert("end","\n~")
    editeur.focus()


def initialiserEditeur(editeur: ctk.CTkTextbox):
    """
    Cette fonction permet d'initialiser l'éditeur en éffaçant toutes les lignes écrites
    @param: editeur (la zone d'édition de code)
    @return: 
    """
    answer = messagebox.askquestion("Initialisation de l'éditeur", "Êtes vous certain d'initialiser l'éditeur?")
    if answer == "yes":
        editeur.configure(state = tk.NORMAL)
        editeur.delete("1.0", "end")
        editeur.insert("1.0", "~")
        editeur.focus()

def analyserCode(editeur: ctk.CTkTextbox):
    """
    Cette fonction permet de récuéper le pseudo code de  l'éditeur et passeur à un analyseur. 
    Après l'analyseur, on affichera le resultat sur le autre fenetre
    @param: editeur (la zone d'édition de code)
    @return: none
    """

    code = editeur.get("1.0", "end-1c")

    if len(code)==0 or len(code)==1:
        messagebox.showwarning("Analyse du code", "Désolé! vous n'avez aucun code à analyser.")
    else:
        code_in_liste = code.split("\n")
        les_lignes_de_codes = list()

        for ligne in code_in_liste:
            les_lignes_de_codes.append(ligne[1:])
            
        
