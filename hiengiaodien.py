import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from GUItest import Ui_MainWindow
from xuly import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btngieo.clicked.connect(self.xu_ly)
    def xu_ly(self):
        self.lnketqua.setText(str(tungxucxac(socham)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()