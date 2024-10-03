# VIẾT BẰNG PYTHON
# Bài 54: Kiểm tra chuỗi có chứa ký tự đặc biệt không

import re # Import thư viện re (regular expression) để sử dụng biểu thức chính quy 

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập chuỗi: ") 

# Sử dụng biểu thức chính quy để kiểm tra ký tự đặc biệt
# Ký tự đặc biệt là những ký tự không phải chữ cái và số
if re.search(r'[^a-zA-Z0-9]', chuoi): 
    # Nếu chuỗi có chứa ký tự đặc biệt thì in ra "Chuỗi có chứa ký tự đặc biệt."
    print("Chuỗi có chứa ký tự đặc biệt.")
else: # Ngược lại in ra "Chuỗi không chứa ký tự đặc biệt."
    print("Chuỗi không chứa ký tự đặc biệt.")
