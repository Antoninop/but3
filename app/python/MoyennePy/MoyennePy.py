# -*- coding: utf-8 -*-

with open("../../sortiez.txt", "r") as fichier:
    lignes = fichier.readlines()

coefs_texte = lignes[0].split(';')
notes_texte = lignes[1].split(';')


for ligne in lignes[1:]:
    # Extraire les notes de chaque ligne
    notes_texte = ligne.split(';')
    
    # Extraire le nom et prénom de l'élève
    nom_prenom = notes_texte[0].split(',')
    nom = notes_texte[0]
    prenom = notes_texte[1]

    # Calculer la moyenne pondérée
    # Convertir coef en float 
    coefs = [float(coef.replace(',', '.')) for coef in coefs_texte[0:]]
    notes = [float(notes.replace(',', '.')) for notes in notes_texte[2:]]
    somme_produits = sum(coef * note for coef, note in zip(coefs, notes))
    somme_coefs = sum(coefs)
    moyenne_ponderee = somme_produits / somme_coefs

    print(nom,prenom,moyenne_ponderee)
