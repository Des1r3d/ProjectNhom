import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from giaodien import Ui_MainWindow
from xuly import tungxucxac, socham


class MainWindow(QMainWindow, Ui_MainWindow):   # Class MainWindow kế thừa cả thuộc tính QMainWindow và Ui_MainWindow
    def __init__(self):         # Hàm khởi tạo để thiết lập cửa sổ
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Lấy các thuộc tính của ui, tạo ra ui
        self.push.clicked.connect(self.xu_ly) # liên kết nút lệnh vào hàm xử lý
        self.kq.raise_()  # Nâng cac label kết quả lên trên cùng
        self.kq_2.raise_()  # Tránh việc mất kết quả do thuộc tính che mất
    def xu_ly(self):   # Hàm xử lý khi nút lênh được bấm
        self.kq.setText(str(tungxucxac(socham)))
        self.kq_2.setText(str(tungxucxac(socham)))


if __name__ == "__main__":   # Chạy chương trình khi được thực thi trực tiếp
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
