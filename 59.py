# VIẾT BẰNG PYTHON
# Bài 59: Tạo hàm tính diện tích hình tròn.

import math

# Hàm tính diện tích hình tròn
def tinh_dien_tich_hinh_tron(ban_kinh): # ban_kinh là tham số truyền vào hàm
    return math.pi * (ban_kinh ** 2) # Trả về diện tích hình tròn

# Nhập bán kính từ người dùng
ban_kinh = float(input("Nhập bán kính của hình tròn: ")) 
# Ép kiểu dữ liệu về float để có thể nhận số thực

# Tính và in kết quả diện tích hình tròn
dien_tich = tinh_dien_tich_hinh_tron(ban_kinh) 
# Gọi hàm và truyền tham số vào hàm
print(f"Diện tích của hình tròn là: {dien_tich:.2f}") # In kết quả

# Kết quả:
# Nhập bán kính của hình tròn: 4
# Diện tích của hình tròn là: 50.27