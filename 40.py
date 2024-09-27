# VIẾT BẰNG PYTHON 
# Tính tổng các giá trị trong từ điển: Nhập một từ điển với các giá trị số và tính tổng của chúng.

# Nhập từ điển từ người dùng
tu_dien = eval(input("Nhập từ điển với các giá trị là số (dưới dạng {'key': value, ...}): ")) 
# Sử dụng hàm eval() để chuyển chuỗi nhập vào thành từ điển

# Tính tổng các giá trị trong từ điển
tong = sum(tu_dien.values()) # Sử dụng hàm sum() để tính tổng các giá trị trong từ điển

# In tổng các giá trị
print("Tổng các giá trị trong từ điển là:", tong)
