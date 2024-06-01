
#importation des modules pythons
import customtkinter as ctk


#importation des modules crées
import gestionInterface.buildMenu as bm
import gestionInterface.buildPanel as bp

def buildInterface():
    
    #définition du cadre de l'interface utilisateur
    fenetre = ctk.CTk()
    fenetre.geometry("1100x750+0+0")
    fenetre.title("Analyseur de pseudo code")
    
    #création du menu
    bm.buildMenu(fenetre)

    #Editeur de saisie du pseudo code
    
    bp.buildPanel(fenetre)

    #Les boutons



    fenetre.mainloop()