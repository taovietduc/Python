# VIẾT BẰNG PYTHON
# Tìm số nhỏ nhất trong ba số

# Nhập ba số từ người dùng
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

# Tìm số nhỏ nhất
so_nho_nhat = min(a, b, c)

# In kết quả
print("Số nhỏ nhất là:", so_nho_nhat)

# VIẾT BẰNG PYTHON
# Tìm số nhỏ nhất trong ba số (Cách 2)

# Nhập ba số từ ban phím
list = []
for i in range(3):
    so = float(input(f"Nhập số thứ {i + 1}: "))
    so_list.append(so)

# Tìm số nhỏ nhất
so_nho_nhat = list[0]
for so in list:
    if so < so_nho_nhat:
        so_nho_nhat = so

# In kết quả
print("Số nhỏ nhất là:", so_nho_nhat)
