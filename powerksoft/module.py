#--- coding:UTF-8 ---

from pickle import *

def searchUser(name, password = " "):
    if password != " ":
        with open('comptes.dat', 'rb') as fichier:
            while True:
                try:
                    chaine = load(fichier)
                    chaine = chaine.strip()
                    liste = chaine.split(" ")
                    if name == liste[0] and password == liste[1]:
                        return liste
                except EOFError:
                    return False
    else:
        with open('comptes.dat', 'rb') as fichier:
            while True:
                try:
                    chaine = load(fichier)
                    chaine = chaine.strip()
                    liste = chaine.split(" ")
                    if name == liste[0]:
                        return liste[0]
                except EOFError:
                    return False

def transactionList(user):
    listes = []
    listoftransaction = []
    with open('transactions.txt', 'r') as fichier:
        listes = fichier.readlines()
    for element in listes:
        element = element.strip()
        liste = element.split(" ")
        if liste[0] == user:
            chaine = " ".join(liste)
            listoftransaction.append(chaine)
    return listoftransaction
    
                
def depot(montant, user):
    listes = []
    with open('comptes.dat', 'rb') as fichier:
        while True:
            try:
                chaine = load(fichier)
                chaine = chaine.strip()
                liste = chaine.split(" ")
                listes.append(liste)    
            except EOFError:
                break
    i = 0
    for liste in listes:
        if liste[0] == user and 0 < montant:
            liste[2] = int(liste[2])
            liste[2] += montant
            with open('transactions.txt', 'a') as fic:
                chaine = user + " : " + "depot de " + str(montant) + "\n"
                fic.write(chaine)
            i = 1
    with open('comptes.dat', 'wb') as fichier:
        for liste in listes:
            chaine = str(liste[0]) + " " + str(liste[1]) + " " + str(liste[2]) + "\n"
            dump(chaine, fichier)
    if i == 1:
        return 'succes'
    else:
        return 'echec'
                    
def retrait(montant, user):
    listes = []
    with open('comptes.dat', 'rb') as fichier:
        while True:
            try:
                chaine = load(fichier)
                chaine = chaine.strip()
                liste = chaine.split(" ")
                listes.append(liste)    
            except EOFError:
                break
    i = 0
    for liste in listes:
        liste[2] = int(liste[2])
        if liste[0] == user and montant < liste[2] and 0 < montant:
            liste[2] -= montant
            with open('transactions.txt', 'a') as fic:
                chaine = user + " : " + "retrait de " + str(montant) + "\n"
                fic.write(chaine)
            i = 1
    with open('comptes.dat', 'wb') as fichier:
        for liste in listes:
            chaine = str(liste[0]) + " " + str(liste[1]) + " " + str(liste[2]) + "\n"
            dump(chaine, fichier)
    if i == 1:
        return 'succes'
    else:
        return 'echec'
    
def transfert(montant, user, destinataire):
    listes = []
    print(user, destinataire)
    if searchUser(destinataire) == False:
        return 'echec'
    with open('comptes.dat', 'rb') as fichier:
        while True:
            try:
                chaine = load(fichier)
                chaine = chaine.strip()
                liste = chaine.split(" ")
                listes.append(liste)    
            except EOFError:
                break
    i = 0
    for liste in listes:
        liste[2] = int(liste[2])
        if liste[0] == user and 0 < montant and montant < liste[2]:
            liste[2] -= montant
            with open('transactions.txt', 'a') as fic:
                chaine = user + " : " + "transfert de " + str(montant) + " a " + destinataire + "\n"
                fic.write(chaine)
            i += 1
    for liste in listes:
        liste[2] = int(liste[2])
        if liste[0] == destinataire:
            liste[2] += montant
            with open('transactions.txt', 'a') as fic:
                ch = destinataire + " : " + "reception de " + str(montant) + " venant de " + user + "\n"
                fic.write(ch)
            i += 1
    with open('comptes.dat', 'wb') as fichier:
        for liste in listes:
            chaine = str(liste[0]) + " " + str(liste[1]) + " " + str(liste[2]) + "\n"
            dump(chaine, fichier)
    if i == 2:
        return 'succes'
    else:
        return 'echec'