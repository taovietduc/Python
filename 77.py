# VIẾT BẰNG PYTHON
# Bài 77: Tạo hàm kiểm tra phần tử có trong danh sách.

def kiem_tra_phan_tu(danh_sach, phan_tu): # Hàm kiểm tra phần tử có trong danh sách
    return phan_tu in danh_sach # Trả về True nếu phần tử có trong danh sách, ngược lại trả về False

# Danh sách mẫu
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# Phần tử cần kiểm tra
phan_tu = 5 # Phần tử cần kiểm tra có trong danh sách

# Gọi hàm kiểm tra phần tử
if kiem_tra_phan_tu(danh_sach, phan_tu): # Nếu phần tử có trong danh sách
    print(f"{phan_tu} có trong danh sách.") 
else: # Nếu phần tử không có trong danh sách    
    print(f"{phan_tu} không có trong danh sách.")
