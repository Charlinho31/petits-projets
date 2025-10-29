import os
import json
import logging


CUR_DIR = os.path.dirname(__file__)
DATA_FILES = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies(): # Fonction pour lire les films depuis le fichier JSON
    with open(DATA_FILES, "r") as f:
        movies = json.load(f)
    
    movies = [movie for movie in movies]
    return movies

class Movie: # Classe représentant un film
    def __init__(self, title, director, year):
        self.title = title.title() # créer un attribut title avec la première lettre en majuscule
        self.director = director.title() # créer un attribut director avec la première lettre en majuscule
        self.year = year

    def __str__(self): # Méthode spéciale pour représenter l'objet sous forme de chaîne de caractères
        return f"{self.title} ({self.year}), réalisé par {self.director}"
    

    def _get_movies(self): # Lire les films depuis le fichier JSON
        with open(DATA_FILES, "r") as f:
            return json.load(f)
            
    # Écrire les informations du film (titre, année et directeur) dans le fichier JSON
    def write_movies(self, movies):
        with open(DATA_FILES, "w") as f:
            json.dump(movies, f, indent=4, ensure_ascii=False)
    
    def add_movie(self): # Ajouter un film au fichier JSON
        movies = self._get_movies() # Récupérer la liste des films existants
        
        if not any(
            movie["title"] == self.title and 
            movie["director"] == self.director and 
            movie["year"] == self.year 
            for movie in movies):
            
            movies.append({
            "title": self.title,
            "director": self.director,
            "year": self.year
        })
            self.write_movies(movies) # Écrire la liste mise à jour dans le fichier JSON
            return True
        else: 
            logging.warning(f"Le film {self.title} de {self.director} ({self.year}) existe déjà.")
            return False
 
    def remove_from_movies(self, mode="all"): # Supprimer un film du fichier JSON
        movies = self._get_movies() # Récupérer la liste des films existants
        if mode == "all": # Supprimer le film correspondant exactement au titre, réalisateur et année
            
            movies = [movie for movie in movies if not (
            movie["title"] == self.title and 
            movie["director"] == self.director and 
            movie["year"] == self.year 
        )]
            self.write_movies(movies) # Écrire la liste mise à jour dans le fichier JSON
        
        elif mode == "title": # Supprimer les films avec le même titre
            movies = [movie for movie in movies if movie["title"] != self.title] # Supprimer les films avec le même titre
            self.write_movies(movies) 
        
        elif mode == "director": # Supprimer les films avec le même réalisateur
            movies = [movie for movie in movies if movie["director"] != self.director] # Supprimer les films avec le même réalisateur
            self.write_movies(movies)
        
        elif mode == "year": # Supprimer les films de la même année
            movies = [movie for movie in movies if movie["year"] != self.year] # Supprimer les films de la même année
            self.write_movies(movies)  

        else:
            raise ValueError("Mode invalide. Utilisez 'all', 'title', 'director' ou 'year'.")

if __name__ == "__main__":
    # Exemple d'utilisation de la classe Movie
    m = Movie("The Grand Budapest Hotel", "Wes Anderson", 2014)
    m.remove_from_movies( mode="all")
       
