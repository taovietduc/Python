# VIẾT BẰNG PYTHON
# Bài 118: Tạo hàm kiểm tra một chuỗi có chứa khoảng trắng hay không.

def contains_whitespace(string): # Hàm kiểm tra chuỗi có chứa khoảng trắng hay không
    for char in string: # Duyệt qua từng ký tự trong chuỗi
        if char.isspace():  # Kiểm tra nếu ký tự là khoảng trắng
            return True # Trả về True nếu có ký tự khoảng trắng
    return False # Trả về False nếu không có ký tự khoảng trắng

# Ví dụ sử dụng
string = "Hello World" # Chuỗi cần kiểm tra
if contains_whitespace(string): # Kiểm tra chuỗi có chứa khoảng trắng hay không
    print("Chuỗi chứa khoảng trắng.")
else: # Nếu chuỗi không chứa khoảng trắng thì in ra thông báo sau đây
    print("Chuỗi không chứa khoảng trắng.")
