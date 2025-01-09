import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt


class calcGUI(QMainWindow):

    
    expression = ""
    finalExpression=""
    
    def __init__(self):
        super(calcGUI, self).__init__()
        uic.loadUi("calc.ui", self)
        
        self.show()
        self.setWindowTitle("Calculator")
        
        # set property for each button
        self.btn0.setProperty("data","0")   # data = 0      ,property.("data")
        self.btn1.setProperty("data","1")
        self.btn2.setProperty("data","2")
        self.btn3.setProperty("data","3")
        self.btn4.setProperty("data","4")
        self.btn5.setProperty("data","5")
        self.btn6.setProperty("data","6")
        self.btn7.setProperty("data","7")
        self.btn8.setProperty("data","8")
        self.btn9.setProperty("data","9")
        self.btnDivide.setProperty("data","/")
        # self.btnEquals.setProperty("data","1")
        self.btnMinus.setProperty("data","-")
        self.btnMultiply.setProperty("data","*")
        self.btnPlus.setProperty("data","+")
        self.btnPoint.setProperty("data",".")
        self.btnPercentage.setProperty("data","%")
        # self.clearbtn.setProperty("data","1")
        self.leftBracket.setProperty("data","(")
        self.rightBracket.setProperty("data",")")
        
        # set the function for each button
        self.btn0.clicked.connect(self.handle_button)
        self.btn1.clicked.connect(self.handle_button)
        self.btn2.clicked.connect(self.handle_button)
        self.btn3.clicked.connect(self.handle_button)
        self.btn4.clicked.connect(self.handle_button)
        self.btn5.clicked.connect(self.handle_button)
        self.btn6.clicked.connect(self.handle_button)
        self.btn7.clicked.connect(self.handle_button)
        self.btn8.clicked.connect(self.handle_button)
        self.btn9.clicked.connect(self.handle_button)
        self.btnDivide.clicked.connect(self.handle_button)
        self.btnEquals.clicked.connect(self.handle_equals_btn)
        self.btnMinus.clicked.connect(self.handle_button)
        self.btnMultiply.clicked.connect(self.handle_button)
        self.btnPlus.clicked.connect(self.handle_button)
        self.btnPoint.clicked.connect(self.handle_button)
        self.btnPercentage.clicked.connect(self.handle_button)
        self.clearbtn.clicked.connect(self.clear_input)
        self.leftBracket.clicked.connect(self.handle_button)
        self.rightBracket.clicked.connect(self.handle_button)

        # if enter is pressed
        self.inputBox.returnPressed.connect(self.handle_equals_btn)
        
        # data = self.btn1.property("data")
        # print(data)

    def handle_button(self):
        sender = self.sender()
        # print(f"button clicked: {sender.property("data")}")
        self.expression = self.inputBox.text().strip() # update the expression in case user typed something afterwards
        self.expression = self.expression+sender.property("data")
        # print(self.expression)
        self.inputBox.setText(self.expression)

        
    def handle_equals_btn(self):

        self.finalExpression = self.inputBox.text().strip()
        if not self.finalExpression:
            pass
        else:

            try:
                res = eval(self.finalExpression)
                self.outputBox.setText(str(res))
                self.update_input()
            except (ValueError , ZeroDivisionError, TypeError):
                self.outputBox.setText("error")
    def clear_input(self):
        self.finalExpression = ""
        self.expression = ""
        self.outputBox.clear()
        self.update_input()
    def update_input(self):
        self.inputBox.setText(self.finalExpression)

def main():
    app = QApplication(sys.argv)
    window = calcGUI()
    
    app.exec()


if __name__ == '__main__':
    main()
