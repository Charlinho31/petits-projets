# liste de courses
import sys
import os
import json

CUR_DIR = os.path.dirname(__file__) # Chemin du répertoire 
LISTE_PATH = os.path.join(CUR_DIR, "liste.json") # Chemin du fichier JSON pour stocker la liste de courses

# Liste de courses interactive en Python

menu ="""Veuillez choisir entre les options suivantes :
1 : Ajouter un élément à la liste de courses 
2 : Afficher les éléments de la liste de courses 
3 : Retirer un élément de la liste de courses 
4 : Vider la liste de courses
5 : Quitter le programme
? Votre choix : """

# Liste des choix valides pour le menu
Menu_choix = ["1", "2", "3", "4", "5"] 

# Chargement de la liste de courses depuis le fichier JSON s'il existe
if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, 'r') as f:
        try:
            Liste = json.load(f)  # Charge la liste de courses depuis le fichier JSON
        except json.JSONDecodeError:
            print("Le fichier liste.json est vide ou corrompu. Une nouvelle liste sera créée.")           
else:
    Liste = []  # Initialise une nouvelle liste de courses si le fichier n'existe pas

while True: 
    choix = ""  # Réinitialise le choix à chaque itération
    while choix not in Menu_choix:  # Continue de demander un choix valide
        choix = input(menu) # Demande à l'utilisateur de faire un choix
        if choix not in Menu_choix: # Vérifie si le choix est valide
            print("veuillez choisir une option valide.") 

    if choix == "1": # Ajouter un élément à la liste de courses
        element = input("Entrez l'élément à ajouter : ")
        Liste.append(element)
        print(f"{element} a été ajouté à la liste de courses.")
    
    elif choix == "2": # Afficher les éléments de la liste de courses
        if Liste: # Vérifie si la liste n'est pas vide
            print("Liste de courses :")
            for i, element in enumerate(Liste):
                print(f"{i}. {element}")
        else:
            print("La liste de courses est vide.")

    elif choix == "3": # Retirer un élément de la liste de courses
        element = input("Entrez l'élément à retirer : ")  
        if element in Liste: # Vérifie si l'élément est dans la liste
            # Retire l'élément de la liste
            Liste.remove(element)
            print(f"{element} a été retiré de la liste de courses.")
        else: # Si l'élément n'est pas dans la liste, affiche un message
            print(f"{element} n'est pas dans la liste de courses.")

    elif choix == "4": #Vider la liste de courses
        Liste.clear()
        print("La liste de courses a été vidée.")

    elif choix == "5": # Sauvegarder et quitter le programme 
        with open(LISTE_PATH, 'w') as f:
            json.dump(Liste, f, indent=4)  # Sauvegarde la liste de courses dans le fichier JSON
        print("La liste de courses a été sauvegardée.")
        print("Au revoir!")
        sys.exit() 
    
    print("=" * 40)  # Affiche une ligne de séparation
    print()  # Ajout d'une ligne vide pour une meilleure lisibilité
    print("État actuel de la liste de courses :", Liste) # Affiche l'état actuel de la liste de courses
    print()  # Ajout d'une ligne vide pour une meilleure lisibilité