# VIẾT BẰNG PYTHON
# BÀI 52:Tạo chuỗi từ các phần tử trong danh sách.

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: ")) 

# Nhập các phần tử vào danh sách
danh_sach = [] # Khởi tạo danh sách rỗng để lưu trữ các phần tử
for i in range(n): # Duyệt qua từng phần tử trong danh sách
    phan_tu = input(f"Nhập phần tử thứ {i + 1}: ") # Nhập phần tử từ bàn phím
    danh_sach.append(phan_tu) # Thêm phần tử vào danh sách 

# Tạo chuỗi từ danh sách
chuoi = ' '.join(danh_sach) # Sử dụng phương thức join() để tạo chuỗi từ danh sách

# In chuỗi
print("Chuỗi được tạo từ danh sách là:", chuoi)

