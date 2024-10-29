# VIẾT BẰNG PYTHON
# Bài 82: Tạo hàm tìm ước chung lớn nhất của hai số.

def ucln(a, b): # Hàm tìm ước chung lớn nhất của 2 số
    while b != 0: # Sử dụng thuật toán Euclid
        a, b = b, a % b # Đổi chỗ a và b, a = b, b = a % b
    return a # Trả về a

# Kiểm tra
a = int(input("Nhập số thứ nhất: ")) # Nhập số thứ nhất
b = int(input("Nhập số thứ hai: ")) # Nhập số thứ hai
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln(a, b)}") # In ra kết quả
