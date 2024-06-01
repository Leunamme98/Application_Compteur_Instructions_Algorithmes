"""
@auteur:  HELOU Komlan Mawulé
@but: Ce fichier constitue le panneau d'affichage et de saisie
@date: 01/06/2024
"""

#importation des modules de python
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import END

#importations des modules crées
import gestionInterface.optionFonctions as of
def saisir_pseudo_code():
    print("Action: Saisir du pseudo code")



def analyser_programme():
    print("Action: Analyser le programme")

def initialiser_editeur():
    print("Action: Initialiser l'éditeur")



def buildPanel(fenetre: ctk.CTk):
    """
    Construire le panneau où il y aura la zone d'affichage ou de saisie de l'algorithme.
    @paramètre: fenetre (fenetre dans laquelle le panneau sera construit)
    """
       # Fonction pour ajouter un tilde au début de chaque nouvelle ligne
    def add_tilde(event):
        # Obtenir la position actuelle du curseur
        current_pos = textbox.index("insert")
        line, column = map(int, current_pos.split('.'))

        if column == 0:
            textbox.insert(f"{line}.0", "~")
        else:
            textbox.insert(current_pos, "\n~")
        return "break"

    # Fonction pour empêcher la suppression du premier tilde
    def prevent_tilde_deletion(event):
        current_pos = textbox.index("insert")
        line, column = map(int, current_pos.split('.'))
        
        # Empêcher la suppression du premier tilde
        if line == 1 and column == 1:
            return "break"
        
        # Si le curseur est après un tilde, et que l'on supprime, on passe à la ligne précédente
        if column == 1 and line > 1:
            textbox.delete(f"{line}.0", f"{line}.1")
            textbox.mark_set("insert", f"{line-1}.end")
            return "break"
        
    
    def on_item_click(event):
    # Vérifier s'il y a au moins un élément sélectionné dans le TreeView
        

        if tree.selection():
            # Obtenir le premier élément sélectionné dans le TreeView
            item = tree.selection()[0]
            item_text = tree.item(item, "text")
            
            # Exécuter l'action appropriée en fonction de l'élément sélectionné
            if item_text == "1- Saisir du pseudo code":
                saisir_pseudo_code()
            elif item_text == "2- Importer un fichier":
                of.importerFichier(textbox)
            elif item_text == "3- Analyser le programme":
                analyser_programme()
            elif item_text == "4- Initialiser l'éditeur":
                initialiser_editeur()



    # Le panneau principal
    panel = ctk.CTkFrame(fenetre, fg_color="#eee")

    # Frame pour contenir le titre 
    titre_frame = ctk.CTkFrame(panel, fg_color="#eee", height=10, corner_radius=10)
    titre_frame.pack(fill="both",padx=15, pady=10)

    titre = ctk.CTkLabel(titre_frame, text="Mini éditeur de pseudo code", height=10, font=("Arial", 15))
    titre.pack(side="left")


    # TextBox scrollable Editeur
    editeur_frame = ctk.CTkFrame(panel, fg_color="#eee", corner_radius=0,border_color="#000", border_width=1)
    editeur_frame.pack(fill="both", padx=10, pady=10)
    
    textbox = ctk.CTkTextbox(editeur_frame, wrap="none",height=450, font=("Arial", 15,'bold'))
    textbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    textbox.bind("<Return>", add_tilde)
    textbox.bind("<BackSpace>", prevent_tilde_deletion)
    textbox.bind("<Delete>", prevent_tilde_deletion)
    textbox.insert("1.0", "~")
    

    #titre pour les options
    option_title_frame = ctk.CTkFrame(panel, fg_color="#eee", height=10, corner_radius=10)
    option_title_frame.pack(fill="both",padx=15, pady=10)

    option_title = ctk.CTkLabel(option_title_frame, text="Les options", height=10, font=("Arial", 15))
    option_title.pack(side="left")

    # Ajouter le panneau principal à la fenêtre
    option_frame = ctk.CTkFrame(panel, fg_color="#eee", corner_radius=0,border_color="#000", border_width=1)
    option_frame.pack(fill="both", padx=10, pady=10)

    
    # Création du TreeView widget
    tree = ttk.Treeview(option_frame, show="tree")
    tree.pack(fill="both", expand=True)

    # Configurer l'épaisseur des lignes
    style = ttk.Style()
    style.configure("Treeview", rowheight=35, font=("Arial", 13), fieldbackground="#FFFFFF")
    
    # Liste des actions
    actions = ["1- Saisir du pseudo code", "2- Importer un fichier", "3- Analyser le programme", "4- Initialiser l'éditeur"]

    # Ajout des actions au TreeView
    for action in actions:
        tree.insert("", "end", text=action)

    # Liaison de l'événement de clic à la fonction on_item_click
    tree.bind('<ButtonRelease-1>', on_item_click)
        # Listbox pour afficher les actions
    


    panel.pack(fill="both", expand=True)