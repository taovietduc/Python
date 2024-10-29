# VIẾT BẰNG PYTHON
# Bai 103: Tạo hàm kiểm tra một danh sách có chứa phần tử trùng lặp hay không.

def kiem_tra_phan_tu_trung_lap(danh_sach): # Hàm kiểm tra phần tử trùng lặp
    # Sử dụng set để loại bỏ các phần tử trùng lặp
    if len(danh_sach) != len(set(danh_sach)): # So sánh độ dài danh sách với set của danh sách
        return True  # Danh sách có phần tử trùng lặp
    return False  # Danh sách không có phần tử trùng lặp

# Ví dụ sử dụng
danh_sach = [1, 2, 3, 4, 5, 2] # Danh sách có phần tử trùng lặp
if kiem_tra_phan_tu_trung_lap(danh_sach): # Gọi hàm kiểm tra phần tử trùng lặp
    print("Danh sách có chứa phần tử trùng lặp.")
else: # Danh sách không chứa phần tử trùng lặp
    print("Danh sách không chứa phần tử trùng lặp.")
