# VIẾT BẰNG PYTHON
# Tính thương hai số: Nhập hai số và in ra thương của chúng.

# Nhập hai số từ bàn phím
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

# Kiểm tra nếu b khác 0
if b != 0:
    # Tính thương của hai số
    T = a / b
    # In kết quả
    print("Thương của hai số là:", T)
else:
    print("Không thể chia cho 0.")
