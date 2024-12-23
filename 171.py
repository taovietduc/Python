# Viết Bằng Python
# Bai 171: Viết hàm sắp xếp danh sách các số nhưng chỉ di chuyển các số nguyên tố.

def is_prime(n): # Kiểm tra số nguyên tố hay không
    if n < 2: # 0, 1 không phải số nguyên tố nên trả về False
        return False
    for i in range(2, int(n**0.5) + 1): # Vòng lặp từ 2 đến căn bậc 2 của n
        if n % i == 0: # Nếu n chia hết cho i thì n không phải số nguyên tố
            return False
    return True

def sort_primes_only(nums): # Sắp xếp danh sách các số nhưng chỉ di chuyển các số nguyên tố
    primes = sorted([num for num in nums if is_prime(num)])  # Lấy danh sách số nguyên tố và sắp xếp
    result = []
    prime_index = 0

    for num in nums: # Duyệt qua từng số trong danh sách
        if is_prime(num):
            result.append(primes[prime_index])  # Chèn số nguyên tố đã sắp xếp
            prime_index += 1
        else:
            result.append(num)  # Giữ nguyên vị trí của số không phải nguyên tố

    return result

# Test
nums = [11, 4, 7, 8, 3, 10, 2]
print(sort_primes_only(nums))  # Output: [2, 4, 3, 8, 7, 10, 11]
