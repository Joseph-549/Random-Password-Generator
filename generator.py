import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import random
from password import mainPassword


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(100,100, 800,500)
        self.arayuz()
    

    def arayuz(self):
        self.text = QLabel("Password", self)
        self.text.move(5,30)

        self.button = QPushButton("Click for Password", self)
        self.button.clicked.connect(self.buttonFunction)	
        
        self.show()
        
    
    def buttonFunction(self):
        self.text.setText(mainPassword())

    
    

uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())








