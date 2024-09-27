# VIẾT BẰNG PYTHON 
# Thêm phần tử vào từ điển: Nhập một từ điển và thêm một phần tử mới vào từ điển.

# Nhập từ điển từ người dùng
tu_dien = eval(input("Nhập từ điển (dưới dạng {'key': 'value', ...}): ")) 
# eval() để chuyển chuỗi thành từ điển

# Nhập khóa và giá trị mới
khoa_moi = input("Nhập khóa mới: ") # Nhập khóa mới
gia_tri_moi = input("Nhập giá trị mới: ") # Nhập giá trị mới

# Thêm phần tử mới vào từ điển
tu_dien[khoa_moi] = gia_tri_moi # Thêm phần tử mới vào từ điển

# In từ điển sau khi thêm phần tử mới
print("Từ điển sau khi thêm phần tử mới:")
print(tu_dien)
