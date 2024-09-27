# VIẾT BẰNG PYTHON 
# Xóa phần tử khỏi từ điển: Nhập một từ điển và xóa một phần tử khỏi từ điển.

# Nhập từ điển từ người dùng
tu_dien = eval(input("Nhập từ điển (dưới dạng {'key': 'value', ...}): "))

# In từ điển trước khi xóa
print("Từ điển hiện tại:", tu_dien)

# Nhập khóa của phần tử cần xóa
khoa_can_xoa = input("Nhập khóa cần xóa: ") # Nhập khóa cần xóa

# Kiểm tra nếu khóa tồn tại trong từ điển và xóa

if khoa_can_xoa in tu_dien: # Kiểm tra khóa có tồn tại trong từ điển không
    del tu_dien[khoa_can_xoa] # Xóa phần tử có khóa 'khoa_can_xoa' khỏi từ điển
    print(f"Đã xóa phần tử có khóa '{khoa_can_xoa}'") # Thông báo xóa thành công
else: # Nếu khóa không tồn tại trong từ điển
    print(f"Không tìm thấy khóa '{khoa_can_xoa}' trong từ điển") # Thông báo không tìm thấy khóa

# In từ điển sau khi xóa
print("Từ điển sau khi xóa:", tu_dien)

