# VIẾT BẰNG PYTHON
# Bài 109: Tạo hàm tính khoảng cách giữa hai điểm trên mặt phẳng tọa độ.

import math

def distance_between_points(x1, y1, x2, y2): # Hàm distance_between_points
    # Tính khoảng cách giữa hai điểm (x1, y1) và (x2, y2) trên mặt phẳng tọa độ.

    # Parameters:
    # x1 (float): Tọa độ x của điểm thứ nhất.
    # y1 (float): Tọa độ y của điểm thứ nhất.
    # x2 (float): Tọa độ x của điểm thứ hai.
    # y2 (float): Tọa độ y của điểm thứ hai.

    # Returns:
    # float: Khoảng cách giữa hai điểm.
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Tính khoảng cách giữa hai điểm
    return distance # Trả về kết quả

# Ví dụ sử dụng
point1 = (1, 2) # Điểm thứ nhất
point2 = (4, 6) # Điểm thứ hai
distance = distance_between_points(point1[0], point1[1], point2[0], point2[1]) # Tính khoảng cách giữa hai điểm
print(f"Khoảng cách giữa hai điểm {point1} và {point2} là: {distance}") # In kết quả
