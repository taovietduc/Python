# Viết bằng Python
# Bài 193: Kiểm tra xem một dãy số có phải là dãy con của dãy Fibonacci không.

def generate_fibonacci(limit): # Hàm tạo dãy Fibonacci nhỏ hơn hoặc bằng limit cho trước
    fib = [0, 1] # Dãy Fibonacci đầu tiên
    while fib[-1] <= limit: # Thêm số Fibonacci mới vào dãy cho đến khi số mới nhất lớn hơn limit
        fib.append(fib[-1] + fib[-2]) # Số Fibonacci mới bằng tổng 2 số Fibonacci trước đó
    return set(fib) # Trả về tập hợp các số Fibonacci nhỏ hơn hoặc bằng limit

def is_fibonacci_subsequence(seq): # Hàm kiểm tra xem dãy số có phải là dãy con của dãy Fibonacci không
    if not seq: # Nếu dãy rỗng
        return False # Trả về False
    fib_set = generate_fibonacci(max(seq)) # Tạo tập hợp các số Fibonacci nhỏ hơn hoặc bằng số lớn nhất trong dãy
    return all(num in fib_set for num in seq)

seq = [1, 2, 3, 5] # Dãy số cần kiểm tra
print(is_fibonacci_subsequence(seq))  # Output: True