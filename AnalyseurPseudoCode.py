"""
Module: analyseur_pseudocode

Description:
Ce module fournit des fonctions pour analyser le pseudo-code et extraire les instructions.
Il permet de gérer les affectations, les opérations et les boucles, et d'évaluer les conditions.

Fonctions:
- est_affectation(ligne: str) -> Tuple[bool, Tuple[str, str, str]]: Vérifie si une ligne est une affectation.
- est_operation(ligne: str) -> Tuple[bool, Tuple[str, str, str, str]]: Vérifie si une ligne est une opération.
- analyser_boucle_while(ligne: str) -> bool: Vérifie si une ligne est une boucle while.
- extraire_conditions_boucle_while(ligne: str) -> Tuple[str, str, str]: Extrait la condition d'une boucle while.
- evaluer_condition(var1: str, oprel: str, var2: str) -> bool: Évalue une condition de boucle.
- effectuer_affectation(var1: str, var2: str, variables: dict) -> None: Effectue une affectation.
- effectuer_operation(var1: str, var2: str, operateur: str, var3: str, variables: dict) -> None: Effectue une opération.
"""

import re
from typing import Tuple, Dict


def est_affectation(ligne: str) -> Tuple[bool, Tuple[str, str]]:
    """
    Vérifie si la ligne spécifiée correspond à une affectation dans le pseudo-code.

    :param ligne: La ligne à analyser
    :return: Un tuple contenant un booléen indiquant si c'est une affectation et les variables impliquées
    """
    match = re.match(r'^\s*(\w+)\s*=\s*(\w+)\s*$', ligne)
    if match:
        return True, (match.group(1), match.group(2))
    return False, (None, None)


def est_operation(ligne: str) -> Tuple[bool, Tuple[str, str, str, str]]:
    """
    Vérifie si la ligne spécifiée correspond à une opération dans le pseudo-code.

    :param ligne: La ligne à analyser
    :return: Un tuple contenant un booléen indiquant si c'est une opération et les variables et opérateur impliqués
    """
    match = re.match(r'^\s*(\w+)\s*=\s*(\w+)\s*([\+\-\*/])\s*(\w+)\s*$', ligne)
    if match:
        return True, (match.group(1), match.group(2), match.group(3), match.group(4))
    return False, (None, None, None, None)


def est_boucle_while(ligne: str) -> bool:
    """
    Vérifie si la ligne spécifiée correspond à une boucle While dans le pseudo-code.

    :param ligne: La ligne à analyser
    :return: True si la ligne représente une boucle While, False sinon
    """
    ligne = ligne.strip().lower()
    return ligne.startswith("while")


def extraire_conditions_boucle_while(ligne: str) -> Tuple[str, str, str]:
    """
    Extrait la condition d'une boucle 'while' à partir d'une ligne de pseudo-code.

    :param ligne: La ligne de pseudo-code contenant la boucle 'while'.
    :return: Un tuple contenant les deux variables et l'opérateur de relation de la condition.
    :raises ValueError: Si la ligne ne contient pas une condition de boucle 'while' valide.
    """
    debut_condition = ligne.find("(")
    fin_condition = ligne.rfind(")")

    if debut_condition == -1 or fin_condition == -1 or fin_condition < debut_condition:
        raise ValueError("La ligne ne contient pas une boucle 'while' valide.")

    condition_str = ligne[debut_condition + 1: fin_condition].strip()
    op_rels = ["<=", ">=", "=", "<", ">"]
    for op_rel in op_rels:
        if op_rel in condition_str:
            var1, oprel, var2 = condition_str.partition(op_rel)
            return var1.strip(), oprel.strip(), var2.strip()

    raise ValueError(
        "La condition de la boucle 'while' ne contient pas un opérateur de relation valide.")


def evaluer_condition(var1: str, oprel: str, var2: str, variables: Dict[str, int]) -> bool:
    """
    Évalue une condition de boucle while.

    :param var1: La première variable ou valeur
    :param oprel: L'opérateur de relation
    :param var2: La deuxième variable ou valeur
    :param variables: Un dictionnaire des variables avec leurs valeurs
    :return: Le résultat de l'évaluation de la condition
    """
    val1 = variables.get(var1, 0)
    val2 = variables.get(var2, 0)
    if oprel == "<=":
        return val1 <= val2
    elif oprel == ">=":
        return val1 >= val2
    elif oprel == "=":
        return val1 == val2
    elif oprel == "<":
        return val1 < val2
    elif oprel == ">":
        return val1 > val2
    else:
        raise ValueError(f"Opérateur de relation non reconnu: {oprel}")


def effectuer_affectation(var1: str, var2: str, variables: Dict[str, int]) -> None:
    """
    Effectue une affectation de var2 à var1.

    :param var1: La variable à laquelle assigner la valeur
    :param var2: La variable ou la valeur à assigner
    :param variables: Un dictionnaire des variables avec leurs valeurs
    """
    variables[var1] = variables.get(var2, 0)


def effectuer_operation(var1: str, var2: str, operateur: str, var3: str, variables: Dict[str, int]) -> None:
    """
    Effectue une opération arithmétique et stocke le résultat dans var1.

    :param var1: La variable où stocker le résultat
    :param var2: La première variable ou valeur de l'opération
    :param operateur: L'opérateur arithmétique (+, -, *, /)
    :param var3: La deuxième variable ou valeur de l'opération
    :param variables: Un dictionnaire des variables avec leurs valeurs
    """
    val2 = variables.get(var2, 0)
    val3 = variables.get(var3, 0)
    if operateur == "+":
        variables[var1] = val2 + val3
    elif operateur == "-":
        variables[var1] = val2 - val3
    elif operateur == "*":
        variables[var1] = val2 * val3
    elif operateur == "/":
        variables[var1] = val2 // val3  # Utilisation de la division entière
    else:
        raise ValueError(f"Opérateur arithmétique non reconnu: {operateur}")
