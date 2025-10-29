# le jeu du nombre mystère 

import random
import sys
# Ce script implémente un jeu où l'utilisateur doit deviner un nombre mystère entre 1 et 100.
nombre_mystere = random.randint(1, 100)
essais_restant= 5
print("Bienvenue au jeu du nombre mystère !")
print("Je pense à un nombre entre 1 et 100.")
        

# On initialise le nombre mystère et le nombre d'essais restants
while True:  # boucle pour demander la proposition de l'utilisateur
    
    print(f"vous avez {essais_restant} essai{'s' if essais_restant > 1 else ""}.")
    while essais_restant > 0:  # boucle principale du jeu
        print(f"Vous avez {essais_restant} essai{'s' if essais_restant > 1 else ''} restant{'s' if essais_restant > 1 else ''}.")
    # Demande à l'utilisateur de deviner le nombre
        proposition = input("Devinez le nombre : ")

        if not proposition.isdigit():
            print("Veuillez entrer un nombre valide.")
            continue   

        proposition = int(proposition) # conversion de la proposition en entier

        # Vérifie si la proposition est correcte
        if proposition < nombre_mystere:
            print("C'est plus grand !")
        elif proposition > nombre_mystere:
            print("C'est plus petit !")
        else:
            
            break # fin de la boucle si le nombre est trouvé

        essais_restant -= 1  # décrémente le nombre d'essais restants

    # Vérifie si l'utilisateur a gagné ou perdu
    if essais_restant == 0:
        
        print(f"Désolé, vous avez perdu. Le nombre mystère était : {nombre_mystere}.")
    else:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère : {nombre_mystere} en {6 - essais_restant} coups !")
        
                 
        
    # On demande à l'utilisateur s'il veut effectuer une autre opération
    oui = "oui"
    non = "non" 
    while True:
        reponse = input("Voulez-vous effectuer une autre partie ? (oui/non) : ")
        if reponse == oui:
        # Si l'utilisateur veut continuer, on relance le programme 
            print("Recommençons !")
            break # On sort de la boucle pour revenir à la principale et recommencer le processus
        elif reponse == non:
            # Si l'utilisateur ne veut pas continuer, on quitte le programme
            print("Merci d'avoir joué au jeu du nombre mystère !")
            print("Au revoir !")
            
            sys.exit()  # Quitte le programme
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
            continue
            


        

        

            
            