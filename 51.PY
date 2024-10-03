# VIẾT BẰNG PYTHON
# BÀI 51:Tạo danh sách các số Fibonacci từ 0 đến n.

# Nhập một số n từ người dùng
n = int(input("Nhập một số n: ")) 

# Tạo danh sách các số Fibonacci
fibonacci_list = [] # Khởi tạo danh sách rỗng để lưu các số Fibonacci
a, b = 0, 1 # Khởi tạo 2 số đầu tiên của dãy Fibonacci

while a <= n: # Lặp cho đến khi số Fibonacci lớn h
    fibonacci_list.append(a) # Thêm số Fibonacci a vào danh sách
    a, b = b, a + b # Cập nhật 2 số Fibonacci tiếp theo

# In danh sách các số Fibonacci
print(f"Danh sách các số Fibonacci từ 0 đến {n}: {fibonacci_list}") 
