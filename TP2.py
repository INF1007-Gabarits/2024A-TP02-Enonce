"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  11
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

# open an existing file for reading -
csvfile = open('C:\\Users\\Margot-Loane\\Desktop\\A24\\INF1007\\2024A-TP02-Enonce\\collection_bibliotheque.csv', newline='')
c = csv.reader(csvfile)

# make a new variable - c - for Python's CSV reader object -
#def cote() :
    #for row in range(c[1], c[462]) : 
            # cr = row[-4]
    #return cr
bibliothèque = {}
c = csv.DictReader(csvfile)
for row in c :
    titre = row["titre"]
    auteur = row["auteur"]
    date = row["date_publication"]
    cote_rangement=row["cote_rangement"]
    bibliothèque[cote_rangement] = [titre,auteur,date] 
#print(f' \n Bibliotheque initiale : {bibliothèque} \n')
#cote = str(input())
#print(bibliothèque[cote])
csvfile.close()





########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile = open ("collection_bibliotheque.csv")
csvfile_1 = open("nouvelle_collection.csv")

c = csv.DictReader(csvfile)
d = csv.DictReader(csvfile_1)

new_bibliothèque = {}

for row in d : 
    new_cote = row["cote_rangement"]
    if new_cote != cote_rangement : 
        new_titre = row["titre"]
        new_auteur = row["auteur"]
        new_date = row["date_publication"]
        new_bibliothèque[new_cote]= [new_titre, new_auteur, new_date]
        print(f"Le livre {new_cote} ---- {new_titre} par {new_auteur} ---- a été ajouté avec succès")
    else : 
        print(f"Le livre {new_cote} ---- {new_titre} par {new_auteur} ---- est déjà présent dans la bibliothèque")
bibliothèque.update(new_bibliothèque)
new_cote = cote_rangement

print(f' \n Bibliotheque totale : {bibliothèque} \n')










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






