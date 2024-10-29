# VIẾT BẰNG PYTHON
# Bài 84: Tạo hàm kiểm tra chuỗi có chứa toàn chữ số không.

def kiem_tra_toan_chu_so(chuoi): # Hàm kiểm tra chuỗi có chứa toàn chữ số không
    return chuoi.isdigit()  # Hàm isdigit() kiểm tra toàn chữ số

# Nhập chuỗi từ người dùng  
chuoi = input("Nhập chuỗi: ") # Nhập chuỗi từ người dùng

# Kiểm tra và in kết quả
if kiem_tra_toan_chu_so(chuoi): 
# Nếu chuỗi chứa toàn chữ số thì in ra "Chuỗi chứa toàn chữ số."
    print("Chuỗi chứa toàn chữ số.")    
else: # Ngược lại in ra "Chuỗi không chứa toàn chữ số."
    print("Chuỗi không chứa toàn chữ số.")
