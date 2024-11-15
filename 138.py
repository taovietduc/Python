# VIẾT BẰNG PYTHON
# Bài 138: Tạo hàm tính diện tích hình elip.

import math

def ellipse_area(a, b): # a: bán trục lớn, b: bán trục nhỏ 
    return math.pi * a * b # Diện tích hình elip = π * a * b

# Ví dụ sử dụng
a = 5 # bán trục lớn
b = 3 # bán trục nhỏ
print(f"Diện tích hình elip với bán trục lớn {a} và bán trục nhỏ {b} là:", ellipse_area(a, b)) 

# Kết quả: 47.12388980384689 
