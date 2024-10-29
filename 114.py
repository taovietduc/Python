# VIẾT BẰNG PYTHON\
# Bài 114: Tạo hàm tính diện tích của một tam giác với ba cạnh cho trước.

import math # Import thư viện toán học math

def triangle_area(a, b, c): # Định nghĩa hàm triangle_area với 3 tham số a, b, c
    """
    Tính diện tích của một tam giác với ba cạnh cho trước.

    Parameters:
    a, b, c (float): Độ dài ba cạnh của tam giác.

    Returns:
    float: Diện tích của tam giác hoặc -1 nếu ba cạnh không tạo thành tam giác.
    """
    # Kiểm tra điều kiện tạo thành tam giác
    if a + b > c and a + c > b and b + c > a: # Tạo thành tam giác 
        s = (a + b + c) / 2  # Nửa chu vi
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Công thức Heron
        return area # Trả về diện tích tam giác 
    else: # Không tạo thành tam giác
        return -1  # Không tạo thành tam giác

# Ví dụ sử dụng
a, b, c = 3, 4, 5
area = triangle_area(a, b, c) # Gọi hàm triangle_area với 3 tham số a, b, c
if area != -1: # Kiểm tra điều kiện tạo thành tam giác
    print(f"Diện tích của tam giác là: {area}")
else: # Không tạo thành tam giác
    print("Ba cạnh không tạo thành tam giác.")
