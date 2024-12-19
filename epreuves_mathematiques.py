import random
from time import sleep
ESC = '\x1b'
NORMAL = ESC + '[0m'
RED    = ESC + '[31m'
YELLOW = ESC + '[33m'
GREEN  = ESC + '[32m'
BLUE   = ESC + '[34m'
PURPLE = ESC + '[35m'
GRAS = "\033[1m"
def epreuve_math_factorielle():
    print("")
    n=random.randint(1,10)
    print(f"Trouve la valeur de factorielle {BLUE}{n}{NORMAL}")
    sleep(1)
    y=int(input("Votre réponse:"))
    x=1
    for i in range(1, n+1):
       x*=i
    if x==y:
        print (f"{GREEN}Correct!{YELLOW} Vous gagnez une clé.{NORMAL}")
        return True
    else:
        print (f"{RED}La réponse est incorrecte{NORMAL}")
        return False

def resoudre_equation_lineaire():
    a=random.randint(1,10)
    b=random.randint(1,10)
    res = -b/a
    if type(res) == float and str(res)[-2:] == ".0":
        res = str(int(res))
    elif type(res) == float:
        res = str(res)
    else:
        res = str(res)
    return a, b, res

def epreuve_math_equation():
    print("")
    #implementation de l'autre fonction
    a, b, res = resoudre_equation_lineaire()
    print(f"Trouve la valeur de x de cette équation : {BLUE}{a}x+{b}=0{NORMAL}")
    sleep(1)
    prop=input("Quelle est la valeur de x:")
    if "/" in prop:
        prop = prop.split("/")
        a = int(prop[0])
        b = int(prop[1])
        prop = str(a / b)
    if prop==res or prop=="-"+str(b)+"/"+str(a):
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
    y=int(input("Votre réponse :"))
    if y==res:
        print(f"{GREEN}Bonne réponse! {YELLOW}Vous avez gagné une clé.{NORMAL}")
        return True
    else:
        print(f"{RED}Mauvaise réponse!{NORMAL}")
        return False

def epreuve_maths():
    x=random.randint(1,3)
    if x==1:
        return epreuve_math_factorielle()
    elif x==2:
        return epreuve_math_equation()
    else:
        return roulette_maths()
epreuve_maths()