# VIẾT BẰNG PYTHON
# Bài 154: Tạo hàm tìm số nguyên tố lớn nhất là bội số của một số cho trước.

def is_prime(n):
    # Kiểm tra số nguyên tố
    if n < 2:
        return False # Nếu n < 2 thì không phải số nguyên tố
    for i in range(2, int(n ** 0.5) + 1):   
        if n % i == 0:
            return False # Nếu n chia hết cho bất kỳ số nào -> không phải số nguyên tố
    return True # Ngược lại -> là số nguyên tố

def find_largest_prime_multiple(n, limit=10000):
    # Tìm số nguyên tố lớn nhất là bội của n trong khoảng [1, limit]
    # Duyệt từ lớn đến nhỏ để tìm số nguyên tố lớn nhất
    for i in range(limit, n-1, -1):
        # Kiểm tra nếu i là bội của n và là số nguyên tố
        if i % n == 0 and is_prime(i):
            return i # Trả về i nếu thỏa điều kiện
    return -1  # Trả về -1 nếu không tìm thấy

# Test thử hàm
if __name__ == "__main__":
    n = int(input("Nhập số n: "))
    result = find_largest_prime_multiple(n)
    
    if result != -1:
        print(f"Số nguyên tố lớn nhất là bội của {n} là: {result}")
    else:
        print("Không tìm thấy số thỏa mãn!")

"""
Giải thích chi tiết:

1. Hàm is_prime(n):
   - Kiểm tra một số có phải là số nguyên tố hay không
   - Nếu n < 2 thì không phải số nguyên tố
   - Kiểm tra các ước từ 2 đến căn bậc 2 của n
   - Nếu n chia hết cho bất kỳ số nào -> không phải số nguyên tố
   - Ngược lại -> là số nguyên tố

2. Hàm find_largest_prime_multiple(n, limit=10000):
   - Tìm số nguyên tố lớn nhất là bội của n trong khoảng [1, limit]
   - Duyệt từ lớn đến nhỏ (limit đến n) để tìm số lớn nhất
   - Với mỗi số i:
     + Kiểm tra xem i có chia hết cho n không (là bội của n)
     + Kiểm tra xem i có phải số nguyên tố không
     + Nếu thỏa cả 2 điều kiện -> return i
   - Nếu không tìm thấy số thỏa mãn -> return -1

3. Phần test:
   - Nhập số n từ người dùng
   - Gọi hàm find_largest_prime_multiple(n)
   - In kết quả tương ứng

4. Độ phức tạp:
   - Thời gian: O(limit * sqrt(limit)) trong trường hợp xấu nhất
   - Không gian: O(1)
"""
