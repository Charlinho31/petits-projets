from PySide6 import QtCore, QtWidgets
from movie import get_movies, Movie
import logging

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        #self.le_movieTitle = QtWidgets.QLineEdit() 

        # Champs pour ajouter un film
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.le_title = QtWidgets.QLineEdit()
        self.le_title.setPlaceholderText("Titre du film")
        self.le_director = QtWidgets.QLineEdit()
        self.le_director.setPlaceholderText("Réalisateur")
        self.le_year = QtWidgets.QLineEdit()
        self.le_year.setPlaceholderText("Année de sortie")

        # Liste pour afficher les films
        self.lw_movies = QtWidgets.QListWidget() 
        self.lw_movies.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection) # type: ignore

        self.btn_removeMovie = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        # Ajouter les widgets au layout
        #self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.le_title)
        self.main_layout.addWidget(self.le_director)
        self.main_layout.addWidget(self.le_year)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovie)
    
    def setup_connections(self): # Connecter les signaux aux slots
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.le_title.returnPressed.connect(self.add_movie)
        self.btn_removeMovie.clicked.connect(self.remove_movie)
        #self.le_title.returnPressed.connect(self.remove_movie)
        #self.le_director.returnPressed.connect(self.remove_movie)
        #self.le_year.returnPressed.connect(self.remove_movie)


    def populate_movies(self):
        """Remplit la QListWidget avec les films du JSON"""
        self.lw_movies.clear()
        movies = get_movies()

        for movie in movies:
            item_text = f"{movie['title']} ({movie['year']}), de {movie['director']}"
            lw_item = QtWidgets.QListWidgetItem(item_text)


            lw_item.setData(QtCore.Qt.UserRole, { # type: ignore
                "title": str(movie["title"]),
                "director": str(movie["director"]),
                "year": int(movie["year"]) if str(movie["year"]).isdigit() else 0
            }) 
            self.lw_movies.addItem(lw_item)
        
    def add_movie(self):
        title = self.le_title.text().strip()
        director = self.le_director.text().strip()
        year_text = self.le_year.text().strip()

        if not title or not director or not year_text:
            logging.warning("Veuillez remplir tous les champs.")
            return

        try:
            year = int(year_text)
        except ValueError:
            logging.warning("L'année doit être un nombre.")
            return
        
        movie = Movie(title=title, director=director, year=year)
        if movie.add_movie():
            lw_item = QtWidgets.QListWidgetItem(f"{movie.title} ({movie.year}), de {movie.director}")
            lw_item.setData(QtCore.Qt.UserRole, { # type: ignore
                "title": movie.title,
                "director": movie.director,
                "year": movie.year
            })
            self.lw_movies.addItem(lw_item)

            # Effacer les champs après ajout
            self.le_title.clear()
            self.le_director.clear()
            self.le_year.clear()

            print(f"Film ajouté : {movie}")
        else:
            logging.warning(f"Le film {movie.title} de {movie.director} ({movie.year}) existe déjà.")

    def remove_movie(self):
        selected_items = self.lw_movies.selectedItems()
        removed_count = 0

        # --- Suppression par sélection ---
        if selected_items:
            for item in selected_items:
                movie_data = item.data(QtCore.Qt.UserRole) # type: ignore
                temp_movie = Movie(
                    title=movie_data["title"],
                    director=movie_data["director"],
                    year=movie_data["year"]
                )
                if temp_movie.remove_from_movies(mode="all"):
                    removed_count += 1
                # Collecter les films à supprimer de la QListWidget
                    self.lw_movies.takeItem(self.lw_movies.row(item))
        
        # --- Suppression via champs de recherche ---
        else:
            title_text = self.le_title.text().strip()
            director_text = self.le_director.text().strip()
            year_text = self.le_year.text().strip()

            for i in reversed(range(self.lw_movies.count())):
                item = self.lw_movies.item(i)
                movie_data = item.data(QtCore.Qt.UserRole) # type: ignore
                temp_movie = Movie(
                    title=movie_data["title"],
                    director=movie_data["director"],
                    year=movie_data["year"]
                )
                delete = False

            # Mode "all" : tous les champs remplis doivent correspondre
                if ((not title_text or movie_data["title"] == title_text) and
                    (not director_text or movie_data["director"] == director_text) and
                    (not year_text or str(movie_data["year"]) == year_text)):
                    delete = True

                if delete:
                    # Supprime selon les champs remplis
                    if title_text:
                        temp_movie.remove_from_movies(mode="title")
                    if director_text:
                        temp_movie.remove_from_movies(mode="director")
                    if title_text and director_text and year_text:
                        temp_movie.remove_from_movies(mode="all")

                    self.lw_movies.takeItem(i)
                    removed_count += 1

            
        print(f"{removed_count} film(s) supprimé(s)")


app = QtWidgets.QApplication([])
window = App()
window.show()
app.exec()