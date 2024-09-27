# VIẾT BẰNG PYTHON
# Tìm số lớn nhất trong danh sách: Nhập một danh sách các số và tìm số lớn nhất trong danh sách.

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split())) 
# Sử dụng hàm map() để chuyển các phần tử nhập vào thành kiểu int và lưu vào danh sách

# Tìm số lớn nhất
max_num = max(danh_sach) # Sử dụng hàm max() để tìm số lớn nhất

# In số lớn nhất
print("Số lớn nhất trong danh sách là:", max_num)
