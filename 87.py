# VIẾT BẰNG PYTHON
# Bài 87: Tạo hàm đếm số phần tử dương trong danh sách.

# Hàm đếm số phần tử dương trong danh sách
def dem_so_duong(danh_sach): # Truyền vào 1 danh sách   
    dem = 0
    for phan_tu in danh_sach: # Duyệt từng phần tử trong danh sách 
        if phan_tu > 0:  # Kiểm tra nếu phần tử lớn hơn 0
            dem += 1 # Tăng biến đếm lên 1 đơn vị
    return dem

# Nhập danh sách từ người dùng
danh_sach = list(map(int, input("Nhập các phần tử của danh sách (cách nhau bởi dấu cách): ").split())) 
#.split() tách chuỗi thành list các phần tử cách nhau bởi dấu cách và map(int, list) chuyển các phần tử trong list thành kiểu int

# Đếm số phần tử dương
so_phan_tu_duong = dem_so_duong(danh_sach) # Gọi hàm và truyền vào danh sách cần đếm

# In kết quả
print("Số lượng phần tử dương trong danh sách là:", so_phan_tu_duong) # In ra số lượng phần tử dương trong danh sách
