import random
from fonctions_utiles import *
import json
def charger_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)

    #remplace chaques dico de la liste enigmes en un dico: {question : reponse}
    for i in range(len(enigmes)):
        question, reponse = list(enigmes[i].values())[-2:]
        enigmes[i] = {"question" : question, "reponse" : reponse}
    return enigmes


def enigme_pere_fouras():
    print(f"{GREEN}Bienvenue{NORMAL} dans l'épreuve des {GREEN}enigmes du père Fouras{NORMAL} !\n"
          f"Vous allez devoir trouver la {BLUE}solution{NORMAL} à une {BLUE}énigme{NORMAL} "
          f"pour gagner une {GRAS}{YELLOW}clé{NORMAL}.\n"
          f"Voici l'énigme :")
    L=[]
    essais=3
    for i in charger_enigmes("data/enigmesPF.json"):
        L.append(i)
    x=random.randint(0,len(L)-1)
    question=L[x]["question"]
    reponse=L[x]["reponse"]
    print("\n"+question+"\n")
    while essais>0:
        rep=input("Entrez votre réponse : ")
        rep=rep.lower()
        reponse=reponse.lower()
        if rep==reponse:
            print(f"{GREEN}La réponse est correcte{NORMAL}")
            sleep(1)
            print(f"{YELLOW}Vous gagnez une {GRAS}clé{NORMAL}")
            return True
        else:
            essais-=1
            if essais>0:
                print(f"{RED}La réponse est incorrecte{NORMAL}, il vous reste {essais} essais")
            else:
                print(f"{RED}Vous avez échoué{NORMAL}")
                attente("La réponse était")
                print(f"{BLUE}{reponse}{NORMAL}")
                return False
