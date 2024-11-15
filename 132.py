# VIẾT BẰNG PYTHON
# Bài 132: Tạo hàm đếm số lượng số nguyên tố trong danh sách.

def is_prime(n): # Hàm kiểm tra số nguyên tố 
    if n <= 1: # Nếu n nhỏ hơn hoặc bằng 1 thì không phải số nguyên tố
        return False 
    for i in range(2, int(n ** 0.5) + 1): # Duyệt từ 2 đến căn bậc 2 của n
        if n % i == 0: # Nếu n chia hết cho i thì không phải số nguyên tố
            return False 
    return True # Còn lại là số nguyên tố

def count_primes_in_list(lst): # Hàm đếm số lượng số nguyên tố trong danh sách
    return sum(1 for num in lst if is_prime(num))  
    # Sử dụng hàm is_prime để kiểm tra số nguyên tố và đếm số lượng số nguyên tố trong danh sách

# Ví dụ sử dụng
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10] # Danh sách số cần kiểm tra số nguyên tố
print("Số lượng số nguyên tố trong danh sách là:", count_primes_in_list(numbers)) 
# In ra số lượng số nguyên tố trong danh sách

# Kết quả
# Số lượng số nguyên tố trong danh sách là: 4
# Có 4 số nguyên tố trong danh sách là 2, 3, 5, 7

