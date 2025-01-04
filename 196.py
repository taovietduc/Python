# Viết bằng Python
# Bài 196: Kiểm tra xem một số có thể được viết dưới dạng tổng của hai số nguyên tố hay không.

def is_prime(n): # Hàm kiểm tra số nguyên tố 
    if n < 2: # Nếu n nhỏ hơn 2 thì không phải là số nguyên tố
        return False
    for i in range(2, int(n**0.5) + 1): # Vòng lặp từ 2 đến căn bậc 2 của n
        if n % i == 0: # Nếu n chia hết cho i thì không phải là số nguyên tố
            return False
    return True

def can_be_sum_of_two_primes(n): 
# Hàm kiểm tra số có thể được viết dưới dạng tổng của hai số nguyên tố hay không
    for i in range(2, n // 2 + 1): # Vòng lặp từ 2 đến n//2 + 1
        if is_prime(i) and is_prime(n - i): # Nếu i và n - i là số nguyên tố
            return True
    return False

number = 34 # Số cần kiểm tra
print(can_be_sum_of_two_primes(number))  # Output: True

number = 94 # Số cần kiểm tra
print(can_be_sum_of_two_primes(number))  # Output: True