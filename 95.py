# VIẾT BẰNG PYTHON
# Bài 95: Tạo hàm tính tổng các chữ số trong một số.

# Hàm tính tổng các chữ số trong một số
def tinh_tong_chu_so(n): # n là số cần tính tổng các chữ số
    tong = 0       # Khởi tạo biến tổng
    while n != 0: # Vòng lặp chạy cho đến khi n = 0
        tong += n % 10  # Lấy chữ số cuối cùng
        n //= 10  # Loại bỏ chữ số cuối cùng
    return tong

# Nhập từ bàn phím và in kết quả
n = int(input("Nhập một số: ")) # Nhập một số từ bàn phím
print(f"Tổng các chữ số trong {n} là: {tinh_tong_chu_so(n)}") # In kết quả

# Kết quả
# Nhập một số: 1234 
# Tổng các chữ số trong 1234 là: 10 ( 1 + 2 + 3 + 4 = 10 )