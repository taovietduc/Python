# VIẾT BẰNG PYTHON
# Bài 93: Tạo hàm kiểm tra số nguyên tố trong một khoảng cho trước.

import math

# Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n): # Hàm kiểm tra số nguyên tố
    if n <= 1: # Số nhỏ hơn hoặc bằng 1 không phải số nguyên tố
        return False  # Số nhỏ hơn hoặc bằng 1 không phải số nguyên tố
    for i in range(2, int(math.sqrt(n)) + 1): # Duyệt từ 2 đến căn bậc 2 của n
        if n % i == 0: # Nếu n chia hết cho i thì n không phải số nguyên tố
            return False # Nếu n chia hết cho i thì n không phải số nguyên tố
    return True # Nếu không có số nào chia hết n thì n là số nguyên tố

# Hàm kiểm tra các số nguyên tố trong một khoảng cho trước
def nguyen_to_trong_khoang(start, end): # Hàm kiểm tra các số nguyên tố trong một khoảng cho trước
    print(f"Các số nguyên tố từ {start} đến {end} là: ", end="") 
    for i in range(start, end + 1): # Duyệt từ start đến end
        if kiem_tra_nguyen_to(i): # Nếu i là số nguyên tố
            print(i, end=" ")
    print()

# Nhập khoảng từ người dùng
start = int(input("Nhập khoảng bắt đầu: ")) # Nhập khoảng bắt đầu
end = int(input("Nhập khoảng kết thúc: ")) # Nhập khoảng kết thúc
 
nguyen_to_trong_khoang(start, end) # Gọi hàm kiểm tra các số nguyên tố trong một khoảng cho trước

# Kết quả
# Nhập khoảng bắt đầu: 1
# Nhập khoảng kết thúc: 9
# Các số nguyên tố từ 1 đến 9 là: 2 3 5 7 