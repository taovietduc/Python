# VIẾT BẰNG PYTHON
# Bài 92: Tạo hàm sắp xếp chuỗi theo thứ tự bảng chữ cái.

# Hàm sắp xếp chuỗi theo thứ tự bảng chữ cái
def sap_xep_chuoi(chuoi): # chuoi = "abc" => chuoi = ['a', 'b', 'c'] => chuoi = "abc"
    return ''.join(sorted(chuoi)) # sắp xếp chuỗi và nối lại thành chuỗi mới

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ") # chuoi = "abc"

# Sắp xếp chuỗi và in kết quả
chuoi_sap_xep = sap_xep_chuoi(chuoi) # chuoi_sap_xep = "abc"
print(f"Chuỗi sau khi sắp xếp: {chuoi_sap_xep}") # Chuỗi sau khi sắp xếp: abc
