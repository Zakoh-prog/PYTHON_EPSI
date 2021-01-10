from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
  
import sys 
  
  
class Window(QMainWindow): 
  
    def __init__(self): 
        super().__init__() 
  
        # Definition du titre
        self.setWindowTitle("Calculatrice ") 
  
        # Definition de la position et de la taille de la fenêtre
        self.setGeometry(100, 100, 360, 350) 
  
        # Appel de la fonction qui rempli la fenetre avec des widget
        self.UiComponents() 
  
        # Affichage de tout les widget de la fenetre 
        self.show() 
  
        # fonction qui rempli la fenetre avec des widget 
    def UiComponents(self): 
  
        # Creation d'un label 
        self.label = QLabel(self) 
  
        # Definition de la position et de la taille du label
        self.label.setGeometry(5, 5, 350, 70) 
  
        # Creation de lignes multiples sur le label 
        self.label.setWordWrap(True) 
  
        # Definition du style du label 
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "}") 
  
        # Definition de l'alignement du label 
        self.label.setAlignment(Qt.AlignRight) 
  
        # Definition de la police d'écriture à Comic Sans MS  (╯°□°)╯︵ ┻━┻
        self.label.setFont(QFont('Arial', 20))     
  
  
        # ajout des boutons représentants le pavé numérique 
        # creation d'un pushButton 
        pushb1 = QPushButton("1", self) 
  
        # Definition de la position et de la taille 
        pushb1.setGeometry(5, 150, 80, 40) 
  
        # creation d'un pushButton  
        pushb2 = QPushButton("2", self) 
  
        # Definition de la position et de la taille 
        pushb2.setGeometry(95, 150, 80, 40) 
  
        # creation d'un pushButton  
        pushb3 = QPushButton("3", self) 
  
        # Definition de la position et de la taille 
        pushb3.setGeometry(185, 150, 80, 40) 
  
        # creation d'un pushButton  
        pushb4 = QPushButton("4", self) 
  
        # Definition de la position et de la taille 
        pushb4.setGeometry(5, 200, 80, 40) 
  
        # creation d'un pushButton  
        pushb5 = QPushButton("5", self) 
  
        # Definition de la position et de la taille 
        pushb5.setGeometry(95, 200, 80, 40) 
  
        # creation d'un pushButton  
        pushb6 = QPushButton("5", self) 
  
        # Definition de la position et de la taille 
        pushb6.setGeometry(185, 200, 80, 40) 
  
        # creation d'un pushButton  
        pushb7 = QPushButton("7", self) 
  
        # Definition de la position et de la taille 
        pushb7.setGeometry(5, 250, 80, 40) 
  
        # creation d'un pushButton  
        pushb8 = QPushButton("8", self) 
  
        # Definition de la position et de la taille 
        pushb8.setGeometry(95, 250, 80, 40) 
  
        # creation d'un pushButton  
        pushb9 = QPushButton("9", self) 
  
        # Definition de la position et de la taille 
        pushb9.setGeometry(185, 250, 80, 40) 
  
        # creation d'un pushButton  
        pushb0 = QPushButton("0", self) 
  
        # Definition de la position et de la taille 
        pushb0.setGeometry(5, 300, 80, 40) 
  
        # adding operator push button 
        # creation d'un pushButton  
        pushb_equal = QPushButton("=", self) 
  
        # Definition de la position et de la taille 
        pushb_equal.setGeometry(275, 300, 80, 40) 
  
        # creation d'un pushButton  
        pushb_plus = QPushButton("+", self) 
  
        # Definition de la position et de la taille 
        pushb_plus.setGeometry(275, 250, 80, 40) 
  
        # creation d'un pushButton  
        pushb_minus = QPushButton("-", self) 
  
        # Definition de la position et de la taille 
        pushb_minus.setGeometry(275, 200, 80, 40) 
  
        # creation d'un pushButton  
        pushb_mul = QPushButton("*", self) 
  
        # Definition de la position et de la taille 
        pushb_mul.setGeometry(275, 150, 80, 40) 
  
        # creation d'un pushButton  
        pushb_div = QPushButton("/", self) 
  
        # Definition de la position et de la taille 
        pushb_div.setGeometry(185, 300, 80, 40) 
  
        # creation d'un pushButton  
        pushb_point = QPushButton(".", self) 
  
        # Definition de la position et de la taille 
        pushb_point.setGeometry(95, 300, 80, 40) 
  
  
        # Bouton clear 
        pushb_clear = QPushButton("Clear", self) 
        pushb_clear.setGeometry(5, 100, 170, 40) 
  
        # Bouton pour supprimer 1 
        pushb_del = QPushButton("Delete", self) 
        pushb_del.setGeometry(185, 100, 170, 40) 

        # ajout de couleurs à des pushbuttons 
        c_effect1 = QGraphicsColorizeEffect() 
        c_effect1.setColor(QColor(0, 150, 0)) 

        c_effect2 = QGraphicsColorizeEffect() 
        c_effect2.setColor(Qt.red)

        c_effect3 = QGraphicsColorizeEffect() 
        c_effect3.setColor(Qt.blue)

        pushb_equal.setGraphicsEffect(c_effect1) 
        pushb_del.setGraphicsEffect(c_effect2)
        pushb_clear.setGraphicsEffect(c_effect3)
  
        # ajout de sa fonction à chaque pushbutton 
        pushb_minus.clicked.connect(self.pbutton_minus) 
        pushb_equal.clicked.connect(self.pbutton_equal) 
        pushb0.clicked.connect(self.pbutton0) 
        pushb1.clicked.connect(self.pbutton1) 
        pushb2.clicked.connect(self.pbutton2) 
        pushb3.clicked.connect(self.pbutton3) 
        pushb4.clicked.connect(self.pbutton4) 
        pushb5.clicked.connect(self.pbutton5) 
        pushb6.clicked.connect(self.pbutton6) 
        pushb7.clicked.connect(self.pbutton7) 
        pushb8.clicked.connect(self.pbutton8) 
        pushb9.clicked.connect(self.pbutton9) 
        pushb_div.clicked.connect(self.pbutton_div) 
        pushb_mul.clicked.connect(self.pbutton_mul) 
        pushb_plus.clicked.connect(self.pbutton_plus) 
        pushb_point.clicked.connect(self.pbutton_point) 
        pushb_clear.clicked.connect(self.pbutton_clear) 
        pushb_del.clicked.connect(self.pbutton_del) 
  
  
    def pbutton_equal(self): 
  
        # recuperation du contenu du label 
        equation = self.label.text() 
  
        try: 
            # recupération de la solution 
            ans = eval(equation) 
  
            # ecriture de la solution dans le label 
            self.label.setText(str(ans)) 
  
        except: 
            # message d'erreur  
            QMessageBox.about(self, "Error", "/ ﹋ \\ \n(҂`_´)\n<, ︻╦╤─ ҉ - - - - - - - - (Error!)\n/ ﹋ \\ \n\n WRONG INPUT")
            
  
    def pbutton_plus(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + " + ") 
  
    def pbutton_minus(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + " - ") 
  
    def pbutton_div(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + " / ") 
  
    def pbutton_mul(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + " * ") 
  
    def pbutton_point(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + ".") 
  
    def pbutton0(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "0") 
  
    def pbutton1(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "1") 
  
    def pbutton2(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "2") 
  
    def pbutton3(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "3") 
  
    def pbutton4(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "4") 
  
    def pbutton5(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "5") 
  
    def pbutton6(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "6") 
  
    def pbutton7(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "7") 
  
    def pbutton8(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "8") 
  
    def pbutton9(self): 
        # mise à jour du label 
        text = self.label.text() 
        self.label.setText(text + "9") 
  
    def pbutton_clear(self): 
        # on vide le label 
        self.label.setText("") 
  
    def pbutton_del(self): 
        # retrait du dernier input 
        text = self.label.text() 
        print(text[:len(text)-1]) 
        self.label.setText(text[:len(text)-1]) 
  
  
App = QApplication(sys.argv) 
  
window = Window() 
  
sys.exit(App.exec()) 
