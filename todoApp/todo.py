import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

class todogui(QMainWindow):

    tasks=[]
    res=[]
    def __init__(self):
        super(todogui, self).__init__()
        uic.loadUi("todo2.ui", self)
        self.show()

        self.add_task.clicked.connect(self.add)
        self.task_input.returnPressed.connect(self.add)
        self.remove_task.clicked.connect(self.remove)
        self.setWindowTitle("Todo list")

    def add(self):
        input = self.task_input.text()
        if not input.strip() or input in self.tasks:
            pass
        else:
            self.tasks.append(input)
        
        self.update_list()
        self.task_input.clear()
    def update_list(self):  
        self.task_list.clear()
        
        # Add each task as an item in the list widget
        for i in range(len(self.tasks)):
            j=i
            data = f"{str(j+1)}. {self.tasks[i]}"
            item = QListWidgetItem(data)
            item.setData(Qt.UserRole, self.tasks[i])   # sets a data for what is actually visible to the user, lets say user sees 1. car wash, set data does is, it sets the real data to what was actually in the tasks list
            self.task_list.addItem(item)

        # Qt.UserRole is a constant that stores custom data, here we are storing the self.tasks[i] to the item and when we retreive that data, if we try to access the data using Qt.UserRole it will find the custom data attached to that item. It is like a database which stores hidden data to the data diplayed to the user.
        # we are displaying numbers before the tasks to the user, but the real list doesnt have numbers so what we are doing is we take that data, addItem with that modified data, then set the real data to the real item in the taskslist, now when we getch that data with widget.selecteditems() we can now pass it to data(Qt.UserRole), UserRole stored the real data, so it will fetch the real data (raw data), which we can then compare to the tasksList easily, because his data is available to the tasks list

    def remove(self):
        try:
            rawTask = self.task_list.selectedItems()[0].data(Qt.UserRole)
            # rawTask = item.data(Qt.UserRole)    # raw task is the real tasks list's item
            # print(rawTask)
            for i in range(len(self.tasks)):
                if self.tasks[i]==rawTask:
                    self.tasks.pop(i)
                    break
                
            # print(self.tasks)
            self.update_list()

        except IndexError:
            pass
        
        # print(text)
        # print(text[3:])

        
def main():
    app = QApplication(sys.argv)
    window = todogui()
    app.exec()

if __name__ == '__main__':
    main()
