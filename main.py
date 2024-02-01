import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class main_interface(QDialog):
    def __init__(self):
        super(main_interface, self).__init__()
        uic.loadUi("main.ui", self)
        
        calendar_win = calendar_interface()
        budget_win = budget_interface()
#        tm_win = tm_interface()
        
        self.widget = QStackedWidget()
        self.widget.addWidget(self)
        self.widget.addWidget(calendar_win)
        self.widget.addWidget(budget_win)
#        self.widget.addWidget(tm_win)
        self.widget.show()
        
        self.calendar_btn.clicked.connect(self.spawn_calendar)
        self.budget_btn.clicked.connect(self.spawn_budget)
    #    self.tm_btn.clicked.connect(self.spawn_tm)

    def spawn_calendar(self):
        self.widget.setCurrentIndex(1)

    def spawn_budget(self):
        self.widget.setCurrentIndex(2)
    
    #def spawn_tm(self):
    #    self.widget.setCurrentIndex(3)

class calendar_interface(QDialog):
    def __init__(self):
        super(calendar_interface, self).__init__()
        uic.loadUi("calendar.ui", self)


class budget_interface(QDialog):
    def __init__(self):
        super(budget_interface, self).__init__()
        uic.loadUi("budget.ui", self)
        #self.show()

#class tm_interface(QDialog):
#    def __init__(self):
#        super(tm_interface, self).__init__()
#        uic.loadUi("tm.ui", self)
        #self.show()
        
def main():
    app = QApplication(sys.argv)
    main_window =  main_interface()

    app.exec()


if __name__ == "__main__":
    main()