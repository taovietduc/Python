# VIẾT BẰNG PYTHON
# Tính chu vi, diện tích hình tròn: Nhập bán kính và in ra chu vi, diện tích hình tròn.

import math

# Nhập bán kính từ bàn phím
r = float(input("Nhập bán kính của hình tròn: "))

# Kiểm tra điều kiện bán kính > 0
if r > 0:
    # Tính chu vi hình tròn
    C = 2 * math.pi * r
    # Tính diện tích hình tròn
    S = math.pi * r ** 2
    # In kết quả
    print("Chu vi của hình tròn là:", C)
    print("Diện tích của hình tròn là:", S)
else:
    print("Bán kính phải lớn hơn 0.")
