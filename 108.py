# VIẾT BẰNG PYTHON
# Bài 108: Tạo hàm tính số hạng thứ n của dãy số hình học.

def tinh_so_hang_thu_n(a1, r, n): # a1: số hạng đầu tiên, r: công bội, n: vị trí số hạng
    return a1 * (r ** (n - 1)) # công thức tính số hạng thứ n của dãy số hình học

# Ví dụ sử dụng
a1 = float(input("Nhập số hạng đầu tiên (a1): ")) # Nhập số hạng đầu tiên
r = float(input("Nhập công bội (r): ")) # Nhập công bội
n = int(input("Nhập vị trí số hạng cần tính (n): ")) # Nhập vị trí số hạng cần tính
 
so_hang_thu_n = tinh_so_hang_thu_n(a1, r, n) # Gọi hàm tính số hạng thứ n của dãy số hình học
print(f"Số hạng thứ {n} của dãy là: {so_hang_thu_n}") # In kết quả

# Kết quả
# Nhập số hạng đầu tiên (a1): 2
# Nhập công bội (r): 3
# Nhập vị trí số hạng cần tính (n): 4
# Số hạng thứ 4 của dãy là: 54.0

