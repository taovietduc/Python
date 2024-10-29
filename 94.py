# VIẾT BẰNG PYTHON
# Bài 94: Tạo hàm tìm số Fibonacci lớn nhất nhỏ hơn hoặc bằng n.

# Hàm tính số Fibonacci lớn nhất nhỏ hơn hoặc bằng n
def fibonacci_lon_nhat(n): # Hàm này trả về số Fibonacci lớn nhất nhỏ hơn hoặc bằng n
    if n < 0: # Không có số Fibonacci cho n âm nên trả về -1
        return -1  # Không có số Fibonacci cho n âm
    if n == 0: # Số Fibonacci cho n = 0 là 0
        return 0  # Số Fibonacci cho n = 0 là 0
    
    fib1, fib2 = 0, 1 # Khởi tạo 2 số Fibonacci đầu tiên
    
    while fib2 <= n: # Duyệt qua các số Fibonacci cho đến khi số Fibonacci lớn nhất nhỏ hơn hoặc bằng n
        fib1, fib2 = fib2, fib1 + fib2 
        # Cập nhật 2 số Fibonacci tiếp theo để duyệt tiếp tục cho đến khi số Fibonacci lớn nhất nhỏ hơn hoặc bằng n

    return fib1 # Trả về số Fibonacci lớn nhất nhỏ hơn hoặc bằng n

# Nhập số n từ người dùng
n = int(input("Nhập số n: ")) # Nhập số n từ người dùng
fib_max = fibonacci_lon_nhat(n) # Gọi hàm tìm số Fibonacci lớn nhất nhỏ hơn hoặc bằng n

if fib_max != -1: # Nếu tồn tại số Fibonacci lớn nhất nhỏ hơn hoặc bằng n
    print(f"Số Fibonacci lớn nhất nhỏ hơn hoặc bằng {n} là: {fib_max}")
else: # Nếu không tồn tại số Fibonacci lớn nhất nhỏ hơn hoặc bằng n
    print("Không tồn tại số Fibonacci.")

# Kết quả
# Nhập số n: 20
# Số Fibonacci lớn nhất nhỏ hơn hoặc bằng 20 là: 13