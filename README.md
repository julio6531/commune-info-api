# commune-info-api
Ce programme a pour but de récupérer des informations sur le site du gouvernement pour le département du 64(Pyrénées-Atlantiques)

Nom de l’auteur : Julien LAULHE
Date : 20/10/2021
Version : 1

Il va falloir mettre import requests et télécharger requests : 
C’est un dictionnaire ou un modèle qui permettra d’envoyer des requêtes http et https
```py
import requests
```

Il va falloir mettre  Importer csv et télécharger csv :
C’est un module ou un dictionnaire qui a des fonctionnalités pour le traitement 
```py
import csv
```
Il va falloir mettre Import json et télécharger json :
 C’est dictionnaire ou module qui fournit des méthodes pour traiter du json
```py
import json
```
La ligne avec la variable response = requests. Get(‘’), qui ira récupérer des informations sur le site concerné et de le stocké dans response.
```py
response = requests.get("https://geo.api.gouv.fr/departements/64/communes")
```
La ligne avec la variable communes = reponse.json(), va nous permettre de mettre les informations au format json et rendre le texte lisible.
```py
communes = response.json()
```
La ligne avec la variables ville etc……
Ces variables vont créer des tableaux pour stocker les informations récupérées sur le site web cité plus haut et ceci pour chaque variable explicitéee (nom……).
```py
villes = []
codes = []
codeDepartments = []
codeRegions = []
codesPostaux = []
populations = []
```
La ligne for commune in communes :
C’est une boucle qui va permettre de mettre les informations reçues et de les ajoutées ligne par ligne au tableau respectif.
```py
for commune in communes:
    villes.append(commune["nom"])
    codes.append(commune["code"])
    codeDepartments.append(commune["codeDepartement"])
    codeRegions.append(commune["codeRegion"])
    codesPostaux.append(commune["codesPostaux"])
    populations.append(commune["population"])
```    
La ligne with open, write, write. writerow et for ville…. : 
La première ligne va créer un fichier en csv, la seconde ligne va paramètre la méthode d’écriture dans le fichier csv, la ligne trois va écrire les en tête  ville : []…… vu plus haut , puis la dernière ligne va boucler les tableaux créer auparavant et les écrire ligne par ligne dans le fichier csv
```py
en_tete = ["ville", "code", "codeDepartement", "codeRegion", "codesPostaux", "Population" ]
with open('communes.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')
    writer.writerow(en_tete)
    for ville, code, codeDepartment, codeRegion, codePostal, population in zip(villes, codes, codeDepartments, codeRegions, codesPostaux, populations  ):
        writer.writerow([ville, code, codeDepartment, codeRegion,codePostal[0], population])
```



