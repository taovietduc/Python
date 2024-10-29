# VIẾT BẰNG PYTHON
# Bài 66: Tạo hàm đếm số lượng ký tự 'a' trong chuỗi.

def dem_ky_tu_a(chuoi): # Hàm đếm số lượng ký tự 'a' với tham số chuỗi
    # Sử dụng phương thức count() để đếm số lượng ký tự 'a'
    return chuoi.count('a') # Trả về số lượng ký tự 'a'

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ") # Nhập chuỗi từ bàn phím

# Đếm số lượng ký tự 'a' và in ra kết quả
so_luong_a = dem_ky_tu_a(chuoi) # Gọi hàm và lưu kết quả vào biến
print("Số lượng ký tự 'a' trong chuỗi:", so_luong_a) # In kết quả
