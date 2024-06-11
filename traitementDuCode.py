"""
Module: traitementDuCode

Description:
Ce module fournit une fonctionnalité pour traiter le code source Python en insérant l'instruction `operation += 1` après chaque instruction.

Fonction:
- traitementDuCode(code: str) -> str: 
    Insère l'instruction `operation += 1` après chaque instruction dans le code Python donné.

"""


def traitementDuCode(code: str) -> str:
    """
    Insère l'instruction `operation += 1` après chaque instruction dans le code Python donné.

    Args:
        code (str): Le code source Python à traiter.

    Returns:
        str: Le code source modifié avec l'instruction d'incrément ajoutée après chaque instruction.
    """

    code = code.strip()
    code_liste = code.split("\n")

    # suppression des commentaires
    new_code = []
    for i in code_liste:
        a = i.strip()

        if not (a == "" or a[0] == '#'):
            new_code.append(i)

    # Ajout du compteur d'operation
    compteur = "operation+=1"
    code_compteur = []

    for i in range(len(new_code)):

        ligne = new_code[i]

        # Ajout après les lignes qui ne contient pas de boucle while, for de if, elif, else
        if not (('while ' in ligne) or ('for ' in ligne) or ('if ' in ligne) or ('elif ' in ligne) or ('else ' in ligne) or
                ('with ' in ligne) or ('def ' in ligne) or ('match ' in ligne) or ('case ' in ligne)):

            # ajout des ligne sans insctruction (boucle)
            code_compteur.append(ligne)

            # Détermination de l'intentation
            nbre_espace = ligne.find(ligne.strip()[0])
            espace = " "*nbre_espace

            compteur_reel = espace+compteur  # Configuration réel du compteur à ajouter

            code_compteur.append(compteur_reel)  # Ajout du conpteur

        else:

            code_compteur.append(ligne)

    # reformer le code
    code_traiter = "\n".join(code_compteur)

    code_final = code_traiter

    return code_final
