# VIẾT BẰNG PYTHON
# Tính số lượng chữ cái trong chuỗi: Nhập một chuỗi và đếm số lượng chữ cái trong chuỗi.

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập một chuỗi: ")

# Đếm số lượng chữ cái trong chuỗi
so_luong_chu_cai = 0
for ky_tu in chuoi:
    if ky_tu.isalpha():  # Kiểm tra nếu ký tự là chữ cái
        so_luong_chu_cai += 1 # Tăng biến đếm lên 1

# In kết quả
print(f"Số lượng chữ cái trong chuỗi là: {so_luong_chu_cai}")
