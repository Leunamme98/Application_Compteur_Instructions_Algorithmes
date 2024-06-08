"""
@auteur:  HELOU Komlan Mawulé
@but: Ce fichier contient les fonctions permettants de géré les options
@date: 01/06/2024
"""

#importation des modules de python
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog

#importation des modules crées
import LecteurFichier as lf
import compteurDoperation as co

def importerFichier(editeur: ctk.CTkTextbox):
    """
    Cette fonction permet de charger le pseudo code depuis son emplacement dans le mini éditeur.
    @param: editeur (la zone d'édition de pseudo code)
    @return: none
    """
    # Liste des types de fichiers autorisés
    liste_des_types_de_fichier = [("Fichiers texte", "*.txt"), ("Fichiers PDF", "*.pdf"), ("Fichiers Word", "*.docx")]

    # Ouvrir une boîte de dialogue pour sélectionner un fichier
    fichier = filedialog.askopenfilename(filetypes=liste_des_types_de_fichier)
    
    # Vérifier si un fichier a été sélectionné
    if fichier:
    
        # Afficher le contenu dans l'éditeur
        editeur.configure(state= tk.NORMAL)
        editeur.delete("1.0", "end")

        liste_ligne, succes = lf.lireFichier(fichier)
        
        if succes and liste_ligne:
            for ligne in liste_ligne:
                
                editeur.insert("end", ligne)
            editeur.configure(state = "disabled")
        else:
            messagebox.showwarning("Importation de code", "Le fichier choisi est vide!")
    else:
        # Afficher un message si aucun fichier n'a été sélectionné
        messagebox.showwarning("Importation de code", "Aucun fichier n'a été sélectionné.")

def saisirPseudoCode(editeur: ctk.CTkTextbox):
    """
    Cette donnée la possibilité à l'utilisateur d'éditer et pseudo code.
    @param: editeur (la zone d'édition de code)
    """
    editeur.configure(state = "disabled")
    editeur.configure(state = tk.NORMAL)
    
    
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
        editeur.focus()

def analyserCode(editeur: ctk.CTkTextbox):
    """
    Cette fonction permet de récuéper le pseudo code de  l'éditeur et passeur à un analyseur. 
    Après l'analyseur, on affichera le resultat sur le autre fenetre
    @param: editeur (la zone d'édition de code)
    @return: none
    """

    code = editeur.get("1.0", "end-1c")

    if len(code)==0:
        messagebox.showwarning("Analyse du code", "Désolé! vous n'avez aucun code à analyser.")
    else:

        reponse , message = co.compteurOperation(code)

        
    
        if reponse:
            #Affichage du résultat
            affichage = ctk.CTkToplevel()
            affichage.title("Résultat de l'analyse")
            affichage.geometry("700x200")

            #Titre de la fenetre
            ctk.CTkLabel(affichage, text="RESULTAT DE L'ANALYSE", font=("Garamo", 14)).pack(fill="both", padx=10, pady=10)

            frame = ctk.CTkFrame(affichage, border_width=1, corner_radius=2)
            frame.pack(fill="both", padx=10, pady=10)


            message = "Nombre d'opération effectué: "+ str(message)
            ctk.CTkLabel(frame, text=message, font=("Garamone", 14)).pack(fill="both", padx=10, pady=10)

            boutonFrame=ctk.CTkFrame(affichage, border_width=0, corner_radius=0,fg_color="transparent")
            boutonFrame.pack(fill="both", padx=10, pady=10)

            btn=ctk.CTkButton(boutonFrame, text="Fermer", font=("Garamone", 13),height=40, hover_color="#555" , fg_color="black",
                               border_width=1, command= lambda: affichage.destroy())
            btn.pack(side="right", padx=0, pady=5)

            affichage.mainloop()
        else:

            message = "Erreur d'analyse: "+ message
            messagebox.showwarning("Erreur", message)

        
        


        
