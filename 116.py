# VIẾT BẰNG PYTHON
# Bài 116: Tạo hàm chuyển đổi từ radian sang độ.

import math

def radians_to_degrees(radian): # Hàm chuyển đổi từ radian sang độ 
    return radian * (180 / math.pi) # Công thức chuyển đổi từ radian sang độ

# Ví dụ sử dụng
radian = math.pi # radian = 180 độ 
degree = radians_to_degrees(radian) # Chuyển đổi từ radian sang độ 
print(f"{radian} radian bằng {degree} độ") # In kết quả 
