from PyQt5.QtWidgets import *
from view1 import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_Window_votemenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.votes_john=0
        self.votes_jane=0
        self.frame_votemenu.show()
        self.frame_cand_menu.hide()
        self.frame_results.hide()
        self.button_restart.hide()
        self.button_vote.clicked.connect(lambda: self.vote())
        self.button_submit.clicked.connect(lambda: self.choice())
        self.button_voteagain.clicked.connect(lambda: self.revote())
        self.button_viewresults.clicked.connect(lambda: self.results())
        self.button_restart.clicked.connect(lambda: self.restart())

    def vote(self):
        self.frame_cand_menu.show()
        self.frame_votemenu.hide()

    def choice(self):
        if self.radio_opt1.isChecked():
            self.votes_john += 1
            self.frame_results.show()
            self.frame_cand_menu.hide()
            self.label_votedname.setText('Voted John')
        elif self.radio_opt2.isChecked():
            self.votes_jane += 1
            self.frame_results.show()
            self.frame_cand_menu.hide()
            self.label_votedname.setText('Voted Jane')
            self.radio_opt2.nextCheckState()
        else:
            self.label_candmenu.setText('Please select a candidate')

    def revote(self):
        self.label_candmenu.setText('Candidate Menu')
        if self.radio_opt1.isChecked():
            self.radio_opt1.nextCheckState()
        if self.radio_opt2.isChecked():
            self.radio_opt2.nextCheckState()
        self.frame_cand_menu.show()
        self.frame_results.hide()

    def results(self):
        self.label_votedname.setText('')
        self.button_voteagain.hide()
        self.button_viewresults.hide()
        self.label_results.setGeometry(QtCore.QRect(100, 60, 301, 200))
        self.label_results.setText(f'John Smith = {self.votes_john}\nJane Reynolds = {self.votes_jane}')
        self.button_restart.show()

    def restart(self):
        self.frame_votemenu.show()
        self.frame_results.hide()
        self.button_restart.hide()
        self.button_voteagain.show()
        self.button_viewresults.show()
        self.label_results.setGeometry(QtCore.QRect(100, 60, 301, 31))
        self.label_results.setText('')
        self.label_votedname.setText('')
        if self.radio_opt1.isChecked():
            self.radio_opt1.nextCheckState()
        if self.radio_opt2.isChecked():
            self.radio_opt2.nextCheckState()
        self.votes_john = 0
        self.votes_jane = 0






