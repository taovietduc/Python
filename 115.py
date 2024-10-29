# VIẾT BẰNG PYTHON
# Bài 115: Tạo hàm chuyển đổi từ độ sang radian.

import math # Import thư viện math để sử dụng hàm pi

def degrees_to_radians(degree): 
    """
    Chuyển đổi từ độ sang radian.

    Parameters:
    degree (float): Góc tính bằng độ.

    Returns:
    float: Góc tính bằng radian.
    """
    return degree * (math.pi / 180) # Công thức chuyển đổi từ độ sang radian

# Ví dụ sử dụng
degree = 180
radian = degrees_to_radians(degree) # Gọi hàm chuyển đổi từ độ sang radian
print(f"{degree} độ bằng {radian} radian") # In kết quả     
