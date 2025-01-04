1. Présentation Générale :

  o Titre du Projet

  o Contributeurs : Villard Lucien, David Maxime

  o Description : Créer un jeu inspiré de l'émission Fort Boyard avec 4 épreuves jouable en équipe de 1 à 3 joueurs.

  o Fonctionnalités Principales : 

    Formation d'une équipe.
    Interraction avec l'utilisateur à travers la console python.
    Epreuves de mathématiques, de logique (Bataille navale), de hasard, et d'enigmes.
    Sauvegarde d'un score pour chaque utilisateur.


  o Technologies Utilisées :

    Language : Python
    Bibliothèques : Random, Time
    Encodage "ANSI" pour afficher en couleur
    Outil: PyCharm Community Edition, IntelliJ IDEA
    

  o Installation :
    
    pour cloner le dépôt Git avec PyCharm : Trouver l'URL dans <>Code -> HTTPS sur GitHub et le copier
                                              Dans PyCharm ouvrir la barre de menus (En haut à gauche) -> Git -> Clone...
                                              Coller l'URL dans la case appropriée et choisir l'endroit où cloner
                                              Appuyer sur "Cloner" pour finaliser.
    
    Une fois Cloné dans PyCharm accune installation n'est nécessaire .

    Hors Pycharm : Utiliser la commande "git clone https://..." dans Git Bash

  o Utilisation :

    Pour lancer le programme : Simplement exécutez le programme principale : main.py .
    Aucune autre commande n'est nécessaire pour executer le programme

2. Documentation Technique

  o Algorithme du jeu :

    1 - Présentation des règles du jeu via une fonction introduction().
    2 - Création de l'équipe avec la fonction composer_equipe().
    3 - Sélection aléatoire d'épreuves parmi les types disponibles : énigmes, mathématiques, logique.
    4 - Gestion des réponses des joueurs et vérification de la validité.
    5 - Suivi du score et des clés obtenues.
    6 - Détermination de la victoire/défaite et affichage des résultats.

  o Détails des fonctions implémentées :

    main.py :
      - jeu() Fonction principale qui fait le lien entre toutes les autres. Permet l'execution du jeu.
    
    fonctions_utiles.py :
      - attente(message) message -> Chaine de charactère, Permet d'afficher le message avec ". . ." à la fin avec un delai entre chaques '.' -> simule une attente
      
      - est_entier(chaine) chaine -> Chaine de charactère, Permet de vérifier si chaine est un contient un entier sous forme de charactère. return un Booléen
      - est_float(chaine) chaine -> Chaine de charactère, Permet de vérifier si chaine est un contient un float sous forme de charactère. return un Booléen
      - est_fraction(chaine) -> chaine -> Chaine de charactère, Permet de vérifier si chaine est un contient une fraction sous forme "a/b" avec a et b entiers. return un Booléen

      - introduction() Fonction qui affiche le message de debut de jeu et les règles.
      - composer_equipe() Permet à l'utilisateur de composer une équipe de 1 à 3 personnes. return une liste de dictionnaires.
      - menu_epreuves() Affiche à l'utilisateur la liste d'epreuves et lui demande de choisir. return un entier
      - choisir_joueur(equipe) equipe -> Liste, Affiche la liste de joueurs et demande de choisir qui participe à l'epreuve. reutrn un entier

      - sauvegarde(joueur) joueur -> dictionnaire, Permet de sauvegarder le nombre de clés gagnées par un utilisateur. Sauvegarde le tout dans un fichier text: historique.txt

    epreuves_mathématiques.py :
      - epreuve_math_factorielle() Permet le déroulement de l'épreuve de factorielle. return un Booléen

      - resoudre_equation_lineaire() Créée une équation linéaire aléatoire et renvoie le résultat sous forme de string et les eux entier: return un string, deux entiers
      - epreuve_math_equation() Permet le déroulement de l'epreuve d'equation linéaire. return un Booléen

      - roulette_maths() Permet le déroulement de l'epreuve de roulette. C'est à dire aléatoirement : addition, soustraction, multiplication, division. return un Booléen

      - epreuve_maths() choisit une des epreuves de math au hasard.

    epreuves_hasard.py :
      - bonneteau() Permet le déroulement de l'epreuve des Bonneteaux. return un Booléen
      - jeu_lance_des() Permet le déroulement de l'epreuve de lancé de dés. return un Booléen

      - epreuve_hasard() Choisit une des deux epreuves au hasard.

    epreuves_logiques.py :
      - suiv(joueur) joueur -> entier, return un entier qui représente le joueur suivant. 0 ou 1
      - grille_vide() Initialise une matrice vide de 3x3 avec des listes. return une liste (2D)
      - affiche_grille(grille,message) grille -> liste (2D), message -> chaine de caractère, affiche une grille de jeu (bataille navale) pour l'utilisateur
      - demande_position() Demande une position sur la matrice à l'utilisateur sous la forme : "x,y"
      - init() Permet à l'utilisateur d'initialiser sa grille de jeu. return une liste (2D)
      - init_maitre() Initialise la grille de jeu du maitre de manière aléatoire. return une liste (2D)
      - tour(joueur, grille_tirs_joueur, grille_adversaire) joueur -> entier, grille_tirs_joueur -> liste (2D), grille_adversaire -> liste (2D), Effectue un tour de jeu. return grille avec le tir
      - gagne(grille_tirs_joueur) grille_tirs_joueur -> liste (2D), Verfie si le joueur dont la grille est en paramètre a gagné ou non. return un Booléen
      - jeu_bataille_navale() Permet le déroulement de l'epreuve. return un Booléen

    enigmes_pere_fouras :
      - charger_enigmes(fichier) fichier -> chaine de caractère, Charge les données du fichier enigmes.json. return liste de dictionnaires
      - enigme_pere_fouras() Permet le déroulement de l'epreuve d'énigmes. return un Booléen

    Epreuve_finale.py :
      - salle_De_Tresor() Permet le déroulement de l'epreuve de salle du trésor. return Booléen
  o Gestion des Entrées et Erreurs :

    Pour gerer les erruers liées aux input de l'utilisateur nous avons mit en place des boucles
    qui redemandent à l'utilisateur la valeur tant qu'elle n'a pas le bon format

    Il n'y à pas de bug qui procurent un erreur dans ce que nous avons testé. Chaque input est "protegé" et a forcément le bon format.
    Juste un problème avec la sauvegarde : deux utilisateurs qui ont le même nom vont avoir la même sauvegarde.
    Il faudrait utiliser une id unique mais cela demanderai une refonte du programme.

4. Tests et Validation

  o Stratégies de Test : Boucle tant que sur chaque input pour forcer l'utilisateur a donner une valeur qu'on peut traiter.
  
  Exemple de test spécifiques et résultats:

  ![image](https://github.com/user-attachments/assets/d6ef25c3-36b2-4bd9-a722-e8268cdeec72)
