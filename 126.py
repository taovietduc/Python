# VIẾT BẰNG PYTHON
# Bài 126: Tạo hàm chuyển đổi một chuỗi thành chữ in thường.

def to_lowercase(s): # Hàm chuyển chuỗi s thành chữ in thường
    return s.lower() # Hàm lower() sẽ chuyển chuỗi s thành chữ in thường

# Ví dụ sử dụng
s = "Hello, World!" # Chuỗi s
print("Chuỗi in thường là:", to_lowercase(s)) # In ra chuỗi in thường của chuỗi s
 
# Kết quả
# Chuỗi in thường là: hello, world!