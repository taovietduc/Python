# VIẾT BẰNG PYTHON
# Bài 91: Tạo hàm tìm số lần xuất hiện của một phần tử trong danh sách.

# Hàm tìm số lần xuất hiện của một phần tử trong danh sách
def dem_so_lan_xuat_hien(danh_sach, phan_tu): # danh_sach: list, phan_tu: int -> int 
    return danh_sach.count(phan_tu) # Trả về số lần xuất hiện của phần tử trong danh sách

# Nhập danh sách từ người dùng
danh_sach = list(map(int, input("Nhập các phần tử của danh sách (cách nhau bởi dấu cách): ").split())) 
# .split() để tách các phần tử cách nhau bởi dấu cách và chuyển thành list

# Nhập phần tử cần tìm
phan_tu = int(input("Nhập phần tử cần tìm: "))  # Nhập phần tử cần tìm 

# Tìm và in số lần xuất hiện của phần tử
so_lan_xuat_hien = dem_so_lan_xuat_hien(danh_sach, phan_tu) # Gọi hàm tìm số lần xuất hiện của phần tử
print(f"Phần tử {phan_tu} xuất hiện {so_lan_xuat_hien} lần.") # In kết quả
