# Organiser des données
from pprint import pprint

with open(r"C:\Users\charl\Desktop\formation_dev_python\projets\organiser des données\prenoms.txt", "r") as f: # ouvre le fichier en mode lecture
    lines = f.read().splitlines() # lit le contenu du fichier et le divise en lignes
# sépare les prénoms en une liste 
prenoms = []
for line in lines:
    prenoms.extend(line.split()) # ajoute chaque prénom à la liste  
# supprime les caractères indésirables et les espaces
prenoms_final = [prenom.strip(",. ") for prenom in prenoms]


with open(r"C:\Users\charl\Desktop\formation_dev_python\projets\organiser des données\prenoms_final.txt", "w") as f: # ouvre le fichier en mode écriture
    # écrit les prénoms triés dans le fichier
    f.write("\n".join(sorted(prenoms_final)))