# VIẾT BẰNG PYTHON
# Kiểm tra số nguyên tố: Nhập một số và kiểm tra xem nó có phải là số nguyên tố không.

# Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số từ bàn phím
n = int(input("Nhập một số: "))

# Kiểm tra và in kết quả
if kiem_tra_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
