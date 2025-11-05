# import hàm random từ python
import random

# tạo list gồm các mặt của số chấm
socham = [1, 2, 3, 4, 5, 6]
def tungxucxac(socham):
    # random số chạy từ index 0 đến index 5
    so = random.randint(0, 5)
    # trả lại giá trị đã được random trong danh sách socham
    kqtungxucxac = socham[so]
    return kqtungxucxac
def so_sanh(a, b):
    # Hàm này trả về True nếu a và b bằng nhau (số đôi), ngược lại trả về False
    return a == b
def xu_ly_cuoc(sodu_hientai, tiencuoc, cuoctoithieu):
    """
    Hàm xử lý logic cá cược.
    Nhận vào số dư, tiền cược, cược tối thiểu.
    Trả về một dictionary chứa kết quả.
    """
    # B1. Kiểm tra xem người chơi có đủ tiền cược không
    if tiencuoc > sodu_hientai:
        return {
            "sodu_moi": sodu_hientai,
            "message": "Nghèo quá bạn hiền",
            "tungxucxac": (None, None),  # Không tung xúc xắc
            "phasan": False,
            "game_played": False
        }
    # B2. Trừ tiền cược (cược trước)
    sodu_moi = sodu_hientai - tiencuoc
    # B3. Tung xúc xắc
    tungxucxac1 = tungxucxac(socham)
    tungxucxac2 = tungxucxac(socham)
    # B4. Kiểm tra thắng/thua
    gapdoi_tien = so_sanh(tungxucxac1, tungxucxac2)
    message = ""
    phasan = False
    if gapdoi_tien:
        # Thắng!
        chienthang = tiencuoc * 2  # Thắng x2 tiền cược
        sodu_moi += chienthang
        message = f"Xin chúc mừng, bạn đã lụm được {chienthang:,.0f} $"
    else:
        # Thua!
        message = f"Thật đáng tiếc, bạn đã bị lụm mất {tiencuoc:,.0f} $"
    # 5. hết tiền rầu
    if sodu_moi < cuoctoithieu:
        message = "Hết tiền mất rồi, hẹn bạn lần sau"
        phasan = True
    # 6. Trả về kết quả
    return {
        "sodu_moi": sodu_moi,
        "message": message,
        "tungxucxac": (tungxucxac1, tungxucxac2),
        "phasan": phasan,
        "game_played": True
    }
# Phần kiểm tra lỗi xử lý
if __name__ == '__main__':
    # Kiểm tra hàm xu_ly_cuoc
    sodu = 1000
    cuoctoithieu = 10
    # Test 1: Cược thắng
    print("Test 1: Cược thắng (giả lập)")
    # (Không thể giả lập thắng, nhưng ta test logic)
    ketqua = xu_ly_cuoc(sodu, 100, cuoctoithieu)
    print(ketqua)
    # Test 2: Cược không đủ tiền
    print("\nTest 2: Cược không đủ tiền")
    ketqua = xu_ly_cuoc(sodu, 2000, cuoctoithieu)
    print(ketqua)
    # Test 3: Cược phá sản
    print("\nTest 3: Cược phá sản (cược hết tiền và thua)")
    ketqua = xu_ly_cuoc(10, 10, cuoctoithieu)  # Giả sử cược 10 và thua
    if "thua" in ketqua["message"]:
        print(ketqua)
    else:
        print("Test phá sản (thắng, không phá sản):", ketqua)