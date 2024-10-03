# VIẾT BẰNG PYTHON
# Tạo ma trận 2x2 và tính tổng của các phần tử.

# Khai báo ma trận 2x2
ma_tran = [] # ma trận 2x2 sẽ có 2 hàng và mỗi hàng có 2 phần tử

# Nhập các phần tử của ma trận
print("Nhập các phần tử của ma trận 2x2:") 
for i in range(2): # Duyệt qua từng hàng của ma trận
    hang = [] # Khai báo một hàng mới để chứa các phần tử
    for j in range(2): # Duyệt qua từng phần tử trong hàng đó
        phan_tu = int(input(f"Phần tử [{i}][{j}]: ")) # Nhập phần tử từ bàn phím
        hang.append(phan_tu) # Thêm phần tử vào hàng đó
    ma_tran.append(hang) # Thêm hàng vào ma trận đó

# Tính tổng các phần tử
tong = 0 # Khởi tạo biến tổng bằng 0
for i in range(2): # Duyệt qua từng hàng của ma trận 
    for j in range(2): # Duyệt qua từng phần tử trong hàng đó
        tong += ma_tran[i][j] # Cộng phần tử đó vào biến tổng

# In ra tổng các phần tử
print("Tổng các phần tử trong ma trận là:", tong) 

# OUTPUT
# Nhập các phần tử của ma trận 2x2:
# Phần tử [0][0]: 1
# Phần tử [0][1]: 2
# Phần tử [1][0]: 3
# Phần tử [1][1]: 4

# Tổng các phần tử trong ma trận là: 10
