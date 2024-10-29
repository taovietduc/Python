# VIẾT BẰNG PYTHON
# Bài 113: Tạo hàm tính tổng các số nguyên tố trong khoảng cho trước.

def is_prime(n): 
    """
    Kiểm tra một số có phải là số nguyên tố hay không.

    Parameters:
    n (int): Số cần kiểm tra.

    Returns:
    bool: True nếu là số nguyên tố, False nếu không.
    """
    if n < 2: # Số nguyên tố phải lớn hơn 1
        return False 
    for i in range(2, int(n**0.5) + 1): 
    # Số nguyên tố không chia hết cho số nào khác ngoài 1 và chính nó
        if n % i == 0: # Nếu n chia hết cho i
            return False 
    return True

def sum_primes_in_range(start, end): 
# Hàm tính tổng các số nguyên tố trong khoảng [start, end]
    """
    Tính tổng các số nguyên tố trong khoảng [start, end].

    Parameters:
    start (int): Điểm bắt đầu của khoảng.
    end (int): Điểm kết thúc của khoảng.

    Returns:
    int: Tổng các số nguyên tố trong khoảng.
    """
    total = 0 # Khởi tạo biến tổng
    for num in range(start, end + 1): # Duyệt qua các số trong khoảng
        if is_prime(num): # Nếu là số nguyên tố
            total += num # Cộng vào tổng
    return total # Trả về tổng

# Ví dụ sử dụng
start = 10 # Điểm bắt đầu
end = 30 # Điểm kết thúc 
print(f"Tổng các số nguyên tố trong khoảng [{start}, {end}] là: {sum_primes_in_range(start, end)}")
