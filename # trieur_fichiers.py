# trieur_fichiers.py
"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""
from pathlib import Path # Importation de la classe Path du module pathlib

# Dictionnaire qui associe les extensions de fichiers à des dossiers cibles
# Les clés sont les extensions de fichiers, les valeurs sont les noms des dossiers cibles
EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents"}

# Chemin absolu du dossier de base contenant les fichiers à trier
BASE_DIR = Path("C:/Users/charl/trieur fichiers")

# On récupère tous les fichiers dans le dossier de base
# On utilise iterdir() pour obtenir un générateur de fichiers
fichiers = [f for f in BASE_DIR.iterdir() if f.is_file()]
for fichier in fichiers:  # On boucle sur chaque fichier
    
    # On récupère le dossier cible à partir du dictionnaire extensions_mapping
    # Si l'extension n'est pas dans le dictionnaire, on utilise "Divers" comme valeur par défaut
    # On utilise la méthode get() pour éviter une KeyError si l'extension n'est pas trouvée
    dossier_cible = EXTENSIONS_MAPPING.get(fichier.suffix, "Divers")
    # On concatène le dossier de base avec le dossier cible
    dossier_cible_absolu = BASE_DIR / dossier_cible
    # On crée le dossier cible s'il n'existe pas déjà
    dossier_cible_absolu.mkdir(exist_ok=True)
    # On concatène le dossier cible avec le nom du fichier
    fichier_cible = dossier_cible_absolu / fichier.name
    # On déplace le fichier
    fichier.rename(fichier_cible)
# On affiche un message de confirmation
print("Tri des fichiers terminé.")