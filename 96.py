# VIẾT BẰNG PYTHON
# Bài 96: Tạo hàm kiểm tra chuỗi có phải là chuỗi con của một chuỗi khác hay không.

# Hàm kiểm tra chuỗi con
def la_chuoi_con(chuoi_cha, chuoi_con): # chuoi_cha là chuỗi cha, chuoi_con là chuỗi con
    # Sử dụng toán tử 'in' để kiểm tra chuỗi con
    return chuoi_con in chuoi_cha 
    # Trả về True nếu chuỗi con tồn tại trong chuỗi cha, ngược lại trả về False

# Nhập chuỗi từ bàn phím
chuoi_cha = input("Nhập chuỗi cha: ") # Nhập chuỗi cha
chuoi_con = input("Nhập chuỗi con: ") # Nhập chuỗi con

# Kiểm tra và in kết quả
if la_chuoi_con(chuoi_cha, chuoi_con): # Gọi hàm và kiểm tra kết quả
    print(f"Chuỗi con '{chuoi_con}' có tồn tại trong chuỗi cha.")
else: # Nếu kết quả là False
    print(f"Chuỗi con '{chuoi_con}' không tồn tại trong chuỗi cha.")
