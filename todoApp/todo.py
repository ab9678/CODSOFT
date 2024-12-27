import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from rapidfuzz import fuzz
from rapidfuzz import process

'''
    here I am using set data and other stuff but we can do the same thing in another way

    If I take the lineEdit.text() alter the string with a number i+1, and then add it to the listView and also to the tasks[].
    That way we can directly compare the listView's data to task[] because its essentially the same data. But problem is that why the numberings wont chang eafter removing the widgets, we would have to re-update the task list and put numbers in the task list, its doable ofc. So there are two ways it can be done, that I have found.
    tl;dr :)

'''


class todogui(QMainWindow):
    task=""
    tasks=[]
    res=[]
    mode = "normal"
    
    def __init__(self):
        super(todogui, self).__init__()
        uic.loadUi("todoFinal.ui", self)
        self.show()
        # set placeholder text in Input
        self.update_task.setDisabled(True)
        self.remove_task.setDisabled(True)
        self.task_input.setPlaceholderText("Create a task")
        self.search_box.setPlaceholderText("Search")
        self.search_box.setDisabled(True)
        self.search_box.textChanged.connect(self.search)

        self.add_task.clicked.connect(self.return_add_pressed_handle)
        self.task_input.returnPressed.connect(self.return_add_pressed_handle)
        self.remove_task.clicked.connect(self.remove)
        self.update_task.clicked.connect(self.update_button)
        self.setWindowTitle("Todo list")

    def search(self):
        pass
    

    def return_add_pressed_handle(self):
        if self.mode == "normal":
            self.add()
        elif self.mode == "edit":
            self.put_new_task()
    
    def update_button(self):
        try:
            self.task = self.task_list.currentItem().data(Qt.UserRole) 
            print(self.task)
            if not self.task:
                pass
            else: 
                self.mode = "edit"
                self.task_input.setText(self.task)
                print("update_button")
                # self.task_input.returnPressed.connect(self.put_new_task)
        except AttributeError:
            pass
        
    def put_new_task(self):
        try:
            print("put new task")
            newTask=self.task_input.text()     
            print(newTask)
            print(self.task)         
            for i in range (len(self.tasks)):
                if self.tasks[i] == self.task:
                    print(self.tasks)
                    self.tasks[i]=newTask   # this is where the task list is changed Now I neeed to output this data with numbers along with other items
                    print(i)
                    print(self.tasks)

                    break
            self.update_list()
            self.task_input.clear()
            self.mode = "normal"    
        except (AttributeError, ValueError, MemoryError):
            pass
            
    def disable_widget(self):
        if not self.task_list.count():
            self.update_task.setDisabled(True)
            self.remove_task.setDisabled(True)
            self.search_box.setDisabled(True)
        else:
            self.update_task.setEnabled(True)
            self.remove_task.setEnabled(True)     
            self.search_box.setEnabled(True)       

    def add(self):
        input = self.task_input.text()
        if not input.strip() or input in self.tasks:
            pass
        else:
            self.tasks.append(input)
            self.update_task.setEnabled(True)
            self.remove_task.setEnabled(True)
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

        self.disable_widget()
        '''
            Qt.UserRole is a constant that stores custom data, here we are storing the self.tasks[i] to the item and when we retreive that data, if we try to access the data using Qt.UserRole it will find the custom data attached to that item. It is like a database which stores hidden data to the data diplayed to the user.
            # we are displaying numbers before the tasks to the user, but the real list doesnt have numbers so what we are doing is we take that data, addItem with that modified data, then set the real data to the real item in the taskslist, now when we getch that data with widget.selecteditems() we can now pass it to data(Qt.UserRole), UserRole stored the real data, so it will fetch the real data (raw data), which we can then compare to the tasksList easily, because his data is available to the tasks list
        '''

    def remove(self):
        try:
            rawTask = self.task_list.selectedItems()[0].data(Qt.UserRole)   
            '''
                we can also use .currentItem() to do the same ething but the difference is selectedItems track all the items selected (thats why [0] is used because I am going for one item at a time) whereas currentItem supports only selection of the one item
                tl;dr
            '''
            
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
