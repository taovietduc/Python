# VIẾT BẰNG PYTHON
# Bài 75: Tạo hàm tạo danh sách các số chẵn từ danh sách.

def loc_so_chan(danh_sach): # Hàm lọc số chẵn từ danh sách các số nguyên danh_sach
    # Dùng list comprehension để lọc các số chẵn
    danh_sach_chan = [x for x in danh_sach if x % 2 == 0] 
    # Lọc số chẵn từ danh sách và lưu vào danh_sach_chan
    return danh_sach_chan # Trả về danh sách các số chẵn 

# Danh sách mẫu
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Danh sách các số nguyên

# Gọi hàm lọc số chẵn
danh_sach_chan = loc_so_chan(danh_sach) # Lọc số chẵn từ danh sách

# In kết quả
print("Danh sách các số chẵn là:", danh_sach_chan) # In danh sách các số chẵn 
