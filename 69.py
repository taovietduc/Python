# VIẾT BẰNG PYTHON
# Bài 69: Tạo hàm tìm số nhỏ nhất trong danh sách.

def tim_so_nho_nhat(danh_sach): # Hàm tìm số nhỏ nhất với tham số danh_sach
    return min(danh_sach) # Trả về số nhỏ nhất trong danh sách

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số, cách nhau bằng dấu cách: ").split())) 
# Nhập danh sách các số từ bàn phím 

# Tìm số nhỏ nhất và in kết quả
so_nho_nhat = tim_so_nho_nhat(danh_sach) # Gọi hàm và lưu kết quả vào biến
print("Số nhỏ nhất trong danh sách là:", so_nho_nhat) # In kết quả
