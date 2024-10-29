# VIẾT BẰNG PYTHON
# Bài 98: Tạo hàm kiểm tra một số có phải là số chính phương không.

import math # Import thư viện toán học math     

# Hàm kiểm tra số chính phương
def la_so_chinh_phuong(n): # Hàm kiểm tra số chính phương
    if n < 0: # Nếu n là số âm
        return False  # Số âm không thể là số chính phương
    sqrt_n = int(math.sqrt(n)) # Lấy căn bậc 2 của n và chuyển về kiểu số nguyên
    return sqrt_n * sqrt_n == n  # Kiểm tra nếu bình phương của sqrt_n bằng n

# Nhập một số
n = int(input("Nhập một số: ")) # Nhập một số nguyên

if la_so_chinh_phuong(n): # Nếu n là số chính phương
    print(f"{n} là số chính phương.")
else: # Nếu n không phải là số chính phương
    print(f"{n} không phải là số chính phương.")
