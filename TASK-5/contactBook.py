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
        uic.loadUi("contactBook.ui", self)
        
        
        self.setWindowTitle("Contact Book App")

        self.model = QStandardItemModel(0,2,self)
        self.model.setHorizontalHeaderLabels(["Name","Phone","Email","Address"])
        self.table.setModel(self.model)
        self.show()
        self.add_btn.clicked.connect(self.add_empty_row)
        self.search_box.setPlaceholderText(" Search")
        self.search_box.textChanged.connect(self.search)
        self.delete_btn.clicked.connect(self.delete)
    
    
    def delete(self):
        index = self.table.selectionModel().selectedIndexes()
        if index:
            selected_row = index[0].row()
            # print("hey")
            
            # print("hey")
            self.model.removeRow(selected_row)


    def search(self,text):
        if self.search_box.text():

            res = self.model.findItems(text,Qt.MatchContains)
            # print(res)
            if res:
                row = res[0].row()
                self.table.selectRow(row)
        else:
            self.table.clearSelection()



    def add_empty_row(self):
        row = [
            QStandardItem(""),
            QStandardItem(""),
            QStandardItem(""),
            QStandardItem("")
        ]
        self.model.appendRow(row)




def main():
    app = QApplication(sys.argv)
    window = contactGUI()
    app.exec()

if __name__ == '__main__':
    main()
