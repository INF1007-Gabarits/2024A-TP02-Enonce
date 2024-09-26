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
    
# print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici


csv_nvCollection = open("nouvelle_collection.csv", newline='')

nvCollection = csv.reader(csv_nvCollection)

for c in nvCollection:
    if c[-1] in bibliotheque:
        print(f"Le livre {c[-1]} ---- {c[0]} par {c[-3]} ---- est déjà présent dans la bibliothèque")
    else:
        bibliotheque.update({c[-1] : c[:-1]})
        print(f"Le livre {c[-1]} ---- {c[0]} par {c[-3]} ---- a été ajouté avec succès")
        


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
toRemove = list()
toAdd = dict()

for b in bibliotheque:
    if "Shakespeare" in bibliotheque[b][1] :
        cote = "W"+b
        toAdd.update({cote : bibliotheque[b]})
        toRemove.append(b)
        
for i in toRemove:
    bibliotheque.pop(i)
    
for i in toAdd:
    bibliotheque.update({i : toAdd[i]})


print(f" \n Bibliotheque avec modifications de cote : {bibliotheque} \n")




########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






