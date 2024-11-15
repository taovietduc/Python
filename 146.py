# VIẾT BẰNG PYTHON
# Bài 146: Viết hàm tính tích của tất cả các số nguyên tố nhỏ hơn một số cho trước.

def is_prime(n): # Hàm kiểm tra số nguyên tố 
    # Kiểm tra số nguyên tố
    if n < 2:           
        return False # Nếu n < 2 thì không phải số nguyên tố
    for i in range(2, int(n ** 0.5) + 1): # Duyệt từ 2 đến căn bậc 2 của n   
        if n % i == 0:
            return False # Nếu n chia hết cho số nào thì không phải số nguyên tố
    return True # Nếu không chia hết cho số nào thì là số nguyên tố

def product_of_primes(n): # Hàm tính tích các số nguyên tố nhỏ hơn n
    result = 1 # Khởi tạo biến result = 1 để lưu tích 
    
    # Duyệt từ 2 đến n-1
    for i in range(2, n): # Duyệt từ 2 đến n-1 
        # Nếu i là số nguyên tố thì nhân vào kết quả
        if is_prime(i):
            result *= i # Nhân vào kết quả 
            
    return result # Trả về kết quả   

# Kiểm thử hàm 
test_cases = [10, 15, 20] # Test với các số 10, 15, 20  
for n in test_cases:
    result = product_of_primes(n) # Gọi hàm tính tích các số nguyên tố nhỏ hơn n 
    print(f"\nTest với n = {n}:") # In ra test với n = n    
    print(f"Tích các số nguyên tố nhỏ hơn {n} là: {result}") # In ra kết quả tích các số nguyên tố nhỏ hơn n 
    print(f"Các số nguyên tố nhỏ hơn {n} là:", end=" ")
    print([i for i in range(2, n) if is_prime(i)]) # In ra các số nguyên tố nhỏ hơn n 

"""
Giải thích chi tiết:

1. Hàm is_prime(n):
   - Kiểm tra một số có phải số nguyên tố hay không
   - Nếu n < 2 thì không phải số nguyên tố
   - Kiểm tra từ 2 đến căn bậc 2 của n
   - Nếu n chia hết cho số nào thì không phải số nguyên tố
   
2. Hàm product_of_primes(n):
   - Input: Số nguyên n
   - Output: Tích các số nguyên tố nhỏ hơn n
   - Khởi tạo result = 1 để lưu tích
   - Duyệt từ 2 đến n-1
   - Nếu số i là số nguyên tố thì nhân vào result
   
3. Kết quả chạy:
Test với n = 10:
- Các số nguyên tố nhỏ hơn 10: [2, 3, 5, 7]
- Tích = 2 * 3 * 5 * 7 = 210

Test với n = 15:
- Các số nguyên tố nhỏ hơn 15: [2, 3, 5, 7, 11, 13]
- Tích = 2 * 3 * 5 * 7 * 11 * 13 = 30030

Test với n = 20:
- Các số nguyên tố nhỏ hơn 20: [2, 3, 5, 7, 11, 13, 17, 19]
- Tích = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 = 9699690
"""
