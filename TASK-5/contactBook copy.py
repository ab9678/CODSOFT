import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class contactGUI(QMainWindow):

    
    expression = ""
    finalExpression=""
    
    def __init__(self):
        super(contactGUI, self).__init__()
        uic.loadUi("contactBook3.ui", self)
        
        
        self.setWindowTitle("Contact Book App")

       
        self.show()
        


def main():
    app = QApplication(sys.argv)
    window = contactGUI()
    app.exec()

if __name__ == '__main__':
    main()
