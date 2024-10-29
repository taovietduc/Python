# VIẾT BẰNG PYTHON
# Bài 67: Tạo hàm tính tổng các số trong danh sách.

def tinh_tong_danh_sach(danh_sach): # Hàm tính tổng các số với tham số danh_sach
    return sum(danh_sach) # Trả về tổng các số trong danh sách

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số, cách nhau bằng dấu cách: ").split())) 
# Nhập danh sách các số từ bàn phím

# Tính tổng và in kết quả
tong = tinh_tong_danh_sach(danh_sach) # Gọi hàm và lưu kết quả vào biến
print("Tổng của các số trong danh sách là:", tong)  # In kết quả
 