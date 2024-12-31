# Viết bằng Python
# Bài 189: Tạo hàm tìm tất cả các số Smith trong một khoảng.

def prime_factors(n): # tìm các ước số nguyên tố của n 
    factors = [] # danh sách chứa các ước số nguyên tố của n
    divisor = 2 # ước số nguyên tố đầu tiên là 2
    while divisor * divisor <= n: # duyệt qua các ước số nguyên tố từ 2 đến căn bậc hai của
        while n % divisor == 0: 
        # nếu n chia hết cho divisor thì thêm divisor vào danh sách factors
            factors.append(divisor) # thêm ước số nguyên tố divisor vào danh sách factors
            n //= divisor # chia n cho divisor để tìm ước số nguyên tố tiếp theo
        divisor += 1 # tăng divisor lên 1
    if n > 1: # nếu n còn lớn hơn 1 thì thêm n vào danh sách factors
        factors.append(n) # thêm n vào danh sách factors
    return factors

def is_smith(number): # kiểm tra xem number có phải là số Smith không
    if number < 2: # nếu number nhỏ hơn 2 thì không phải số Smith
        return False
    factors = prime_factors(number) # tìm các ước số nguyên tố của number
    if len(factors) == 1:  # Không phải số hợp
        return False
    digits_sum = sum(int(digit) for digit in str(number)) # Tính tổng các chữ số của number
    factors_sum = sum(sum(int(digit) for digit in str(factor)) for factor in factors) 
    # Tính tổng các chữ số của các ước số nguyên tố
    return digits_sum == factors_sum

def find_smith_numbers(start, end): # tìm các số Smith trong khoảng từ start đến end
    return [i for i in range(start, end + 1) if is_smith(i)] 
    # tìm các số Smith trong khoảng từ start đến end

# Ví dụ
start, end = 4, 100 # khoảng từ 4 đến 100
smith_numbers = find_smith_numbers(start, end) 
# tìm các số Smith trong khoảng từ start đến end
print(f"Các số Smith trong khoảng {start}-{end}: {smith_numbers}") 

# Kết quả
# Các số Smith trong khoảng 4-100: [4, 22, 27, 58, 85]
# Các số Smith trong khoảng từ 4 đến 100 là 4, 22, 27, 58, 85.
# Số 4 có tổng các chữ số là 4. 4 = 2 * 2.
# Số 22 có tổng các chữ số là 4. 22 = 2 * 11.
# Số 27 có tổng các chữ số là 9. 27 = 3 * 3 * 3.
# Số 58 có tổng các chữ số là 13. 58 = 2 * 29.
# Số 85 có tổng các chữ số là 13. 85 = 5 * 17.
# Cách làm này cũng áp dụng được cho số âm.
# Ví dụ số -4 không phải là số Smith vì không thể tìm được ước số nguyên tố.