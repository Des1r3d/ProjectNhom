import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodien import *
from xuly import *
from xuly import socham
class MainWindow():
        def __init__(self):
            self.main_win=QWidget()
            self.ui=Ui_Form()
            self.ui.setupUi(self.main_win)
            self.lienketnutlenh()
            self.main_win.show()
        def lienketnutlenh(self):
            self.ui.pbtgieo.clicked.connect(self.xulinoibo)
        def xulinoibo(self):
            ketqua=tungxucxac(socham)
            self.ui.lneketqua.setText(ketqua)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()