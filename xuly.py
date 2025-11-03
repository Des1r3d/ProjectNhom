# import hàm random từ python
import random


#tạo list gồm các mặt của số chấm
socham = [1, 2, 3, 4, 5, 6]
def tungxucxac(socham):
    #random số chạy từ index 0 đến index 5
    so= random.randint(0,5)
    #trả lại giá trị đã được random trong danh sách socham
    kq = socham[so]
    return kq

if __name__ == '__main__':
    print(tungxucxac(socham)) # Phần để kiểm tra lỗi phần mềm





