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
import os
import signal

#importations des modules crées
import gestionInterface.optionFonctions as of





def buildPanel(fenetre: ctk.CTk):
    """
    Construire le panneau où il y aura la zone d'affichage ou de saisie de l'algorithme.
    @paramètre: fenetre (fenetre dans laquelle le panneau sera construit)
    """
       # Fonction pour ajouter un tilde au début de chaque nouvelle ligne

    # Fonction pour empêcher la suppression du premier tilde
   
    def on_item_click(event):
    # Vérifier s'il y a au moins un élément sélectionné dans le TreeView
        

        if tree.selection():
            # Obtenir le premier élément sélectionné dans le TreeView
            item = tree.selection()[0]
            item_text = tree.item(item, "text")
            
            # Exécuter l'action appropriée en fonction de l'élément sélectionné
            if item_text == "1- Saisir du pseudo code":
                of.saisirPseudoCode(textbox)
            elif item_text == "2- Importer un fichier":
                of.importerFichier(textbox)
            elif item_text == "3- Analyser le programme":
                of.analyserCode(textbox)
            elif item_text == "4- Initialiser l'éditeur":
                of.initialiserEditeur(textbox)



    # Le panneau principal
    panel = ctk.CTkFrame(fenetre, fg_color="#eee")

    # Frame pour contenir le titre 
    titre_frame = ctk.CTkFrame(panel, fg_color="#eee", height=10, corner_radius=10)
    titre_frame.pack(fill="both",padx=15, pady=10)

    titre = ctk.CTkLabel(titre_frame, text="Mini éditeur de code", height=10, font=("Arial", 15))
    titre.pack(side="left")


    # TextBox scrollable Editeur
    editeur_frame = ctk.CTkFrame(panel, fg_color="#eee", corner_radius=0,border_color="#000", border_width=1)
    editeur_frame.pack(fill="both", padx=10, pady=10)
    
    textbox = ctk.CTkTextbox(editeur_frame, wrap="none",height=350, font=("Garamone", 18), state= "disabled")
    textbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    

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

