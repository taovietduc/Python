# VIẾT BẰNG PYTHON
# Sắp xếp danh sách: Nhập một danh sách các số và sắp xếp chúng theo thứ tự tăng dần.

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split())) 
# map(int, ...) chuyển các phần tử trong list thành kiểu int, input() nhập chuỗi từ bàn phím,
#.split() tách chuỗi thành list

# Sắp xếp danh sách theo thứ tự tăng dần
danh_sach.sort() # Sử dụng phương thức sort() để sắp xếp danh sách

# In danh sách đã sắp xếp
print("Danh sách sau khi sắp xếp:", danh_sach)

# Kết quả
# Nhập các số cách nhau bởi dấu cách: 5 3 7 2 8 4
# Danh sách sau khi sắp xếp: [2, 3, 4, 5, 7, 8]