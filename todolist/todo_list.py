from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pickle
  
import sys 
  

class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        # Definition du titre
        self.setWindowTitle("To Do List") 

        # Definition de la position et de la taille de la fenêtre
        self.setGeometry(100, 100, 270, 460) 

        # Appel de la fonction qui rempli la fenetre avec des widget
        self.UiComponents()
        self.setStyleSheet("background:#141526;")
        
        # Affichage de tout les widget de la fenetre 
        self.show() 
    def UiComponents(self):
        
        self.listbox_tasks = QListWidget(self)
        self.load_tasks()
        
        self.listbox_tasks.setGeometry(5, 5, 260, 280)
        
        self.listbox_tasks.setStyleSheet("""
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:3px;
            margin: 0px 0px 0px 0px;
        }
        QListWidget{color:white;}
        QScrollBar::handle:vertical {
            background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
           
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218))
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218))
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        """)

        self.entry_task = QLineEdit(self)
        self.entry_task.setGeometry(5, 290, 260, 20)
        self.entry_task.setStyleSheet("border-radius:10;background:white;")

        self.button_add_task = QPushButton("ADD TASK", self) 
        self.button_add_task.setGeometry(5, 315, 260, 30)
        self.button_add_task.setStyleSheet("QPushButton{color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));border-style: solid;border-radius:15px;}") 


        self.button_delete_task=QPushButton("DELETE TASK", self)
        self.button_delete_task.setGeometry(5, 350, 260, 30)
        self.button_delete_task.setStyleSheet("QPushButton{color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));border-style: solid;border-radius:15px;}") 


        self.button_load_tasks=QPushButton("LOAD TASKS", self)
        self.button_load_tasks.setGeometry(5, 385, 260, 30)
        self.button_load_tasks.setStyleSheet("QPushButton{color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));border-radius:15;}") 


        self.button_save_tasks=QPushButton("SAVE TASKS", self)
        self.button_save_tasks.setGeometry(5, 420, 260, 30)
        self.button_save_tasks.setStyleSheet("QPushButton{color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));border-style: solid;border-radius:15px;}") 


        self.button_save_tasks.clicked.connect(self.save_tasks)
        self.button_add_task.clicked.connect(self.add_task)
        self.button_delete_task.clicked.connect(self.delete_task)
        self.button_load_tasks.clicked.connect(self.load_tasks)

    def add_task(self):
        task = self.entry_task.text()
        if task != "":
            self.listbox_tasks.addItem(task)
            self.entry_task.setText("")
           
        else:
            QMessageBox.about(self, "Error", "/ ﹋ \\ \n(҂`_´)\n<, ︻╦╤─ ҉ - - - - - - - - (Error!)\n/ ﹋ \\ \n\n WRONG INPUT")

    def delete_task(self):
        try:
            task_index = self.listbox_tasks.currentRow()
            self.listbox_tasks.takeItem(task_index)
        except:
            QMessageBox.about(self, "Error", "/ ﹋ \\ \n(҂`_´)\n<, ︻╦╤─ ҉ - - - - - - - - (Error!)\n/ ﹋ \\ \n\n ERROR")

    def load_tasks(self):
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            self.listbox_tasks.clear()
            for task in tasks:
                self.listbox_tasks.addItem(task)
        except:
            QMessageBox.about(self, "Error", "/ ﹋ \\ \n(҂`_´)\n<, ︻╦╤─ ҉ - - - - - - - - (Error!)\n/ ﹋ \\ \n\n Cannot find tasks.dat")

    def save_tasks(self):
        task = []
        for i in range(0,self.listbox_tasks.count()):
            task.append(self.listbox_tasks.item(i).text())
        test = tuple(task)
        pickle.dump(test, open("tasks.dat", "wb"))

    








App = QApplication(sys.argv) 
App.setWindowIcon(QtGui.QIcon('plume.png'))
  
window = Window() 
  
sys.exit(App.exec()) 