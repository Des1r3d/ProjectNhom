# import hàm random từ python
import random

# tạo list gồm các mặt của số chấm
socham = [1, 2, 3, 4, 5, 6]
def tungxucxac(socham):
    # random số chạy từ index 0 đến index 5
    so = random.randint(0, 5)
    # trả lại giá trị đã được random trong danh sách socham
    kq = socham[so]
    return kq
def so_sanh(a, b):
    # Hàm này trả về True nếu a và b bằng nhau (số đôi), ngược lại trả về False
    return a == b
def xu_ly_cuoc(current_balance, bet_amount, min_bet):
    """
    Hàm xử lý logic cá cược.
    Nhận vào số dư, tiền cược, cược tối thiểu.
    Trả về một dictionary chứa kết quả.
    """
    # B1. Kiểm tra xem người chơi có đủ tiền cược không
    if bet_amount > current_balance:
        return {
            "new_balance": current_balance,
            "message": "Không đủ tiền cược! Vui lòng cược ít hơn.",
            "rolls": (None, None),  # Không tung xúc xắc
            "is_bankrupt": False,
            "game_played": False
        }
    # B2. Trừ tiền cược (cược trước)
    new_balance = current_balance - bet_amount
    # B3. Tung xúc xắc
    roll_1 = tungxucxac(socham)
    roll_2 = tungxucxac(socham)
    # B4. Kiểm tra thắng/thua
    is_double = so_sanh(roll_1, roll_2)
    message = ""
    is_bankrupt = False

    if is_double:
        # Thắng!
        winnings = bet_amount * 2  # Thắng x2 tiền cược
        new_balance += winnings
        message = f" Bạn thắng {winnings:,.0f} $ (Đôi {roll_1})"
    else:
        # Thua!
        message = f"Bạn thua {bet_amount:,.0f} $"

    # 5. Kiểm tra phá sản
    if new_balance < min_bet:
        message = "HẾT TIỀN! Bạn đã phá sản."
        is_bankrupt = True

    # 6. Trả về kết quả
    return {
        "new_balance": new_balance,
        "message": message,
        "rolls": (roll_1, roll_2),
        "is_bankrupt": is_bankrupt,
        "game_played": True
    }


# Phần kiểm tra lỗi phần mềm
if __name__ == '__main__':
    # Kiểm tra hàm xu_ly_cuoc
    balance = 1000
    min_bet = 10
    # Test 1: Cược thắng
    print("Test 1: Cược thắng (giả lập)")
    # (Không thể giả lập thắng, nhưng ta test logic)
    result = xu_ly_cuoc(balance, 100, min_bet)
    print(result)
    # Test 2: Cược không đủ tiền
    print("\nTest 2: Cược không đủ tiền")
    result = xu_ly_cuoc(balance, 2000, min_bet)
    print(result)
    # Test 3: Cược phá sản
    print("\nTest 3: Cược phá sản (cược hết tiền và thua)")
    result = xu_ly_cuoc(10, 10, min_bet)  # Giả sử cược 10 và thua
    if "thua" in result["message"]:
        print(result)
    else:
        print("Test phá sản (thắng, không phá sản):", result)

