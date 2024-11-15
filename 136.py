# VIẾT BẰNG PYTHON
# Bài 136: Tìm số Fibonacci lớn thứ hai nhỏ hơn hoặc bằng 

def second_largest_fibonacci(n): # Hàm tìm số Fibonacci lớn thứ hai nhỏ hơn hoặc bằng n
    if n < 1: # Nếu n nhỏ hơn 1, trả về None (không có số Fibonacci nào nhỏ hơn 1)
        return None 

    # Khởi tạo dãy Fibonacci ban đầu
    fib1, fib2 = 0, 1 # fib1 = 0, fib2 = 1 
    fib_list = [] # Dãy Fibonacci ban đầu rỗng 

    # Xây dựng dãy Fibonacci nhỏ hơn hoặc bằng n
    while fib2 <= n: # Vòng lặp chạy khi số Fibonacci thứ 2 nhỏ hơn hoặc bằng
        fib_list.append(fib2) # Thêm số Fibonacci thứ 2 vào dãy
        fib1, fib2 = fib2, fib1 + fib2 # Cập nhật số Fibonacci thứ 1 và th

    # Nếu dãy có ít hơn 2 phần tử, trả về phần tử đầu tiên
    if len(fib_list) < 2: # Nếu dãy có ít hơn 2 phần tử
        return fib_list[0] if fib_list else None # Trả về phần tử đầu tiên hoặc None

    # Trả về số Fibonacci lớn thứ hai
    return fib_list[-2] # Trả về số Fibonacci lớn thứ hai

# Ví dụ sử dụng
n = 20
print(f"Số Fibonacci lớn thứ hai nhỏ hơn hoặc bằng {n} là:", second_largest_fibonacci(n))

# Kết quả
# Số Fibonacci lớn thứ hai nhỏ hơn hoặc bằng 20 là: 13

