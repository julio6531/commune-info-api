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
```py
Explication sur l’exécution du script
```
```py
Il va falloir créer un fichier .bat et dedans on devra renseigner le chemin ou ce trouver python et ou ce trouve le script:
```
![1](https://user-images.githubusercontent.com/92336484/138939133-f17785ff-f850-439e-926e-a62e29946ef1.png)
```py
On va aller sur planificateur de tâche, puis créer une nouvelle tâche
Il faudra donner un nom a la tâche que l’on souhaite
```
```py
Puis on va aller sur déclencheur, en bas à nouveau, renseigner ce que l’on souhaite mettre comme un fois etc…, le heure de démarrage,  on mettra le repetatage que l’on souhaite
```
![2](https://user-images.githubusercontent.com/92336484/138940043-9b75aebe-3c26-4a63-becc-b184c184231a.png)
```py
Aller dans action, puis nouveau, programme/script renseigner le chemin de PowerShell, dans ajouter un arguments renseigner le chemin du script exemple getcommunen.bat, dans commencer renseigner le chemin dans lequel ce trouve script et en terminant par \ 
```
![3](https://user-images.githubusercontent.com/92336484/138940274-24e7e1c4-6c38-4ba0-91cf-fd4f69845ab1.png)
![4](https://user-images.githubusercontent.com/92336484/138940402-c42ee428-2440-4807-9df7-07e3a6e4e003.png)
```py
Dans les conditions il faudra décochez ne démarrer la tâche arrêtera l’ordinateur passe en alimentation par batterie que si l’ordinateur est relié au secteur.
```
![5](https://user-images.githubusercontent.com/92336484/138940968-5025ff40-0e05-4f25-ac34-9faab6f02e21.png)

