# VIẾT BẰNG PYTHON
# Bài 65: Tạo hàm đếm số lượng từ trong chuỗi.

def dem_so_luong_tu(chuoi): # Hàm đếm số lượng từ với tham số chuỗi
    # Sử dụng hàm split để tách chuỗi thành danh sách từ
    tu = chuoi.split() # Tách chuỗi thành danh sách từ
    return len(tu) # Trả về số lượng từ

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ") # Nhập chuỗi từ bàn phím

# Đếm số lượng từ và in ra kết quả
so_luong_tu = dem_so_luong_tu(chuoi) # Gọi hàm và lưu kết quả vào biến
print("Số lượng từ trong chuỗi:", so_luong_tu) # In kết quả
