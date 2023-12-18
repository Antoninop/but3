# -*- coding: utf-8 -*-
from unidecode import unidecode
from colorama import init, Fore

# Initialiser colorama
init()

def calculer_moyenne_ponderee(notes, coefs):
    if len(notes) != len(coefs):
        raise ValueError("Le nombre de notes ne correspond pas au nombre de coefficients.")

    somme_notes_ponderees = sum(note * coef for note, coef in zip(notes, coefs))
    somme_coefs = sum(coefs)
    moyenne_ponderee = somme_notes_ponderees / somme_coefs if somme_coefs != 0 else 0

    return moyenne_ponderee

def lire_fichier_et_calculer_moyennes(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()

    # Extraction des coefficients depuis la première ligne
    coefs = list(map(float, lignes[0].strip().split(';')))

    resultats = []

    # Lecture des lignes d'étudiants et calcul des moyennes
    for ligne in lignes[1:]:
        colonnes = ligne.strip().split(';')
        prenom, nom = map(unidecode, colonnes[:2])  # Translittération
        notes = list(map(float, colonnes[2:]))
        
        moyenne_ponderee = calculer_moyenne_ponderee(notes, coefs)
        resultats.append((prenom, nom, moyenne_ponderee))

    return resultats

# Exemple d'utilisation
chemin_fichier_txt = "chemin/vers/votre/fichier.txt"
resultats = lire_fichier_et_calculer_moyennes(chemin_fichier_txt)

# Affichage des résultats avec colorama
for prenom, nom, moyenne in resultats:
    print(f"{Fore.CYAN}{prenom} {nom} - Moyenne pondérée : {moyenne:.2f}{Fore.RESET}")
