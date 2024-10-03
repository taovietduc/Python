# VIẾT BẰNG PYTHON 
# Lọc danh sách theo điều kiện: Nhập một danh sách và một điều kiện, lọc các phần tử thỏa mãn điều kiện.

# Nhập danh sách các phần tử từ người dùng
danh_sach = list(map(int, input("Nhập danh sách các số (phân tách bằng dấu cách): ").split())) 
# Nhập danh sách các số từ bàn phím và tách chúng bằng dấu cách, .split() tách chuỗi thành list
# list(map(int, ...) chuyển các phần tử trong list thành kiểu số nguyên 

# Lọc các phần tử thỏa mãn điều kiện (số chẵn)
danh_sach_loc = [x for x in danh_sach if x % 2 == 0] 
# Lọc các phần tử chia hết cho 2 (số chẵn) từ danh sách 

# In danh sách đã lọc
print("Danh sách các số chẵn là:", danh_sach_loc)
