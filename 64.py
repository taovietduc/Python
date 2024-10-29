# VIẾT BẰNG PYTHON
# Bài 64: Tạo hàm đảo ngược chuỗi.

def dao_nguoc_chuoi(chuoi): # Hàm đảo ngược chuỗi với tham số chuỗi
    return chuoi[::-1] # Trả về chuỗi đảo ngược

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi cần đảo ngược: ") # Nhập chuỗi từ bàn phím

# Đảo ngược chuỗi và in ra kết quả
chuoi_dao_nguoc = dao_nguoc_chuoi(chuoi) # Gọi hàm và lưu kết quả vào biến
print("Chuỗi sau khi đảo ngược:", chuoi_dao_nguoc) # In kết quả
