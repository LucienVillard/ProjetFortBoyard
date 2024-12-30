import random as r
from fonctions_utiles import *
from time import sleep
#Le module time sera utilisé pour mettre des pauses entre les affichage.
#Pour rendre le jeu plus fluide.

def bonneteau():
    L = ['A','B','C']
    n = 3

    message = (f"{GREEN}Bienvenue dans cette nouvelle épreuve!{NORMAL}\nIci, {GRAS}vous allez devoir choisir entre plusieurs bonneteaux{NORMAL} "
               f"sous l'un desquels se cache une {GRAS}{YELLOW}Clé{NORMAL}!\n{GREEN}J'espère que vous avez de la chance!{NORMAL}\n")
    print(message)
    print("Nous allons à présent commencer.\n")

    print(f"Vous avez le choix entre les bonneteaux suivants: {GREEN}A{NORMAL},{GREEN}B{NORMAL} ou {GREEN}C{NORMAL}.")

    for i in range(2):  #boucle pour les 2 tentatives
        n -= 1
        solution = r.choice(L)      #choix de la solution
        print(f"Il vous avez encore {GREEN}{n}{NORMAL} tentative(s).\n")

        sleep(1)
        choix = ""
        while choix not in ['A','B','C','a','b','c']:  #assurer que l'input est de la bonne longueur pour la suite
            choix = str(input(f"{BLUE}Lequel choisis tu?{NORMAL}"))

        print("Attente du resultat...")
        sleep(1)

        if ord(choix) < ord('z') or ord(choix) > ord('a'):
            choix = choix.upper()
        if solution == choix:
            print(f"Bravo!!! La {GRAS}{YELLOW}clé{NORMAL} était bien sous le bonneteau {BLUE}{choix}{NORMAL}.")
            print(f"Vous avez gagné une {GRAS}{YELLOW}clé{NORMAL}.")
            return True
        print(f"{RED}Dommage{NORMAL}, le bonneteau {RED}{choix}{NORMAL} ne cachait pas de {GRAS}{YELLOW}clé{NORMAL}.\n")
        print(f"Elle était sous le bonneteau {BLUE}{solution}{NORMAL}.\n")
        print("--------------------\n")

    print(f"Les deux tentatives sont écoulées et {GREEN}la {GRAS}{YELLOW}clé{NORMAL} {GREEN}n'a pas été trouvée{NORMAL}.")
    return False



def jeu_lance_des():
    message = (f"{GREEN}Bienvenue au lancé de dés!{NORMAL}\nIci, {GRAS}vous allez simplement devoir lancer des dés{NORMAL} "
               f"et si vous obtennez un {BLUE}6{NORMAL} vous gagnez une {GRAS}{YELLOW}Clé{NORMAL}!\n")
    print(message)
    print(f"Attention vous jouez contre le {RED}Maitre du jeu{NORMAL}. S'il gagne avant vous c'est perdu!\n{GREEN}Bonne chance!{NORMAL}\n")
    input("Appuyez sur Entrée quand vous êtes prêt.\n")

    int_nb_essai = 3
    for i in range(int_nb_essai):
        print(f"Il vous reste {GREEN} {3-i} {NORMAL} essais.\n")
        input("Appuyez sur Entrée pour lancer vos dés.\n")    #permet d'attendre la touche entrée

        print("Attente du resultat...")
        sleep(2)

        tuple_resultats_j = (r.randint(1,6),r.randint(1,6)) #Resultats du joueur
        print(f"Vous avez obtenu un {BLUE}{tuple_resultats_j[0]} {NORMAL}et un {BLUE}{tuple_resultats_j[1]}{NORMAL}.\n")

        if tuple_resultats_j[0] == 6 or tuple_resultats_j[1] == 6:
            sleep(1)
            print(f"{YELLOW} Bravo !!! Vous avez gagné un clé. {NORMAL}")
            sleep(3)
            return True

        sleep(2)

        print(f"{RED}Le Maitre du jeu lance ses dés...{NORMAL}\n")
        sleep(2)

        tuple_resultats_m = (r.randint(1,6),r.randint(1,6)) #Resultats du maitre du jeu
        print(f"Le Maitre du jeu a obtenu un {RED}{tuple_resultats_m[0]} {NORMAL}et un {RED}{tuple_resultats_m[1]}{NORMAL}.\n")

        if tuple_resultats_m[0] == 6 or tuple_resultats_m[1] == 6:
            sleep(1)
            print(f"{RED}Le Maitre du jeu a gagné la partie!!!{NORMAL} Vous avez perdu.")
            sleep(3)
            return False

        sleep(2)
        print(f"{GREEN}Personne n'a gagné pour l'instant{NORMAL}. Nous passons au {GREEN}prochain tour{NORMAL}. Préparez vous!")
        sleep(2)

    sleep(2)
    print(f"Les trois tentatives sont écoulées et {GREEN}personne n'a obtenu 6{NORMAL}. C'est donc match nul.")
    return False


def epreuve_hasard():
    epreuve = r.randint(1,2)
    if epreuve == 1:
        return bonneteau()
    else:
        return jeu_lance_des()

epreuve_hasard()