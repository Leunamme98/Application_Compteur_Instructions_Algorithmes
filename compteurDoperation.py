"""
Module: compteurDoperation

Description
Ce module fournie une fonctionnalité pour compter le nombre d'operation dans un code 

Fonctions:
lire_contenu_fichier(chemin_fichier:str) str: Fonction permettant de lire dans le fichier de stockage du résulat de comptage
compteurOperation(code: str) bool, int or str: Fonction permettant de compter le nomre d'operation dans un code
"""
#importation des modules crées
import traitementDuCode as tc
import analyseurPseudoCode as apc


def lire_contenu_fichier(chemin_fichier: str) -> int:
    """
    La fonction permet de lire le contenu d'un fichier et renvoie le resulat sous forme d'entier
    @param: chemin relatif du fichier
    @return: le nombre lu dans le fichier
    
    """

    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
    return int(contenu)



def compteurOperation(code: str):
    """
    La fonction permet de compter le nombre d'opérations dans le code
    @param: le code ecrite en python
    @return: le nombre d'operation
    """
    reponse , message = apc.analyser_et_executer(code)
    code = tc.traitementDuCode(code)
    code_pour_ecrire = """
def ecrire_dans_fichier(chemin_fichier, donnee):
    with open(chemin_fichier, 'w') as fichier:
        fichier.write(str(donnee))
\n"""

    fin ="""
# Exemple d'utilisation
chemin = "nombreOperation.txt"
ecrire_dans_fichier(chemin, operation)\n
"""

    
    if reponse:
        code = code_pour_ecrire+"operation = 0\n"+code+fin
        try:
            exec(code)

        # recuperation du nombre d'operation
            chemin = "nombreOperation.txt"
            contenu = lire_contenu_fichier(chemin)
        
        
            return reponse, contenu
        except IndentationError as err_message:
            message = f"Erreur d'indentation : {err_message}"
            
            return False, message

    else :

        return reponse, message




