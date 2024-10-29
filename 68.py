# VIẾT BẰNG PYTHON
# Bài 68: Tạo hàm tìm số lớn nhất trong danh sách.

def tim_so_lon_nhat(danh_sach): # Hàm tìm số lớn nhất với tham số danh_sach 
    return max(danh_sach) # Trả về số lớn nhất trong danh sách

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số, cách nhau bằng dấu cách: ").split())) 
# Nhập danh sách các số từ bàn phím  

# Tìm số lớn nhất và in kết quả
so_lon_nhat = tim_so_lon_nhat(danh_sach) # Gọi hàm và lưu kết quả vào biến
print("Số lớn nhất trong danh sách là:", so_lon_nhat) # In kết quả
