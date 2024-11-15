# VIẾT BẰNG PYTHON
# Bài 144: Viết hàm kiểm tra xem một danh sách có thể được sắp xếp thành một dãy số nguyên tố liên tiếp không.

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    # Hàm kiểm tra số nguyên tố
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Hàm kiểm tra dãy số nguyên tố liên tiếp
def can_form_consecutive_primes(lst):
    # Nếu danh sách rỗng hoặc chỉ có 1 phần tử thì trả về False
    if len(lst) <= 1:
        return False
    
    # Sắp xếp danh sách tăng dần
    sorted_lst = sorted(lst)
    
    # Kiểm tra phần tử đầu tiên có phải số nguyên tố
    if not is_prime(sorted_lst[0]):
        return False
        
    # Kiểm tra các phần tử liên tiếp
    for i in range(len(sorted_lst) - 1):
        # Nếu phần tử hiện tại không phải số nguyên tố
        if not is_prime(sorted_lst[i]):
            return False
        # Nếu khoảng cách giữa 2 số liên tiếp không phải là 2
        if sorted_lst[i+1] - sorted_lst[i] != 2:
            return False
            
    # Kiểm tra phần tử cuối cùng có phải số nguyên tố
    if not is_prime(sorted_lst[-1]):
        return False
        
    return True

# Ví dụ sử dụng
lst1 = [3, 5, 7]  # Dãy số nguyên tố liên tiếp
lst2 = [2, 3, 7]  # Dãy số không liên tiếp
lst3 = [4, 6, 8]  # Dãy không phải số nguyên tố

print("Danh sách 1:", lst1)
print("Có thể sắp xếp thành dãy số nguyên tố liên tiếp?", can_form_consecutive_primes(lst1))

print("\nDanh sách 2:", lst2) 
print("Có thể sắp xếp thành dãy số nguyên tố liên tiếp?", can_form_consecutive_primes(lst2))

print("\nDanh sách 3:", lst3)
print("Có thể sắp xếp thành dãy số nguyên tố liên tiếp?", can_form_consecutive_primes(lst3))

# VIẾT BẰNG PYTHON
# Kết quả chạy chương trình:
# Danh sách 1: [3, 5, 7]
# Có thể sắp xếp thành dãy số nguyên tố liên tiếp? True

# Danh sách 2: [2, 3, 7]
# Có thể sắp xếp thành dãy số nguyên tố liên tiếp? False

# Danh sách 3: [4, 6, 8] 
# Có thể sắp xếp thành dãy số nguyên tố liên tiếp? False

# Giải thích:
# - Danh sách 1: [3,5,7] là dãy số nguyên tố liên tiếp (khoảng cách giữa các số là 2)
# - Danh sách 2: [2,3,7] không phải dãy số nguyên tố liên tiếp (khoảng cách không đều)
# - Danh sách 3: [4,6,8] không phải dãy số nguyên tố
