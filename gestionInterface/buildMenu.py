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
                                 hover_color="#555",border_width=1,command= lambda: fenetre.destroy())

    # Bouton À propos
    bouton_about = ctk.CTkButton(bouton_frame, text="À propos",fg_color="#111", border_color="#fff",text_color="#fff",
                                 hover_color="#555",border_width=1, command= lambda : about())

    # Placer les boutons côte à côte
    bouton_quitter.pack(side="right", padx=5, pady=5)
    bouton_about.pack(side="right", padx=5, pady=5)

    # Ajouter le frame des boutons au menu
    bouton_frame.pack(side="right", padx=5, pady=5)

    menu.pack(fill="both")
    

def about():
    """
    Fonction de présentation d'aide
    """

    about = ctk.CTkToplevel()
    about.title("A propos de l'application") 
    about.geometry("500x480")
    about.attributes('-topmost', True)
    
    ctk.CTkLabel(about,text="APPLICATION DE COMPTAGE DES OPERATIONS DANS UN PSEUDO CODE", text_color="#000", font=("Garamone",13),
                 fg_color="transparent").pack(fill="both", padx=5, pady=5)
    
    messageFrame = ctk.CTkFrame(about, height=370, corner_radius=1, fg_color="transparent")
    messageFrame.pack(fill= "both", padx=5, pady=10)

    texte= ctk.CTkTextbox(messageFrame, height=350, fg_color="transparent",border_width=1, corner_radius=5, font=("Garamone", 12))
    texte.pack(fill="both", padx=5, pady=5)
    message="""
Cette application est une suite du cours d'Algorithmique et Complexité.
Le but est de compter le nombre d'opérations effectuées dans le programme
Nous avons choisis d'utiliser le language python vue qu'il contient une fonction exec() permettant d'exécuter un programme python passer en paramètre sous la forme d'un string.
Nous introduisons une variable dans le programme pour compter le nombre d'opérations et le stocke le resultat dans un fichier et la répère plutard pour afficher à l'écran de l'utilisateur.
    
Pour avoir cette idée très simple nous avons travaillé en équipe de trois étudiants:

APEDO Kossi Emmanuel
ASLO Dogugu Honoré
HELOU Komlan Mawulé

Sous la superviseur de l'Ingénieur GUIFO, enseignant à Institut Africain d'Informatique.
    """

    texte.insert("1.0", message)
    texte.configure(state = "disabled")

    btnFrame =ctk.CTkFrame(about, height=60,fg_color="transparent", border_width=0)
    btnFrame.pack(fill="both", padx=5, pady=10, side= "bottom")
    
    btn = ctk.CTkButton(btnFrame, text="Fermer", fg_color="#000", hover_color="#555", height=40, corner_radius=5,
                  command= lambda: about.destroy())
    btn.pack(side="right")


    about.mainloop()