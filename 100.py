# VIẾT BẰNG PYTHON
# Bài 100: Tạo hàm kiểm tra một chuỗi có chứa chữ cái in hoa hay không.

# Hàm kiểm tra chuỗi có chứa chữ cái in hoa hay không
def chua_chu_in_hoa(s): # s là chuỗi cần kiểm tra chứa chữ cái in hoa hay không
    for char in s: # Duyệt từng ký tự trong chuỗi
        if char.isupper():  # Kiểm tra ký tự có phải là chữ cái in hoa
            return True # Nếu có thì trả về True
    return False # Nếu không thì trả về False

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ") # Nhập chuỗi từ người dùng

if chua_chu_in_hoa(chuoi): # Kiểm tra chuỗi có chứa chữ cái in hoa hay không
    print("Chuỗi có chứa chữ cái in hoa.")
else: # Nếu không chứa chữ cái in hoa thì in ra thông báo
    print("Chuỗi không chứa chữ cái in hoa.")
