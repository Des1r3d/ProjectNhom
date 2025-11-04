import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from giaodien import Ui_MainWindow
from xuly import *


class MainWindow(QMainWindow, Ui_MainWindow):
    # Class MainWindow kế thừa cả thuộc tính QMainWindow và Ui_MainWindow
    def __init__(self):  # Hàm khởi tạo để thiết lập cửa sổ
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Lấy các thuộc tính của ui, tạo ra ui
        self.sodu = 1000  # Số dư ban đầu
        self.cuoctoithieu = 10  # Cược tối thiểu
        self.label_sodu_value.setText(f"{self.sodu:,.0f} $")
        # Cài đặt cho ô nhập tiền cược (SpinBox)
        self.spinBox_bet.setMinimum(self.cuoctoithieu)
        self.spinBox_bet.setMaximum(self.sodu)  # Cược tối đa là toàn bộ số dư
        self.spinBox_bet.setValue(self.cuoctoithieu)  # Đặt cược mặc định là cuoctoithieu
        self.push.clicked.connect(self.xu_ly)  # liên kết nút lệnh vào hàm xử lý
        self.kqtungxucxac.raise_()  # Nâng cac label kết quả lên trên cùng
        self.kqtungxucxac_2.raise_()  # Tránh việc mất kết quả do thuộc tính che mất
    def xu_ly(self):  # Hàm xử lý khi nút lênh được bấm
        # 1. Lấy số tiền cược từ spinBox
        tiencuoc = self.spinBox_bet.value()
        # 2. Gọi hàm logic xử lý từ file xuly.py
        ketqua = xu_ly_cuoc(self.sodu, tiencuoc, self.cuoctoithieu)
        # 3. Cập nhật số dư
        self.sodu = ketqua["sodu_moi"]
        # 4. Cập nhật giao diện dựa trên kết quả trả về
        self.label_message.setText(ketqua["message"])
        if ketqua["game_played"]:
            # Chỉ cập nhật xúc xắc và số dư nếu game đã diễn ra
            tungxucxac1, tungxucxac2 = ketqua["tungxucxac"]
            self.kqtungxucxac.setText(str(tungxucxac1))
            self.kqtungxucxac_2.setText(str(tungxucxac2))
            # Cập nhật lại số dư hiển thị
            self.label_sodu_value.setText(f"{self.sodu:,.0f} $")
            # Cập nhật mức cược tối đa mới
            # Đảm bảo max bet không bao giờ < min bet
            self.spinBox_bet.setMaximum(max(self.cuoctoithieu, self.sodu))
        # 5. Kiểm tra nếu phá sản thì vô hiệu hóa nút
        if ketqua["phasan"]:
            self.push.setEnabled(False)  # Vô hiệu hóa nút bấm
            self.spinBox_bet.setEnabled(False)  # Vô hiệu hóa ô cược


if __name__ == "__main__":  # Chạy chương trình khi được thực thi trực tiếp
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

