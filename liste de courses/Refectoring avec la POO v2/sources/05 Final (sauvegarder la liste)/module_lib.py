# Ce fichier est un module Python qui définit une classe Liste pour gérer une liste d'éléments.
# Il permet d'ajouter, de supprimer, d'afficher et de sauvegarder des éléments

import os # os est utilisé pour les opérations sur le système de fichiers
import json # json est utilisé pour la sérialisation et la désérialisation des données
import logging # logging is used for debugging and error messages

#mine module
from constants import DATA_DIR # DATA_DIR est le répertoire où les données seront sauvegardées

LOGGER = logging.getLogger() # faire un logger pour le module

class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter (self, element):
        """Ajoute un élément à la liste."""
        if not isinstance(element, str): # vérifie si l'élément est une chaîne de caractères
            raise ValueError("L'élément doit être une chaîne de caractères.")
        
        if element in self: # vérifie si l'élément n'est pas déjà dans la liste
            LOGGER.error(f"L'élément '{element}' est déjà dans la liste '{self.nom}'.")
            return False
        
        self.append(element) # ajoute l'élément à la liste
        LOGGER.info(f"L'élément '{element}' a été ajouté à la liste '{self.nom}'.")
        return True
    
    def supprimer(self, element): 
        """Supprime un élément de la liste."""
        if element in self:
            self.remove(element)  # supprime l'élément de la liste
            LOGGER.info(f"L'élément '{element}' a été supprimé de la liste '{self.nom}'.")
            return True
        return False
    
    def afficher(self):
        """Affiche les éléments de la liste."""
        print(f"Liste '{self.nom}':")
        for element in self:
            print(f" - {element}")

    def sauvegarder(self):
        """Sauvegarde la liste dans un fichier."""
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json") # chemin du fichier de sauvegarde
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        with open(chemin, 'w') as f: # ouvre le fichier en écriture
            json.dump(self, f, indent=4) # sauvegarde la liste au format JSON
        LOGGER.info(f"La liste '{self.nom}' a été sauvegardée dans '{chemin }'.")

if __name__ == "__main__":
    # Exemple d'utilisation de la classe Liste
    liste = Liste("Courses")
    liste.ajouter("Pommes") # Ajoute un élément
    liste.ajouter("Poires") # Ajoute un autre élément
    liste.afficher() # Affiche la liste
    liste.sauvegarder() # Sauvegarde la liste dans un fichier