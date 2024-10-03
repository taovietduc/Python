# VIẾT BẰNG PYTHON
# Tạo danh sách các số nguyên tố từ danh sách: Nhập một danh sách các số và tạo danh sách các số nguyên tố.

import math

# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(so): # Kiểm tra số nguyên tố
    if so < 2: # Số nguyên tố phải lớn hơn 1
        return False
    for i in range(2, int(math.sqrt(so)) + 1): # Duyệt từ 2 đến căn bậc 2 của số
        if so % i == 0: # Nếu số chia hết cho một số khác 1 và chính nó thì không phải số nguyên tố
            return False # Trả về False
    return True

# Nhập danh sách các số
n = int(input("Nhập số lượng phần tử trong danh sách: ")) # Nhập số lượng phần tử
danh_sach = [] # Khởi tạo danh sách
print("Nhập các phần tử:") # Nhập các phần tử
for i in range(n): # Duyệt từ 0 đến n - 1
    so = int(input()) # Nhập số
    danh_sach.append(so) # Thêm số vào danh sách

# Lọc số nguyên tố
danh_sach_nguyen_to = [so for so in danh_sach if la_so_nguyen_to(so)] 

# In danh sách số nguyên tố
print("Danh sách các số nguyên tố là:", danh_sach_nguyen_to)
