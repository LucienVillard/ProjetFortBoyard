from time import sleep


#Couleurs
ESC = '\x1b'
NORMAL = ESC + '[0m'
RED    = ESC + '[31m'
YELLOW = ESC + '[33m'
GREEN  = ESC + '[32m'
BLUE   = ESC + '[34m'
PURPLE = ESC + '[35m'
GRAS = "\033[1m"


#Afficher "..." après un message popur simuler une sorte chargement
def attente(message):
    print(message,end="")
    for i in range(3):
        sleep(0.8)
        if i != 2:
            print('.',end="")
        else:
            print('.')
    sleep(0.8)


def est_entier(chaine):
    #Verif si chaine est entier (pour verifier les input où on attend un entier)
    if len(chaine) == 0:
        return False
    elif chaine[0] == '-':  # Vérifie le signe négatif
        chaine = chaine[1:]  # Ignore le signe pour la vérification

    if len(chaine) != 0:
        for i in chaine:
            if '0' > i or '9' < i:
                return False
    else:
        return False
    return True

def est_float(chaine):
    if chaine[0] == '-':  # Vérifie le signe négatif
        chaine = chaine[1:]  # Ignore le signe pour la vérification

    if '.' in chaine:  # Vérifie la présence d'un point
        parts = chaine.split('.')
        if len(parts) != 2:  # Un nombre flottant doit avoir une seule partie décimale
            return False
        # Vérifie que les deux parties sont des entiers (entière ou décimale)
        partie_entiere, partie_decimale = parts
        if est_entier(partie_entiere) and est_entier(partie_decimale):
            return True
        else:
            return False
    else:
        return False

def est_fraction(chaine):
    if chaine[0] == '-':  # Vérifie le signe négatif
        chaine = chaine[1:]  # Ignore le signe pour la vérification

    if '/' not in chaine:
        return False
    parties = chaine.split('/')

    if len(parties) != 2:
        return False
    elif not est_entier(parties[0]) or not est_entier(parties[1]):
        return False
    return True


def introduction():
    """Affiche le message de bienvenue et explique les règles du jeu."""
    print(f"Bienvenue à {GRAS}{YELLOW}Fort Boyard{NORMAL} !\n"
          f"Votre {GREEN}mission{NORMAL} est de relever des épreuves pour gagner des "
          f"{GRAS}{YELLOW}clés{NORMAL}, "
          f"qui vous permettront de déverrouiller la {YELLOW}salle du trésor{NORMAL}.\n"
          f"Vous devez former une {GREEN}équipe{NORMAL} de {GREEN}1{NORMAL} à {GREEN}3{NORMAL} joueurs et participer à diverses épreuves "
          f"comme de la résolution d'énigmes ou des tests de logique.\n"
          f"L'objectif est de récolter {GREEN}3{NORMAL} {GRAS}{YELLOW}clés{NORMAL} pour accéder à la {YELLOW}salle du trésor{NORMAL}.\n"
          f"{GREEN}Bonne chance !{NORMAL}")

def composer_equipe():
    nb_joueurs = ""
    condition = False
    while not condition:
        nb_joueurs = input("Entrez le nombre de joueurs :")
        if est_entier(nb_joueurs):
            nb_joueurs = int(nb_joueurs)
            if nb_joueurs > 3 or nb_joueurs < 1:
                print(f"Le nombre de joueurs doit être comprit entre "
                      f"{GREEN}1{NORMAL} et {GREEN}3{NORMAL}")
            else:
                condition = True
        else:
            print(f"Le nombre de joueurs doit être un entier")

    info_joueurs = []
    existe_leader = False
    for i in range(nb_joueurs):
        print(f"\n{BLUE}Joueur n°{i+1}{NORMAL} :")
        info_joueurs.append({})
        info_joueurs[i]["nom"] = input(f"Entrez votre {GREEN}nom{NORMAL} :")
        info_joueurs[i]["profession"] = input(f"Quelle est votre {GREEN}profession{NORMAL} ?")


        if not existe_leader:  #Si il n'y à pas encore de leader on demande
            leader = ""
            while leader != 'oui' and leader != 'non':
                leader = input(f"Êtes vous le {GREEN}leader{NORMAL} de {GREEN}l'équipe{NORMAL} ('oui' ou 'non') ?").lower()

            if leader == 'oui':
                info_joueurs[i]["leader"] = True
                existe_leader = True
            else:
                info_joueurs[i]["leader"] = False

        else:   #S'il y a déja un leader
            info_joueurs[i]["leader"] = False
        info_joueurs[i]["cles_gagnee"] = 0

    if not existe_leader:
        info_joueurs[0]["leader"] = True
        print(f"\nComme personne ne veut être leader ce role reviendra au {BLUE}jouer 1{NORMAL}.\n")
    else:
        print(f"\nVotre {GREEN}équipe{NORMAL} a bien été formée.\n")
    return info_joueurs

def menu_epreuves():
    print(f"\nVous pouvez maintenant choisir un {GREEN}type d'épreuve{NORMAL} :\n")
    message = "1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras\n"
    print(message)

    epreuve = ""
    while len(epreuve) != 1 or epreuve < '1' or epreuve > '4':
        epreuve = input("Choix :")
    epreuve = int(epreuve)
    return epreuve

def choisir_joueur(equipe):
    print(f"\nVous devez maintenant {GREEN}choisir{NORMAL} le {BLUE}joueur{NORMAL} qui "
          f"participera à l'{GREEN}épreuve{NORMAL} :\n")

    for i in range(len(equipe)):
        joueur = equipe[i]
        if joueur["leader"]:    #Pour le leader
            print(f"{i+1}. {joueur["nom"]} ({joueur["profession"]}) - Leader\n")
        else:   #Pour les membres
            print(f"{i+1}. {joueur["nom"]} ({joueur["profession"]}) - Membre\n")

    joueur = ""
    while len(joueur) != 1 or joueur < '1' or joueur > str(len(equipe)):
        #assure que l'input est un numéro de joueur
        joueur = input(f"Entrez le {GREEN}numéro du joueur{NORMAL} :")
    return int(joueur)


def sauvegarde(joueur):
    with open("historique.txt", 'r', encoding='utf-8') as f:
        dico_donnee = {}
        for ligne in f:
            if len(ligne) != 0: #saute les lignes vides
                nom, nb_cle = ligne.split(":")
                dico_donnee[nom] = int(nb_cle)

    if joueur["nom"] not in dico_donnee:
        dico_donnee[joueur["nom"]] = joueur["cles_gagnee"]
    else:
        dico_donnee[joueur["nom"]] += joueur["cles_gagnee"]

    with open("historique.txt", 'w', encoding='utf-8') as f:
        for nom,nb_cle in dico_donnee.items():
            f.write(f"{nom}:{nb_cle}\n")

