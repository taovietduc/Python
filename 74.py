# VIẾT BẰNG PYTHON
# Bài 74: Tạo hàm lọc danh sách theo điều kiện.

# Hàm lọc danh sách theo điều kiện
def loc_danh_sach(danh_sach, dieu_kien): # Hàm lọc danh sách theo điều kiện
    return [x for x in danh_sach if dieu_kien(x)]  # Lọc các phần tử thỏa mãn điều kiện

# Điều kiện lọc (ví dụ: lọc số chẵn)
def la_so_chan(x): # Hàm trả về True nếu x là số chẵn, ngược lại trả về False
    return x % 2 == 0 # Trả về True nếu x là số chẵn, ngược lại trả về False

# Tạo danh sách mẫu
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Danh sách mẫu

# Lọc danh sách theo điều kiện là số chẵn
danh_sach_loc = loc_danh_sach(danh_sach, la_so_chan) # Lọc danh sách theo điều kiện là số chẵn
print("Danh sách các số chẵn là:", danh_sach_loc) # In danh sách các số chẵn
