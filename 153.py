# VIẾT BẰNG PYTHON
# Bài 153: Viết hàm xác định xem có thể tạo được số Fibonacci từ tổ hợp của các phần tử trong danh sách không.

def is_fibonacci(n):
    # Kiểm tra xem một số có phải là số Fibonacci hay không
    # Một số là số Fibonacci nếu một trong (5n^2 + 4) hoặc (5n^2 - 4) là số chính phương
    def is_perfect_square(x): 
        s = int(x ** 0.5) # Lấy căn bậc 2 của x     
        return s * s == x # Kiểm tra xem bình phương có bằng x hay không    
    
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4) 
    # Kiểm tra xem có phải số Fibonacci hay không

def can_make_fibonacci(arr):
    # Hàm kiểm tra xem có thể tạo được số Fibonacci từ tổ hợp các phần tử trong mảng
    n = len(arr)
    
    # Tạo tất cả các tổ hợp có thể từ mảng
    def get_combinations(start, current_sum):
        # Kiểm tra nếu tổng hiện tại là số Fibonacci
        if current_sum > 0 and is_fibonacci(current_sum):
            return True
            
        # Thử thêm từng phần tử vào tổng hiện tại
        for i in range(start, n):
            if get_combinations(i + 1, current_sum + arr[i]):
                return True
                
        return False
    
    return get_combinations(0, 0)

# Test thử hàm
if __name__ == "__main__":
    # Test case 1: [1, 2, 3, 4]
    arr1 = [1, 2, 3, 4]
    print(f"Mảng {arr1}:", end=" ") # In ra màn hình
    if can_make_fibonacci(arr1):
        print("Có thể tạo được số Fibonacci") 
    else:
        print("Không thể tạo được số Fibonacci")
        
    # Test case 2: [4, 2, 8, 5] 
    arr2 = [4, 2, 8, 5]
    print(f"Mảng {arr2}:", end=" ") # In ra màn hình
    if can_make_fibonacci(arr2):
        print("Có thể tạo được số Fibonacci")
    else:
        print("Không thể tạo được số Fibonacci")

"""
Giải thích chi tiết:

1. Hàm is_fibonacci(n):
   - Kiểm tra một số có phải là số Fibonacci hay không
   - Sử dụng tính chất: một số là số Fibonacci khi và chỉ khi một trong hai số 
     (5n^2 + 4) hoặc (5n^2 - 4) là số chính phương
   - Hàm is_perfect_square(x) kiểm tra x có phải số chính phương không

2. Hàm can_make_fibonacci(arr):
   - Sử dụng đệ quy để tạo tất cả các tổ hợp có thể từ mảng
   - Hàm get_combinations(start, current_sum):
     + start: vị trí bắt đầu xét trong mảng
     + current_sum: tổng hiện tại của tổ hợp
     + Với mỗi phần tử, ta có 2 lựa chọn:
       * Thêm phần tử vào tổng hiện tại
       * Không thêm phần tử và xét phần tử tiếp theo
     + Nếu tổng hiện tại > 0 và là số Fibonacci -> return True
     + Nếu không tìm được tổ hợp nào -> return False

3. Độ phức tạp:
   - Thời gian: O(2^n) do phải xét tất cả tổ hợp có thể
   - Không gian: O(n) cho đệ quy stack

4. Test cases:
   - arr1 = [1, 2, 3, 4]: Có thể tạo được số Fibonacci (ví dụ: 3)
   - arr2 = [4, 2, 8, 5]: Có thể tạo được số Fibonacci (ví dụ: 8)
"""
