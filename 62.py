# VIẾT BẰNG PYTHON
# Bài 62: Tạo hàm tính số Fibonacci thứ n.

# Hàm tính số Fibonacci thứ n
def fibonacci(n): # Hàm có tham số truyền vào là n 
    if n <= 0: # Nếu n <= 0 thì trả về thông báo số phải lớn hơn 0
        return "Số phải lớn hơn 0" 
    elif n == 1: # Nếu n = 1 thì trả về 0 vì số Fibonacci thứ 1 là 0
        return 0 
    elif n == 2: # Nếu n = 2 thì trả về 1 vì số Fibonacci thứ 2 là 1
        return 1
    else: # Ngược lại 
        a, b = 0, 1
        for i in range(2, n): # Duyệt từ 2 đến n 
            a, b = b, a + b # Gán a = b, b = a + b 
        return b

# Nhập số Fibonacci cần tính
n = int(input("Nhập số n để tính số Fibonacci thứ n: "))
print(f"Số Fibonacci thứ {n} là:", fibonacci(n))
