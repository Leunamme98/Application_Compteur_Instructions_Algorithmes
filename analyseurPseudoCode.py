"""
Module: AnalyseurPseudoCode

Description:
Ce module fournit une fonctionnalité pour analyser et exécuter du pseudo-code en Python, et détecter les erreurs.

Fonctions:
- analyser_et_executer(code: str) -> Tuple[bool, Union[str, None]]: Analyse et exécute le pseudo-code,
  renvoyant un booléen indiquant si l'exécution a réussi et un message d'erreur en cas d'échec.
"""

from typing import Tuple, Union


def analyser_et_executer(code: str) -> Tuple[bool, Union[str, None]]:
    """
    Analyse et exécute le pseudo-code en Python, et détecte les erreurs.

    :param code: Chaîne de caractères représentant le pseudo-code à analyser et exécuter
    :return: Un tuple contenant un booléen indiquant si l'exécution a réussi et un message d'erreur en cas d'échec
    """
    try:
        # Exécute le code une fois pour détecter les erreurs
        exec(code)
        # Si l'exécution réussit sans lever d'exception, renvoie True sans message d'erreur
        return True, ""
    except SyntaxError as syntax_err:
        # Si une erreur de syntaxe est détectée, construit un message d'erreur clair
        error_message = f"Erreur de syntaxe : {
            syntax_err.msg} (ligne {syntax_err.lineno})"
        return False, error_message
    except TypeError as type_err:
        # Si une erreur de type est détectée, construit un message d'erreur clair
        error_message = f"Erreur de type : {type_err}"
        return False, error_message
    except ZeroDivisionError as div_err:
        # Si une division par zéro est détectée, construit un message d'erreur clair
        error_message = "Erreur : Division par zéro"
        return False, error_message
    except NameError as name_err:
        # Si une erreur de nom est détectée, construit un message d'erreur clair
        error_message = f"Erreur de nom : {name_err}"
        return False, error_message
    except IndexError as index_err:
        # Si une erreur d'index est détectée, construit un message d'erreur clair
        error_message = f"Erreur d'index : {index_err}"
        return False, error_message
    except KeyboardInterrupt as keybord_err:
        #Si il y a une boucle infinie stopper par le manipulation volontaire
        error_message = f"Erreur de boucle infinie: {keybord_err}"
        return False, error_message
    except Exception as err:
        # Si une autre erreur est détectée, renvoie False avec le message d'erreur générique
        return False, f"Erreur : {err}"
