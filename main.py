from epreuves_mathematiques import *
from epreuves_hasard import *
from epreuves_logiques import *
from enigme_pere_fouras import *
from epreuve_finale import *
from fonctions_utiles import *


def jeu():
    introduction()  #Affiche message de bienvenue et les règles
    equipe = composer_equipe()   #Compose l'équipe


    #Debut des epreuves
    nb_cle = 0
    while nb_cle < 3:
        epreuve = menu_epreuves() #choisir l'épreuve
        n_joueur = choisir_joueur(equipe)   #choisir joueur qui va jouer

        #Lancer la bonne épreuve
        if epreuve == 1:
             resulat = epreuve_maths()     #epreuve de math
        elif epreuve == 2:
            resulat = jeu_bataille_navale()   #epreuve de logique
        elif epreuve == 3:
            resulat = epreuve_hasard()    #epreuve de hasard
        else:
            resulat = enigme_pere_fouras()    #enigmes pere Fouras

        if resulat:
            equipe[n_joueur-1]["cles_gagnee"] += 1
            nb_cle += 1

        attente("")


    #Ici l'équipe a forcément 3 clés
    #Donc épreuve finale
    if salle_De_Tresor():
        print(f"\n\n{GRAS}{YELLOW}Félicitations, vous avez remporté Fort Boyard !{NORMAL}")

    for joueur in equipe:
        #Sauvegarde le nombre de cle que chaque joueur a gagné durant la partie
        sauvegarde(joueur)


#Appel de la fonction jeu() pour lancer le jeu
jeu()