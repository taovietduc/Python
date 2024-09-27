# VIẾT BẰNG PYTHON
# Tìm số nhỏ nhất trong danh sách: Nhập một danh sách các số và tìm số nhỏ nhất trong danh sách.

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split())) 
# map() chuyển các phần tử trong danh sách thành số nguyên 

# Tìm số nhỏ nhất
min_num = min(danh_sach) # min() trả về số nhỏ nhất trong danh sách

# In số nhỏ nhất
print("Số nhỏ nhất trong danh sách là:", min_num)
