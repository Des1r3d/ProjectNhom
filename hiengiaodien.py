import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from GUItest import Ui_MainWindow
from xuly import *


class MainWindow(QMainWindow, Ui_MainWindow):   # lấy thông tin của Qmainwindow và Ui_MainWindow nhập vào class MainWindow
    def __init__(self):         # Hàm khởi tạo để chạy chương trình
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Lấy các thuộc tính của ui, tạo ra ui
        self.push.clicked.connect(self.xu_ly) # liên kết nút lệnh vào hàm xử lý
    def xu_ly(self):   # Hàm xử lý khi nút lênh được bấm
        self.kq.setText(str(tungxucxac(socham)))


if __name__ == "__main__":   # Chạy chương trình với MainWindow
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()