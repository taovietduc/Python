# VIẾT BẰNG PYTHON
# Bài 117: Tạo hàm kiểm tra một chuỗi có chứa ký tự số hay không.

def contains_digit(string): # Hàm kiểm tra chuỗi có chứa ký tự số hay không
    for char in string: # Duyệt từng ký tự trong chuỗi string 
        if char.isdigit():  # Kiểm tra nếu ký tự là số
            return True # Trả về True nếu có ký tự số trong chuỗi
    return False # Trả về False nếu không có ký tự số trong chuỗi

# Ví dụ sử dụng
string = "Hello123" # Chuỗi cần kiểm tra có chứa ký tự số hay không
if contains_digit(string): # Kiểm tra chuỗi có chứa ký tự số hay không
    print("Chuỗi chứa ký tự số.")   
else: # Nếu chuỗi không chứa ký tự số 
    print("Chuỗi không chứa ký tự số.")
