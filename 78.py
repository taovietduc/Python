# VIẾT BẰNG PYTHON
# Bài 78: Tạo hàm tính tổng các số trong ma trận 2x2.

def tinh_tong_ma_tran(mat): # Hàm tính tổng các phần tử trong ma trận
    tong = 0    # Khởi tạo biến 'tong' để lưu tổng các phần tử trong ma trận
    for hang in mat:   # Duyệt qua từng hàng trong ma trận
        tong += sum(hang)  # Tính tổng mỗi hàng và cộng vào biến 'tong'
    return tong # Trả về tổng các phần tử trong ma trận

# Tạo ma trận 2x2
ma_tran = [[1, 2], [3, 4]] # Ma trận 2x2

# Gọi hàm và in kết quả
tong = tinh_tong_ma_tran(ma_tran) # Gọi hàm tính tổng các phần tử trong ma trận
print(f"Tổng các phần tử trong ma trận là: {tong}") # In kết quả
