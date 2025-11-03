import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from giaodien import Ui_MainWindow
# Import logic xử lý, bao gồm hàm mới
from xuly import xu_ly_cuoc


class MainWindow(QMainWindow, Ui_MainWindow):
    # Class MainWindow kế thừa cả thuộc tính QMainWindow và Ui_MainWindow
    def __init__(self):  # Hàm khởi tạo để thiết lập cửa sổ
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Lấy các thuộc tính của ui, tạo ra ui
        self.balance = 1000  # Số dư ban đầu
        self.min_bet = 10  # Cược tối thiểu
        self.label_balance_value.setText(f"{self.balance:,.0f} $")
        # Cài đặt cho ô nhập tiền cược (SpinBox)
        self.spinBox_bet.setMinimum(self.min_bet)
        self.spinBox_bet.setMaximum(self.balance)  # Cược tối đa là toàn bộ số dư
        self.spinBox_bet.setValue(self.min_bet)  # Đặt cược mặc định là min_bet
        self.push.clicked.connect(self.xu_ly)  # liên kết nút lệnh vào hàm xử lý
        self.kq.raise_()  # Nâng cac label kết quả lên trên cùng
        self.kq_2.raise_()  # Tránh việc mất kết quả do thuộc tính che mất
    def xu_ly(self):  # Hàm xử lý khi nút lênh được bấm
        # 1. Lấy số tiền cược từ spinBox
        bet_amount = self.spinBox_bet.value()
        # 2. Gọi hàm logic xử lý từ file xuly.py
        result = xu_ly_cuoc(self.balance, bet_amount, self.min_bet)
        # 3. Cập nhật số dư
        self.balance = result["new_balance"]
        # 4. Cập nhật giao diện dựa trên kết quả trả về
        self.label_message.setText(result["message"])
        if result["game_played"]:
            # Chỉ cập nhật xúc xắc và số dư nếu game đã diễn ra
            roll_1, roll_2 = result["rolls"]
            self.kq.setText(str(roll_1))
            self.kq_2.setText(str(roll_2))
            # Cập nhật lại số dư hiển thị
            self.label_balance_value.setText(f"{self.balance:,.0f} $")
            # Cập nhật mức cược tối đa mới
            # Đảm bảo max bet không bao giờ < min bet
            self.spinBox_bet.setMaximum(max(self.min_bet, self.balance))
        # 5. Kiểm tra nếu phá sản thì vô hiệu hóa nút
        if result["is_bankrupt"]:
            self.push.setEnabled(False)  # Vô hiệu hóa nút bấm
            self.spinBox_bet.setEnabled(False)  # Vô hiệu hóa ô cược


if __name__ == "__main__":  # Chạy chương trình khi được thực thi trực tiếp
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

