# VIẾT BẰNG PYTHON
# Bài 137: Kiểm tra một số có phải là số mạnh không.

import math

def is_strong_number(num): # Hàm kiểm tra số mạnh (Strong number) hay không
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(num)) 
    # Tính tổng giai thừa của các chữ số trong số num 
    return sum_of_factorials == num 
    # Trả về True nếu tổng giai thừa bằng num, ngược lại False

# Ví dụ sử dụng
num = 145 # Số mạnh (Strong number)
print(f"Số {num} là số mạnh:", is_strong_number(num)) # Kết quả: True

# Kết quả: True
# Giải thích: 1! + 4! + 5! = 1 + 24 + 120 = 145

