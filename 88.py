# VIẾT BẰNG PYTHON
# Bài 88: Tạo hàm kiểm tra hai danh sách có giống nhau không.

# Hàm kiểm tra hai danh sách có giống nhau không
def kiem_tra_danh_sach_giong_nhau(danh_sach1, danh_sach2):
    return danh_sach1 == danh_sach2  # So sánh trực tiếp hai danh sách

# Nhập danh sách thứ nhất từ người dùng
danh_sach1 = list(map(int, input("Nhập các phần tử của danh sách thứ nhất (cách nhau bởi dấu cách): ").split()))

# Nhập danh sách thứ hai từ người dùng
danh_sach2 = list(map(int, input("Nhập các phần tử của danh sách thứ hai (cách nhau bởi dấu cách): ").split()))

# Kiểm tra hai danh sách có giống nhau không
if kiem_tra_danh_sach_giong_nhau(danh_sach1, danh_sach2): # Gọi hàm kiem_tra_danh_sach_giong_nhau để kiểm tra hai danh sách
    print("Hai danh sách giống nhau.") # In ra màn hình hai danh sách giống nhau
else:   # Ngược lại hai danh sách không giống nhau
    print("Hai danh sách không giống nhau.") 
