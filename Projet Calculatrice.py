# Projet Calculatrice 

# Auteur : Millet Charles

# Date de création : 22/06/2025
# Date de mise à jour : 24/06/2025
# Version : 2.4

# Description : ce programme est une calculatrice qui permet à l'utilisateur d'entrer deux nombres décimaux et un symbole de calcul (+, -, *, /).
# Une autre version de ce programme avec seulement des nombres entiers était la base de ce projet. Mais il est plus pertinant d'avoir une calculatrice qui accepte les nombres décimaux.

# On déclare 3 variables
a = b = c = ""
# Liste des symboles autorisés
symboles = ['+', '-', '*', '/']
# on déclare oui et non
oui = "oui"
non = "non"
# On importe le module sys pour pouvoir quitter le programme si nécessaire
import sys  


# On affiche un message de bienvenue
print("Bienvenue dans la calculatrice !")


while True: #on créé une boucle principale qui va permettre de relancer le programme si l'utilisateur le souhaite.
# On crée une boucle infinie while pour demander les entrées jusqu'à ce qu'elles soient valides.
# Tant que a et b ne sont pas des nombres et que c n'est pas un symbole de calcul, on boucle.
    while True:
        # On demande deux nombres et symbole à l'utilisateur
        a = input("Entrez un premier nombre : ")
        c = input("Entrez un symbole : ")
        b = input("Entrez un deuxième nombre : ")
        # On vérifie si a et b sont des nombres et c est un symbole de calcul
        # On utilise un try-except pour gérer les erreurs de conversion
        try : 
        # On essaie de convertir a et b en décimaux
            a_float = float(a)
            b_float = float(b)
            if c in symboles:
                break  # Les entrées sont valides, on sort de la boucle
            else: # Si c n'est pas un symbole valide, on affiche un message d'erreur
                print("Symbole invalide. Veuillez entrer +, -, * ou /.")
        except ValueError:
        # Si la conversion échoue, on affiche un message d'erreur
            print("Veuillez entrer des nombres valides.")

    # On effectue l'opération en fonction du symbole entré
    if c == '+':
        resultat = a_float + b_float 
        print(f"Le résultat de l'addition de {a} avec {b} est égal à {resultat}")
    elif c == '-':
        resultat = a_float - b_float
        print(f"Le résultat de la soustraction de {a} avec {b} est égal à {resultat}")
    elif c == '*':
        resultat = a_float * b_float
        print(f"Le résultat de la multiplication de {a} avec {b} est égal à {resultat}")    
    elif c == '/':
        if b_float == 0:
            print("Erreur : Division par zéro n'est pas permise.")
        else:
            resultat = a_float / b_float    
            print(f"Le résultat de la division de {a} avec {b} est égal à {resultat}")

    # On demande à l'utilisateur s'il veut effectuer une autre opération
    while True:
        reponse = input("Voulez-vous effectuer une autre opération ? (oui/non) : ")
        if reponse == oui:
            # Si l'utilisateur veut continuer, on relance le programme 
            print("Recommençons !")
            break # On sort de la boucle pour revenir à la principale et recommencer le processus
        
        elif reponse == non:
            # Si l'utilisateur ne veut pas continuer, on quitte le programme
            print("Merci d'avoir utilisé la calculatrice !")
            print("Au revoir !")
            # Fin du programme
            sys.exit()  # Quitte le programme
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

