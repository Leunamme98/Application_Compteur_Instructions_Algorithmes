
#importation des modules crées
import traitementDuCode as tc
import ast

def detecterBoucleInfinie(code):
    """
    Détecte les boucles infinies potentielles dans un code Python donné.

    Args:
        code (str): Le code source Python à analyser.

    Returns:
        bool: True si une boucle infinie potentielle est détectée, False sinon.
    """
    # Analyser le code en un AST (Arbre Syntaxique Abstrait)
    arbre = ast.parse(code)

    class DetecteurBoucleInfinie(ast.NodeVisitor):
        def __init__(self):
            self.boucle_infinie_trouvee = False

        def visit_While(self, node):
            # Visiter les nœuds de condition
            self.generic_visit(node)
            
            # Vérifier si la condition est une constante True
            if isinstance(node.test, ast.Constant) and node.test.value == True:
        
                self.boucle_infinie_trouvee = True

            # Autres vérifications pour les conditions simples comme 'while 1:'
            if isinstance(node.test, ast.Constant) and node.test.value == 1:
                
                self.boucle_infinie_trouvee = True

        def visit_For(self, node):
            # Vérifier si le nombre d'itérations est potentiellement infini
            self.generic_visit(node)
            # La détection de boucles for infinies est plus complexe
            # car cela dépend de la séquence sur laquelle la boucle itère.
            # Par exemple, une boucle sur une séquence infinie comme itertools.count() pourrait être infinie,
            # mais ce type de détection nécessiterait une analyse plus dynamique.

    # Créer une instance du détecteur
    detecteur = DetecteurBoucleInfinie()
    detecteur.visit(arbre)

    return detecteur.boucle_infinie_trouvee



def lire_contenu_fichier(chemin_fichier: str) -> int:
    """
    La fonction permet de lire le contenu d'un fichier et renvoie le resulat sous forme d'entier
    @param: chemin relatif du fichier
    @return: le nombre lu dans le fichier
    
    """

    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
    return int(contenu)



def compteurOperation(code: str)->int:
    """
    La fonction permet de compter le nombre d'opérations dans le code
    @param: le code ecrite en python
    @return: le nombre d'operation
    """
    
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


    code = code_pour_ecrire+"operation = 0\n"+code+fin
    exec(code)

    # recuperation du nombre d'operation
    chemin = "nombreOperation.txt"
    contenu = lire_contenu_fichier(chemin)
    
    return contenu



code ="""
# Boucle while
i = 0
while i < 5:
    print(f"Boucle while, itération {i}")
    i += 1

# Boucle for
for j in range(3):
    print(f"Boucle for, itération {j}")

"""   


operation = compteurOperation(code)
print(operation)


