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


#Afficher ... après un message popur simuler une sorte chargement
def attente(message):
    print(message,end="")
    for i in range(3):
        sleep(0.8)
        if i != 2:
            print('.',end="")
        else:
            print('.')
    sleep(0.8)