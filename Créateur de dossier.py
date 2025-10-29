from pathlib import Path 
# Création de dossiers avec pathlib

# Chemin de base où les dossiers seront créés
chemin = r"C:\Users\charl\Desktop\formation_dev_python\projets\test"
# Dictionnaire contenant les dossiers à créer
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

# Création des dossiers
for dossier_principal, sous_dossiers in d.items():# itération sur les dossiers principaux
    for dossier in sous_dossiers: # itération sur les sous-dossiers
        # Création du chemin complet pour chaque sous-dossier
        chemin_dossier = Path(chemin) / dossier_principal / dossier # concaténation des chemins
        chemin_dossier.mkdir(exist_ok=True, parents=True) # création du dossier avec parents=True pour créer les dossiers parents si nécessaire