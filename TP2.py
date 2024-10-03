"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 04
Numéro d'équipe :  YY
Noms et matricules : Soeuchelle Michel (2324529), Lily-Rose Arès (2377089)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

import csv 

# open an existing csv file
csvfile = open("collection_bibliotheque.csv", newline = "")
collection_bliblio = csv.reader(csvfile)


# TODO : Écrire votre code ici
# code de rangement permet de retrouver livre 

# faire dict avec dict -> biblotheque
# {R008: {titre: harry pottter, auteur: JK. Rowling , pub: 56/12/6}}


bibliotheque = {}
for row in collection_bliblio:
    # Chaque élément dans la liste complète est une liste
    # on va prendre le 3 ème indice de la liste pour créer 
    # un dict 
    cote = row[3]
    bibliotheque[cote] = {"titre": row[0], "auteur": row[1], "date_publication": row[2]}

print(f'\n Bibliotheque initiale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
# open an existing csv file
csvfile2 = open("nouvelle_collection.csv", newline = "")
nouvelle = csv.reader(csvfile2)


for row in nouvelle:
    cote = row[3]
    if cote in bibliotheque:
        print(f"Le livre {cote} ---- {row[0]} par {row[1]} ---- est déjà présent dans la bibliothèque")
    else:
        bibliotheque[cote] = {"titre": row[0], "auteur": row[1], "date_publication": row[2]}
        print(f"Le livre {cote} ---- {row[0]} par {row[1]} ---- a été ajouté avec succès")


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
# remplacement de la collection de Shakespeare par WS
# a partir du dict bibliotheque: modifier les cotes 
# cote de range débute par S

new_list = []

# Pour avoir accès à la nouvelle clé
# dict.key -> key
# dict.value -> value

# créer un dict avec les clés qui ont 


for cote in bibliotheque:
    if bibliotheque[cote]["auteur"] == "William Shakespeare":
        new_list.append(cote)

print(new_list)


# liste des côtes avec WS au lieu de S
list_ws = []
# besoin de remplacer le S dans la cote de rangement par WS
# faire une copie du dict sans ceux qui ont comme cote de rangement les éléments dans la liste
# ensuite, mettre les même valeur qui sont dans la cote originale dans la copie
for i in range(0, len(new_list)):
    str_or = new_list[i]
    new_str = "W" + str_or
    list_ws.append(new_str)

#print(list_ws)

# nouveau dict avec les nouvelles cotes de forme WS
new_dict ={}
for anc_cote in bibliotheque:
    if anc_cote in new_list:
        for i in range(0, len(list_ws)):
            if anc_cote in new_list[i]:
                new_dict[list_ws[i]] = bibliotheque[anc_cote] 

# merge les deux dictionnaires
bibliotheque.update(new_dict)


# enlever les anciennes cotes si elles sont présentes dans new_list
for cote in new_list:
    bibliotheque.pop(cote)

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

# date d'emprunt dans le fichier 
# ajouter une clé emprunt pour suivre état du livre 
    # si présent dans la bibliothèque: disponible
    # si absent: emprunté

# lire le fichier emprunts.csv
# if the book is in there, clé emprunté
# else: book not emprunté

emprunts_csv = open("emprunts.csv", newline = "")
emprunts_file = csv.reader(emprunts_csv)

# faire un dictionnaire des emprunts
emprunts_dic = {}
    # a les bonnes dates associées à chacun des index 

for row in emprunts_file:
    cote = row[0]
    emprunts_dic[cote] = row[1]

for cle in bibliotheque:
    if cle in emprunts_dic:
        bibliotheque[cle]["emprunts"] = "emprunté"
        bibliotheque[cle]["date_emprunt"] = emprunts_dic[cle]
        
    else:
        bibliotheque[cle]["emprunts"] = "disponible"
        bibliotheque[cle]["date_emprunt"] = None


print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici
# ajouter une clé frais de retard 

# module Datetime
from datetime import datetime 
from datetime import date

# les dates contenues dans les livres empruntés sont déjà sous la forme de str
date_fin = datetime.today()


# date intiale d'emprunt: celle qui se trouve dans le dict
# si plus d'un an de retard, livre considéré perdu 

emprunts_dic_update = {}


# calcul des frais de retard pour chacun des livres
# mettre les livres avec des frais de retard dans un nouveau dict
# besoin de différence de moins ou égal à 30 jours pour ne pas avoir de frais de retardà

# enlever la première rangée de bibliothèque avec les titres 
first = []
for cote in bibliotheque:
    if cote == "cote_rangement":
        first.append(cote)


for cote in first:
    bibliotheque.pop(cote)
    emprunts_dic_update

lst_date = []
for cote in bibliotheque:
    if bibliotheque[cote]["date_emprunt"] != None:
        emprunts_dic_update[cote] = bibliotheque[cote]["date_emprunt"].replace("-", "/")
        lst_date.append(emprunts_dic_update[cote])

retard_list = []
i = 0
for _ in range(i, len(lst_date)):
# use the strptime function from datetime
    anc_date = datetime.strptime(lst_date[i], "%Y/%m/%d")


    difference = (date_fin - anc_date)
    
    retard_list.append(difference.days)
    
    i += 1
print(retard_list)

# frais dictionnaire liste
frais_liste = []
# calculer la quantité de frais à mettre selon les jours de retard 
a = 0 
for i in range(0, len(retard_list)):
    if retard_list[a] <= 30:
        frais_liste.append(0)
        a += 1
    elif retard_list[a] > 30 and retard_list[a] < 365:
        frais = retard_list[a] * 2 
        if frais > 100:
            frais_liste.append(100)
            a += 1 
        else:
            frais_liste.append(frais)
            a += 1 
    else:
        frais_liste.append("perdu")
        a += 1 


# besoin d'append les cotes de rangements dans une liste
cote_liste = []
for ele in emprunts_dic_update:
    cote_liste.append(ele)
print((cote_liste))
print(frais_liste)

dict_frais = {}
# avec la liste des cotes et la liste des frais de retard, on va créer des cotes 
i = 0
j = 0 
for _ in range(i, len(cote_liste)):
    for _ in range(j, len(frais_liste)):
        dict_frais[cote_liste[i]] = frais_liste[j]
        i += 1 
        j += 1




# création des clés pour les frais pour les mettre dans le dict emprunts
for cle in bibliotheque:
    if cle in dict_frais:
        if dict_frais[cle] != "perdu":
            bibliotheque[cle]["frais_retard"] = dict_frais[cle]
        else:
            bibliotheque[cle]["livres_perdus"] = dict_frais[cle]


print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')