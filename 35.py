# VIẾT BẰNG PYTHON 
# Đếm số lần xuất hiện của số trong danh sách: Nhập một danh sách và một số, đếm số lần xuất hiện của số trong danh sách.

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split())) 
# split() để tách các số cách nhau bởi dấu cách và map() để chuyển các số thành kiểu int

# Nhập số cần tìm
so_can_tim = int(input("Nhập số cần đếm: ")) 
# Chuyển số cần tìm thành kiểu int để so sánh với các số trong danh sách

# Đếm số lần xuất hiện của số cần tìm
so_lan_xuat_hien = danh_sach.count(so_can_tim) 
# Hàm count() trả về số lần xuất hiện của phần tử trong danh sách

# In kết quả
print(f"Số {so_can_tim} xuất hiện {so_lan_xuat_hien} lần trong danh sách.")
