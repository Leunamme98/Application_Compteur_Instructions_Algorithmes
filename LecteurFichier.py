"""
Module: LecteurFichier

Description:
Ce module fournit des fonctions pour lire le contenu de fichiers texte (.txt), PDF (.pdf) et Word (.docx)
et retourner une liste de lignes. Il gère les exceptions courantes telles que les fichiers non trouvés
et les erreurs d'entrée/sortie.

Fonctions:
- ouvrirFichierTxt(cheminFichier: str) -> TextIO: Ouvre un fichier texte en mode lecture.
- lireLignesTxt(fichier: TextIO) -> List[str]: Lit les lignes d'un fichier texte ouvert.
- lireFichierPdf(cheminFichier: str) -> List[str]: Lit le contenu d'un fichier PDF.
- lireFichierDocx(cheminFichier: str) -> List[str]: Lit le contenu d'un fichier Word (.docx).
- lireFichier(cheminFichier: str) -> Tuple[List[str], bool]: Lit le contenu d'un fichier texte, PDF ou Word
  et retourne une liste de lignes ainsi qu'un indicateur de succès.

Exceptions:
- FileNotFoundError: Levée si le fichier spécifié est introuvable.
- IOError: Levée en cas d'autres erreurs d'entrée/sortie.
"""

# Import des modules nécessaires pour le traitement des fichiers texte, PDF et Word
from typing import List, TextIO, Tuple  # Module pour les annotations de type
import os  # Module pour la gestion des chemins de fichiers
import PyPDF2  # Module pour la manipulation des fichiers PDF
from docx import Document  # Module pour la manipulation des fichiers Word
from pathlib import Path  # Module pour la manipulation des chemins de fichiers
import chardet


def ouvrirFichierTxt(cheminFichier: str) -> TextIO:
    """
    Ouvre un fichier texte en mode lecture avec détection automatique de l'encodage.

    :param cheminFichier: Chemin du fichier à lire
    :return: Objet fichier ouvert
    :raises FileNotFoundError: Si le fichier n'est pas trouvé
    :raises IOError: Si une erreur d'E/S se produit lors de l'ouverture du fichier
    """
    try:
        # Lire le contenu du fichier en mode binaire
        with open(cheminFichier, 'rb') as fichier:
            contenu_bytes = fichier.read()
        
        # Détecter l'encodage probable
        resultat = chardet.detect(contenu_bytes)
        encodage = resultat['encoding']

        # Ouvrir le fichier avec l'encodage détecté
        fichier_texte = open(cheminFichier, 'r', encoding=encodage)
        return fichier_texte

    except FileNotFoundError:
        raise FileNotFoundError("Le fichier spécifié est introuvable.")
    except IOError as e:
        raise IOError(
            f"Une erreur s'est produite lors de l'ouverture du fichier : {e}")


def lireLignesTxt(fichier: TextIO) -> List[str]:
    """
    Lit les lignes d'un fichier texte ouvert.

    :param fichier: Objet fichier ouvert
    :return: Liste de lignes du fichier
    :raises IOError: Si une erreur d'E/S se produit lors de la lecture du fichier
    """
    try:
        lignes = fichier.readlines()
        return lignes
    except IOError as e:
        raise IOError(
            f"Une erreur s'est produite lors de la lecture du fichier : {e}")


def lireFichierPdf(cheminFichier: str) -> List[str]:
    """
    Lit le contenu d'un fichier PDF.

    :param cheminFichier: Chemin du fichier PDF à lire
    :return: Liste de lignes du fichier PDF
    :raises FileNotFoundError: Si le fichier n'est pas trouvé
    :raises IOError: Si une erreur d'E/S se produit lors de la lecture du fichier
    """
    try:
        with open(cheminFichier, 'rb') as fichier:
            lecteurPdf = PyPDF2.PdfReader(fichier)
            lignes = []
            for page in lecteurPdf.pages:
                lignes.append(page.extract_text())
        return lignes
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier spécifié est introuvable.")
    except IOError as e:
        raise IOError(
            f"Une erreur s'est produite lors de la lecture du fichier : {e}")


def lireFichierDocx(cheminFichier: str) -> List[str]:
    """
    Lit le contenu d'un fichier Word (.docx).

    :param cheminFichier: Chemin du fichier Word à lire
    :return: Liste de lignes du fichier Word
    :raises FileNotFoundError: Si le fichier n'est pas trouvé
    :raises IOError: Si une erreur d'E/S se produit lors de la lecture du fichier
    """
    try:
        doc = Document(cheminFichier)
        lignes = [paragraphe.text for paragraphe in doc.paragraphs]
        return lignes
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier spécifié est introuvable.")
    except IOError as e:
        raise IOError(
            f"Une erreur s'est produite lors de la lecture du fichier : {e}")


def lireFichier(cheminFichier: str) -> Tuple[List[str], bool]:
    """
    Lit le contenu d'un fichier texte, PDF ou Word et retourne une liste de lignes ainsi qu'un indicateur de succès.

    :param cheminFichier: Chemin du fichier à lire
    :return: Tuple contenant la liste de lignes du fichier et un booléen indiquant le succès de la lecture
    """
    chemin = Path(cheminFichier)
    extension = chemin.suffix.lower()
    success = True  # Par défaut, considérer que la lecture est un succès
    try:
        if extension == '.txt':
            with ouvrirFichierTxt(cheminFichier) as fichier:
                lignes = lireLignesTxt(fichier)
        elif extension == '.pdf':
            lignes = lireFichierPdf(cheminFichier)
        elif extension == '.docx':
            lignes = lireFichierDocx(cheminFichier)
        else:
            raise ValueError(
                "Format de fichier non supporté : doit être .txt, .pdf ou .docx")
    except FileNotFoundError:
        success = False
        lignes = []  # Retourner une liste vide si le fichier est introuvable
    except IOError:
        success = False
        lignes = []  # Retourner une liste vide en cas d'erreur d'E/S
    except Exception:
        success = False
        lignes = []  # Retourner une liste vide pour toute autre exception
    return lignes, success
