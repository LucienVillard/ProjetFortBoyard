import json
import random as r
from fonctions_utiles import *

def salle_De_Tresor():
    with open("data/indicesSalle.json", 'r', encoding = 'utf-8') as f:
        jeu_tv = json.load(f)
    liste_annee = list(jeu_tv["Fort Boyard"].keys())
    annee = r.choice(liste_annee)      #Choisit une année
    emission = r.choice(list(jeu_tv["Fort Boyard"][annee].keys()))      #Choisit une émission

    #choisit les indices et le mot_code en fonction de l'émission
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]

    message = (f"Vous êtes arrivés jusqu'à la porte de la {YELLOW}salle du Tresor{NORMAL}. Je vous en félicite."
               f"\nVous allez maintenant devoir {GREEN}déchiffrer un code{NORMAL} qui vous permettra d'accéder "
               f"à la {YELLOW}salle du Tresor{NORMAL}"
               f"\n\nFaites {RED}attention{NORMAL}, vous disposerez d'un "
               f"{GREEN}nombre limité d'essais{NORMAL}.\n")
    print(message)

    print(f"Voici les trois premiers {GREEN}indices{NORMAL} :")
    for indice in indices[:4]:
        print(f"{indice}\n")

    tentative = 3
    bonne_reponse = False
    while tentative > 0 and bonne_reponse == False:
        reponse = input("Entrez votre réponse :")

        #.lower() assure qu'on compare les mêmes caractères. Ex : pas un 'a' avec un 'A'
        if reponse.lower() == mot_code.lower():     #Bonne réponse
            print(f"Bravo ! vous avez trouvé le mot code en {GREEN}{3 - tentative + 1}{NORMAL} essais.")
            return True
        else:   #Mauvaise réponse
            tentative -= 1
            if tentative > 0:   #Si reste des tentatives
                print(f"Mauvaise réponse ! Il vous reste {GREEN}{tentative}{NORMAL} tentatives.")
                print(f"Voici un nouvel indice : {indices[4:][3 - tentative-1]}")
            else:       #Si plus de tentatives
                print(f"Ce n'est toujours pas ça !\n"
                      f"Vous avez épuisé toutes vos tentatives. Le mot code était : {BLUE}{mot_code}{NORMAL}.")
                return False
