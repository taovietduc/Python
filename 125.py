# VIẾT BẰNG PYTHON
# Bài 125: Tạo hàm chuyển đổi một chuỗi thành chữ in hoa.

def to_uppercase(s): # s là chuỗi cần chuyển đổi thành chữ in hoa
    return s.upper() # hàm upper() sẽ chuyển đổi chuỗi s thành chữ in hoa

# Ví dụ sử dụng
s = "Hello, world!" # chuỗi cần chuyển đổi thành chữ in hoa
print("Chuỗi in hoa là:", to_uppercase(s)) 
# Kết quả: HELLO, WORLD!
