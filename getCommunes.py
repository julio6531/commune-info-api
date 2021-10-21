'''
Ce programme a pour but de recupèrer des information sur le site du gouvernement pour la commune du 64(pyrenees-atlantiques)

nom de l'auteur: Julien LAULHE
date: 20/10/2021
version: 1
'''

# Importation des librairies python fournit par Pyhton nécessaire au script suivant
import requests
import csv
import json

# Récupération des données sur les communes du 64
response = requests.get("https://geo.api.gouv.fr/departements/64/communes")
print(response)
# La réponse est envoyée au format json donc nous devons la rendre lisible avec la méthode json()
communes = response.json()
print(communes)
# On crée des tableaux qui vont stocké les informations propres à chaque ligne (nom, ..)
villes = []
codes = []
codeDepartments = []
codeRegions = []
codesPostaux = []
populations = []

# On boucles les communes reçues au format json et pour chaque ligne on ajoute dans le tableau respectif
for commune in communes:
    villes.append(commune["nom"])
    codes.append(commune["code"])
    codeDepartments.append(commune["codeDepartement"])
    codeRegions.append(commune["codeRegion"])
    codesPostaux.append(commune["codesPostaux"])
    populations.append(commune["population"])

en_tete = ["ville", "code", "codeDepartement", "codeRegion", "codesPostaux", "Population" ]

with open('communes.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')
    writer.writerow(en_tete)
    for ville, code, codeDepartment, codeRegion, codePostal, population in zip(villes, codes, codeDepartments, codeRegions, codesPostaux, populations  ):
        writer.writerow([ville, code, codeDepartment, codeRegion,codePostal[0], population])



    