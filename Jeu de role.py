# 🏹 BATTLE RPG - EDITION 80's 🏹

# personnages : vous et un ennemi.
# 50 points de vie chacun.
# 3 potions pour vous, aucune pour l'ennemi.
# Vous pouvez attaquer ou utiliser une potion.
# Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
# Votre attaque = dégâts aléatoires compris entre 5 et 10 points de vie.
# L'attaque de l'ennemi = dégâts aléatoires compris entre 5 et 15 points de vie.
# Lorsque vous utilisez une potion, vous passez le prochain tour.

import random
import sys
import time

# Couleurs & effets ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"



# Fonction pour afficher lentement (effet rétro)
def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Barre de vie style 80's [#####-----]
def retro_hp_bar(hp):
    hp = max(0, min(50, hp))  # Clamp entre 0 et 50
    filled = int(hp)
    empty = 50 - filled
    return "[" + "#" * filled + "-" * empty + "]"

# Ligne de séparation colorée
def separator():
    print(CYAN + "=" * 50 + RESET)

# Animation dots ... pour potion
def loading_dots(times=3, delay=0.4):
    for _ in range(times):
        print(YELLOW + "." + RESET, end='', flush=True)
        time.sleep(delay)
    print()

# Initialisation des variables
enemy_health = 50
player_health = 50
potions = 3
skip_turn = False

# Introduction du jeu

separator()
print_slow(BOLD + "🏹 BATTLE RPG - EDITION 80's 🏹" + RESET)
separator()
print_slow("Bienvenue dans le jeu de rôle !")
print_slow("Vous avez 50 points de vie et 3 potions. l'ennemi a 50 points de vie.")   
separator()

while True:  # Boucle principale du jeu
    enemy_health = 50
    player_health = 50
    potions = 3
    skip_turn = False
    while True : # Déroulé de la partie
    # tour du joueur
        if skip_turn:  # Si le joueur a utilisé une potion, il passe son tour
            print_slow(YELLOW + "Vous avez utilisé une potion et passé le dernier tour. ⏭️" + RESET)
            skip_turn = False  
            continue  # Passe au tour de l'ennemi
        else:  
            user_choice = ""
            while user_choice not in ["1", "2"]:
                print_slow(MAGENTA + "veuillez choisir une action :" + RESET)
                user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        
            if user_choice == "1": # Attaque 
                attack_damage = random.randint(5, 10)
                enemy_health -= attack_damage
                print_slow(RED + f"Vous attaquez l'ennemi et lui infligez {attack_damage} points de dégâts. ⚔️" + RESET)

            elif user_choice == "2" and potions > 0: # Utilisation d'une potion
                print_slow("Vous utilisez une potion 🧪", delay=0.05)
                loading_dots()
                potion_heal = random.randint(15, 50)
                player_health += potion_heal
                potions -= 1
                skip_turn = True # Le joueur passe son tour après avoir utilisé une potion
                print_slow(GREEN + f"Vous récupérez {potion_heal} points de vie ❤️ . Il vous reste {potions} potions et passez ce tour. ⏭️" + RESET)
               
            else:
                print_slow(YELLOW + "Vous n'avez plus de potions 🧪 ! Vous devez attaquer. ⚠️" + RESET)
                continue  # Si l'utilisateur n'a pas de potions, il doit attaquer    
                
        # Vérification de la santé de l'ennemi
        if enemy_health <= 0:
            separator()
            print_slow(BLINK + BOLD + GREEN + "Vous avez vaincu l'ennemi  ! 🎉 VICTORY ! 🎉" + RESET)
            separator()
            break

        # tour de l'ennemi
        enemy_attack_damage = random.randint(5, 15)
        player_health -= enemy_attack_damage
        print_slow(RED + f"L'ennemi vous attaque et vous inflige {enemy_attack_damage} points de dégâts. 💥" + RESET)

        # Vérification de la santé du joueur
        if player_health <= 0:
            separator()
            print_slow(BLINK + BOLD + RED + "Vous avez été vaincu par l'ennemi 👹 . Game Over. 😢" + RESET)
            print_slow(BLINK + BOLD + RED + "💀 GAME OVER 💀" + RESET)
            separator()
            break 
        # Affichage des points de vie restants  
        separator()
        print_slow(RED + f"Points de vie de l'ennemi 👹 : {enemy_health} {retro_hp_bar(enemy_health)}" + RESET)
        print_slow(GREEN + f"Vos points de vie : {player_health} {retro_hp_bar(player_health)}" + RESET)
        print_slow(YELLOW + f"Potions restantes : {potions}" + RESET)
        separator()  
        print("-" * 40)  # Ligne de séparation pour la lisibilité

    # On demande à l'utilisateur s'il veut effectuer une autre opération

    while True:
        oui = "oui"
        non = "non"
        reponse = input("Voulez-vous effectuer une autre partie ? 👾 (oui/non) : ")
        if reponse == oui:
            # Si l'utilisateur veut continuer, on relance le programme 
            print("Nouvelle partie ! 👾")
            break # On sort de la boucle pour revenir à la principale et recommencer le processus
        elif reponse == non:
            # Si l'utilisateur ne veut pas continuer, on quitte le programme
            print("Merci d'avoir joué !")
            print("Au revoir !")
            sys.exit()  # Quitte le programme
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
            continue

    
        