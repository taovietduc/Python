# VIẾT BẰNG PYTHON 
# Tạo danh sách từ từ điển: Nhập một từ điển và tạo danh sách các giá trị từ từ điển đó.

# Nhập từ điển từ người dùng
tu_dien = eval(input("Nhập từ điển (dưới dạng {'key': value, ...}): ")) # Nhập từ điển từ người dùng
# eval() hàm này thực thi một chuỗi được truyền vào và trả về giá trị của chuỗi đó

# Tạo danh sách các giá trị từ từ điển
danh_sach_gia_tri = list(tu_dien.values()) # Tạo danh sách các giá trị từ từ điển

# In danh sách các giá trị
print("Danh sách các giá trị từ từ điển là:", danh_sach_gia_tri) # In danh sách các giá trị
