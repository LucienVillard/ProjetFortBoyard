from fonctions_utiles import *
from time import sleep
import random as r


Joueur = 0
Maitre = 1

#Jeu choisit -> Bataille navale

def suiv(joueur):
    if joueur == 0:
        return 1
    else:
        return 0

def grille_vide():
    return [[' ']*3,[' ']*3,[' ']*3]

def affiche_grille(grille,message):
    print(message)
    taille = len(grille[0])
    for i in range(taille):
        print(end="|")
        for j in range(taille):
            if j != taille:
                #Affiche les B en bleu et les x en rouge (juste estetique)
                if grille[i][j] == 'B':
                    print("",f"{BLUE}B{NORMAL}",end=" |")
                elif grille[i][j] == 'x':
                    print("",f"{RED}x{NORMAL}",end=" |")
                else:
                    print("",grille[i][j],end=" |")
        print("")
    print("-------------\n")



def demande_position2():
    pos = "0,0"
    while (ord(pos[0]) < ord('1') or ord(pos[0]) >= ord('4')) or (ord(pos[2]) < ord('1') or ord(pos[2]) >= ord('4')) or pos[1] != ',' or len(pos) != 3:
            #assure le format attendu
            pos = input(f"Entrez la position ({GREEN}ligne{NORMAL},{GREEN}colonne{NORMAL}) entre "
                        f"{GREEN}1{NORMAL} et {GREEN}3{NORMAL} (ex: 1,2) :")
    x, y = int(pos[0])-1, int(pos[2])-1
    return x,y

def demande_position():
    while True:
        pos = input(f"Entrez la position ({GREEN}ligne{NORMAL},{GREEN}colonne{NORMAL}) entre "
                    f"{GREEN}1{NORMAL} et {GREEN}3{NORMAL} (ex: 1,2) :")

        #Il faut maintenant assurer que le format de l'entrée est: x,y
        # Vérifie que la chaîne fait exactement 3 caractères
        if len(pos) == 3 and pos[1] == ',':
            # Vérifie que pos[0] et pos[2] sont entre '1' et '3' (pour éviter les indices qui n'existent pas)
            if '1' <= pos[0] <= '3' and '1' <= pos[2] <= '3':
                x, y = int(pos[0]), int(pos[2])
                return x - 1, y - 1  # Retourne les indices
            else:
                print(f"Les nombres doivent être entre {GREEN}1{NORMAL} et {GREEN}3{NORMAL}.")
        else:
            print(f"Format invalide. Veuillez entrer une position sous la forme {GREEN}x,y{NORMAL}.")


def init():
    grille = grille_vide()
    i = 0
    while i < 2:
        print(f"\n{BLUE}Bateau n°{i+1}{NORMAL}:")

        x, y = demande_position()

        if grille[x][y] == ' ':
            grille[x][y] = 'B'
            i += 1
        else:
            print(f"Veuillez entrer des {GREEN}coordonées différentes{NORMAL} du {BLUE}bateau n°1{NORMAL}")
    return grille

def init_maitre():
    grille_maitre = grille_vide()
    position_1 = (r.randint(0,2),r.randint(0,2))
    position_2 = position_1

    while position_2 == position_1 :
        position_2 = (r.randint(0,2),r.randint(0,2))

    grille_maitre[position_1[0]][position_1[1]] = 'B'
    grille_maitre[position_2[0]][position_2[1]] = 'B'
    return grille_maitre

def tour(joueur, grille_tirs_joueur, grille_adversaire) :
    if joueur == Joueur:    # Tour du joueur
        print(f"C'est à votre tour de faire {RED}feu{NORMAL} !")
        affiche_grille(grille_tirs_joueur,f"Rappel de l'{BLUE}historique des tirs{NORMAL} que vous avez effectués :")

        x, y = demande_position()

    else:   # Tour du maitre
        x, y = r.randint(0,2), r.randint(0,2)
        while grille_tirs_joueur[x][y] != ' ' :
            x, y = r.randint(0,2), r.randint(0,2)
        attente(f"Le maitre du jeu tire en {x+1}, {y+1}")

    if grille_adversaire[x][y] == 'B' :
        print(f"{YELLOW}Touché coulé !{NORMAL}\n")
        grille_tirs_joueur[x][y] = 'x'
    else:
        print(f"{BLUE}Dans l'eau...{NORMAL}\n")
        grille_tirs_joueur[x][y] = '.'

    print("--------------------\n")
    return grille_tirs_joueur

def gagne(grille_tirs_joueur):
    coule = 0
    for x in grille_tirs_joueur:
        for y in x:
            if y == 'x':
                coule += 1
    if coule == 2:
        return True
    return False


def jeu_bataille_navale():
    message = (f"\nChaque joueur doit placer {GREEN}2{NORMAL} bateaux sur une grille de 3x3."
               f"\nLes bateaux sont représentés par '{BLUE}B{NORMAL}' et les tirs manqués par '.'. Les bateaux"
               f"\ncoulés sont marqués par '{RED}x{NORMAL}'.\n")
    print(message)
    print("Commencez par placer vos bateaux :")
    grille_b_joueur = init()
    affiche_grille(grille_b_joueur,"Voici votre grille de jeu :")
    grille_b_maitre = init_maitre()

    grille_tir_joueur = grille_vide()
    grille_tir_maitre = grille_vide()

    win = ""
    joueur = Joueur
    while win == "":
        sleep(2)
        if joueur == Joueur:
            tour(joueur, grille_tir_joueur, grille_b_maitre)
        else:
            tour(joueur, grille_tir_maitre, grille_b_joueur)

        if gagne(grille_tir_joueur):
            print(f"{YELLOW}Vous avez gagné !{NORMAL}\n")
            win = True
        elif gagne(grille_tir_maitre):
            print(f"{RED}Le maitre a gagné...{NORMAL} Vous avez perdu.\n")
            affiche_grille(grille_b_maitre, f"La {RED}grille{NORMAL} de votre {RED}adversaire{NORMAL} était :")
            win = False

        joueur = suiv(joueur)


jeu_bataille_navale()