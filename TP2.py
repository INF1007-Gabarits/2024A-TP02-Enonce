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
bibliothèque = dict()
for row in c :
    titre = row[0]
    auteur = row[1]
    date = row[2]
    cote_rangement=row[3]
    bibliothèque[cote_rangement] = [titre,auteur,date] 
print(f' \n Bibliotheque initiale : {bibliothèque} \n')



#for row in c :
    #titre = row[0]   
    #print(row)     

#bibliothèque = dict()
#cote = "allo"
#cote_2 = "bonsoir"
#bibliothèque[cote_rangement] = [titre,auteur,date]
#bibliothèque[cote_2] = 2



#print(f' \n Bibliotheque initiale : {bibliothèque} \n')




# read whatever you want from the reader object
# print it or use it any way you like


# save and close the file
csvfile.close()





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






