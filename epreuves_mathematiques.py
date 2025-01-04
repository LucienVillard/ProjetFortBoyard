import random
from fonctions_utiles import *
from time import sleep

def epreuve_math_factorielle():
    print("")
    n=random.randint(1,10)
    print(f"Trouvez la valeur de {GREEN}factorielle {n}{NORMAL}.")

    sleep(1)

    y = ""      #Assure que l'input est bien un entier.
    while not est_entier(y):
        y = input(f"Votre réponse (doit être un {GREEN}entier{NORMAL}) :")
    y = int(y)

    res=1
    for i in range(1, n+1):
        res*=i
    if res == y:
        print (f"{GREEN}Correct! Vous gagnez une {GRAS}{YELLOW}clé{NORMAL}.")
        return True
    else:
        print (f"{RED}La réponse est incorrecte.{NORMAL}")
        return False

def resoudre_equation_lineaire():
    a=random.randint(1,10)
    b=random.randint(1,10)
    res = -b/a
    if type(res) == float and str(res)[-2:] == ".0":    #Si res est un un entier de type float on le remet en int.
        res = str(int(res))
    elif type(res) == float:
        res = str(res)
    else:
        res = str(res)
    return a, b, res


def epreuve_math_equation():
    #implementation de l'autre fonction
    a, b, res = resoudre_equation_lineaire()
    print(f"Trouve la valeur de x de cette équation : {BLUE}{a}x+{b}=0{NORMAL}")
    sleep(1)
    cond = False
    prop = " "
    while not est_entier(prop) and not est_float(prop) and not cond:
        prop=input("Quelle est la valeur de x:")
        if len(prop) == 0:      #Si l'entrée est vide on redemande (" " ne passe pas les comditions de la boucle)
            prop = " "
        if est_fraction(prop):      #Si l'entrée est sous forme de fraction
            a, b = prop.split('/')
            a, b = int(a), int(b)
            prop = str(a / b)
            cond = True

    if prop == res:
        print (f"{GREEN}Correct! {YELLOW}Vous gagnez une clé.{NORMAL}")
        return True
    else:
        print (f"{RED}Mauvaise réponse{NORMAL}")
        return False

def roulette_maths():
    print("")
    liste_op=["addition","soustraction","multiplication"]
    liste_nb=[]
    res=0
    for i in range(5):
        x=random.randint(1,21)
        liste_nb.append(x)
    op=random.choice(liste_op)
    if op=="addition":
        for i in range(5):
            res+=liste_nb[i]
    elif op=="soustraction":
        res=liste_nb[0]
        for i in range(1,5):
            res-=liste_nb[i]
    else:
        res=1
        for i in range(5):
            res*=liste_nb[i]
    print(f"Calculez le résultat en combinant ces nombres avec une {BLUE}{op}{NORMAL}")
    sleep(1)
    print(f"{GRAS}{liste_nb}{NORMAL}")

    sleep(1)

    y = ""      #Assure que l'input est bien un entier.
    while not est_entier(y):
        y = input(f"Votre réponse (doit être un {GREEN}entier{NORMAL}) :")

    y = int(y)
    if y == res:
        print(f"\n{GREEN}Bonne réponse ! Vous gagnez une {GRAS}{YELLOW}clé{NORMAL}.\n")
        return True
    else:
        print(f"\n{RED}Mauvaise réponse!{NORMAL}\n")
        return False

def epreuve_maths():
    x=random.randint(1,3)
    if x==1:
        return epreuve_math_factorielle()
    elif x==2:
        return epreuve_math_equation()
    else:
        return roulette_maths()
