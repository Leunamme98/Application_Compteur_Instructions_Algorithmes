"""
@auteur:  HELOU Komlan Mawulé
@but: Ce fichier constitue la barre de menu de l'application
@date: 01/06/2024
"""

#importation des modules puthon

import customtkinter as ctk


def buildMenu(fenetre : ctk.CTk):
    """
    A pour but de construire la barre de menu de l'application
    @param: fenetre (la fenetre pour laquelle le menu sera constructe)
    @return : None
    """

    # Le menu
    menu = ctk.CTkFrame(fenetre, fg_color="#111", corner_radius=0)

    # Les éléments du menu

    # Créer un frame pour les boutons
    bouton_frame = ctk.CTkFrame(menu, fg_color="#111", corner_radius=0)

    # Bouton Quitter
    bouton_quitter = ctk.CTkButton(bouton_frame, text="Quitter",fg_color="#111", border_color="#fff",text_color="#fff",
                                 border_width=1,command=fenetre.quit)

    # Bouton À propos
    bouton_about = ctk.CTkButton(bouton_frame, text="À propos",fg_color="#111", border_color="#fff",text_color="#fff",
                                 border_width=1,)

    # Placer les boutons côte à côte
    bouton_quitter.pack(side="left", padx=5, pady=5)
    bouton_about.pack(side="left", padx=5, pady=5)

    # Ajouter le frame des boutons au menu
    bouton_frame.pack(side="left", padx=5, pady=5)

    menu.pack(fill="both")
    
