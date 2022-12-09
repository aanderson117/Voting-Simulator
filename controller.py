from PyQt5.QtWidgets import *
from screen1 import *
from screen2 import *
from screen3 import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_Window_votemenu, Ui_Window_candmenu, Ui_Window_resultmenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.votes_john=0
        self.votes_jane=0
        self.button_vote.clicked.connect(lambda: self.vote())

    def screen2(self):
        self.window_candmenu = QtWidgets.QMainWindow()
        self.ui = Ui_Window_candmenu()
        self.ui.setupUi(self.window_candmenu)
        self.window_candmenu.show()
        ###FIXME: close vote menu when opening candidate menu###

    def screen3(self):
        self.window_resultmenu = QtWidgets.QMainWindow()
        self.ui = Ui_Window_resultmenu()
        self.ui.setupUi(self.window_resultmenu)
        self.window_resultmenu.show()
        ###FIXME: close cand menu when opening result menu###

    def vote(self):
        self.screen2()

    def choice(self):
        if self.radio_opt1.isChecked():
            self.votes_john += 1
        elif self.radio_opt2.isChecked():
            self.votes_jane += 1


