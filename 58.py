# VIẾT BẰNG PYTHON
# Bài 58: Tạo hàm tính diện tích hình chữ nhật.

# Hàm tính diện tích hình chữ nhật
def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong): 
# chieu_dai, chieu_rong là tham số truyền vào hàm
    return chieu_dai * chieu_rong 
    # Trả về diện tích hình chữ nhật

# Nhập chiều dài và chiều rộng từ người dùng
chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: ")) 
# Ép kiểu dữ liệu về float để có thể nhận số thực
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))

# Tính và in kết quả
dien_tich = tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong) 
# Gọi hàm và truyền tham số vào hàm 
print(f"Diện tích của hình chữ nhật là: {dien_tich}") # In kết quả
