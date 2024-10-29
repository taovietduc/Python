# VIẾT BẰNG PYTHON
# Bài 99: Tạo hàm kiểm tra một chuỗi có phải là chuỗi đảo ngược của chuỗi khác hay không.

# Hàm kiểm tra chuỗi thứ hai có phải là chuỗi đảo ngược của chuỗi thứ nhất không
def la_chuoi_dao_nguoc(str1, str2): # Truyền vào hai chuỗi cần kiểm tra
    if len(str1) != len(str2): # So sánh độ dài hai chuỗi
        return False  # Nếu độ dài hai chuỗi không bằng nhau, trả về False
    
    return str1 == str2[::-1]  # So sánh chuỗi thứ nhất với chuỗi thứ hai được đảo ngược

# Nhập chuỗi từ người dùng
str1 = input("Nhập chuỗi thứ nhất: ") # Nhập chuỗi thứ nhất từ bàn phím
str2 = input("Nhập chuỗi thứ hai: ") # Nhập chuỗi thứ hai từ bàn phím
if la_chuoi_dao_nguoc(str1, str2): # Gọi hàm kiểm tra chuỗi thứ hai có phải là chuỗi đảo ngược của chuỗi thứ nhất không
    print("Chuỗi thứ hai là chuỗi đảo ngược của chuỗi thứ nhất.")
else: # Nếu không phải chuỗi đảo ngược của nhau thì in ra thông báo   
    print("Chuỗi thứ hai không phải là chuỗi đảo ngược của chuỗi thứ nhất.")
