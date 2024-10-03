# VIẾT BẰNG PYTHON 
# Kiểm tra phần tử có trong danh sách: Nhập một danh sách và một phần tử, kiểm tra xem phần tử đó có trong danh sách không.

# Nhập danh sách các phần tử từ người dùng
danh_sach = input("Nhập danh sách các phần tử (phân tách bằng dấu phẩy): ").split(",") 
# Nhập danh sách các phần tử từ người dùng và tách chúng bằng dấu phẩy

# Nhập phần tử cần kiểm tra
phan_tu = input("Nhập phần tử cần kiểm tra: ") # Nhập phần tử cần kiểm tra từ bàn phím

# Kiểm tra xem phần tử có trong danh sách không
if phan_tu in danh_sach: # Nếu phần tử có trong danh sách 
    print(f"Phần tử '{phan_tu}' có trong danh sách.") 
else:
    print(f"Phần tử '{phan_tu}' không có trong danh sách.")
