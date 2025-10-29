from PySide6 import QtWidgets #appel a la bibliothèque QtWidgets de PySide6
import currency_converter # importation du module currency_converter

class App(QtWidgets.QWidget): # Création d'une classe App qui hérite de QtWidgets.QWidget
    def __init__(self): # Méthode d'initialisation de la classe
        super().__init__()
        self.c = currency_converter.CurrencyConverter() # Création d'une instance de CurrencyConverter
        self.setWindowTitle("Convertisseur de devises") # Définition du titre de la fenêtre
        self.setup_ui() # Appel de la méthode pour configurer l'interface utilisateur
        self.set_defaults_values() # Appel de la méthode pour définir les valeurs par défaut
        self.setup_connections() # Appel de la méthode pour configurer les connexions des signaux et slots
        self.setup_css() # Appel de la méthode pour configurer le style CSS en sombre


    def setup_ui(self): # Méthode pour configurer l'interface utilisateur 
        self.layout = QtWidgets.QHBoxLayout(self) # type: ignore # Création d'un layout horizontal 
        self.cbb_devisesFrom = QtWidgets.QComboBox() # Création d'une combo box pour les devises de départ
        self.spn_montant = QtWidgets.QSpinBox() # Création d'un spin box pour le montant
        self.cbb_devisesTo = QtWidgets.QComboBox() # Création d'une combo box pour les devises d'arrivée
        self.spn_montantConverti = QtWidgets.QSpinBox() # Création d'un spin box pour le montant converti
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises") # Création d'un bouton pour inverser les devises

        # Ajout des widgets au layout
        self.layout.addWidget(self.cbb_devisesFrom)  # type: ignore
        self.layout.addWidget(self.spn_montant)  # type: ignore
        self.layout.addWidget(self.cbb_devisesTo)  # type: ignore
        self.layout.addWidget(self.spn_montantConverti)  # type: ignore
        self.layout.addWidget(self.btn_inverser)  # type: ignore

    def set_defaults_values(self): # Méthode pour définir les valeurs par défaut
        devises = sorted(list(self.c.currencies)) # type: ignore # Récupération et tri des devises disponibles
        self.cbb_devisesFrom.addItems(devises) # Ajout des devises à la combo box de départ
        self.cbb_devisesTo.addItems(devises) # Ajout des devises à la combo box d'arrivée
        self.cbb_devisesFrom.setCurrentText("EUR") # Définition de la devise de départ par défaut
        self.cbb_devisesTo.setCurrentText("USD") # Définition de la devise d'arrivée par défaut
       
        self.spn_montant.setRange(0, 1000000) # Définition de la plage du spin box montant
        self.spn_montantConverti.setRange(0, 1000000) # Définition de la plage du spin box montant converti
        
        self.spn_montant.setValue(100) # Définition de la valeur par défaut du spin box montant
        self.spn_montantConverti.setValue(100) # Définition de la valeur par défaut du spin box montant converti       

    def setup_connections(self): # Méthode pour configurer les connexions des signaux et slots
        self.cbb_devisesFrom.activated.connect(self.compute) # Connexion de la sélection de la devise de départ à la méthode de calcul
        self.cbb_devisesTo.activated.connect(self.compute) # Connexion de la sélection de la devise d'arrivée à la méthode de calcul
        self.spn_montant.valueChanged.connect(self.compute) # Connexion du changement de valeur du montant à la méthode de calcul
        self.btn_inverser.clicked.connect(self.inverser_devises) # Connexion du clic du bouton à la méthode d'inversion des devises

    def setup_css(self): # Méthode pour configurer le style CSS en sombre
        self.setStyleSheet("""
        background-color: black;
        color: white;
        font-size: 20px;
        """)

    def compute(self): # Méthode pour effectuer la conversion de devises
        montant = self.spn_montant.value() # Récupération du montant à convertir
        devise_from = self.cbb_devisesFrom.currentText() # Récupération de la devise de départ
        devise_to = self.cbb_devisesTo.currentText() # Récupération de la devise d'arrivée
        
        try:
            resultat = self.c.convert(montant, devise_from, devise_to) # Conversion du montant
        except currency_converter.currency_converter.RateNotFoundError:
            print("Taux de conversion non trouvé pour les devises sélectionnées.")
        else:
            self.spn_montantConverti.setValue(resultat) # type: ignore # Mise à jour du spin box du montant converti
    
    def inverser_devises(self): # Méthode pour inverser les devises sélectionnées
        devise_from = self.cbb_devisesFrom.currentText() 
        devise_to = self.cbb_devisesTo.currentText() 

        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)
        self.compute() # Recalculer après inversion

app = QtWidgets.QApplication([]) # Création d'une instance de QApplication
win = App() # Création d'une instance de la classe App
win.show() # Affichage de la fenêtre principale
app.exec_() # Démarrage de la boucle d'événements de l'application
