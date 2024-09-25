"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01  
Numéro d'équipe : 01
Noms et matricules : Gaetan Lohier (Matricule1), Nom2 (Matricule2)
"""
import csv

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
csv_collection = open("collection_bibliotheque.csv", newline='')

collection = csv.reader(csv_collection)

bibliotheque  = dict()

for c in collection:
    bibliotheque[c[-1]] = c[:-1]
    
print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






