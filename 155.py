# VIẾT BẰNG PYTHON
# Bài 155: Viết hàm kiểm tra xem một danh sách có thể chia thành hai mảng con có tổng bằng nhau không.

def can_partition(nums):
    # Tính tổng của toàn bộ mảng
    total_sum = sum(nums)
    
    # Nếu tổng lẻ thì không thể chia đều thành 2 phần
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # Tạo bảng dp để lưu trữ kết quả
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Khởi tạo giá trị ban đầu - tổng 0 luôn có thể đạt được
    for i in range(n + 1):
        dp[i][0] = True
    
    # Điền bảng dp
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i-1] <= j:
                # Có thể lấy hoặc không lấy phần tử hiện tại
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                # Không thể lấy phần tử hiện tại vì nó lớn hơn tổng cần đạt
                dp[i][j] = dp[i-1][j]
    
    return dp[n][target]

# Test thử hàm
if __name__ == "__main__":
    # Test với một số ví dụ
    test_cases = [
        [1, 5, 11, 5],  # True (có thể chia thành [1,5,5] và [11])
        [1, 2, 3, 5],   # False
        [2, 2, 2, 2]    # True (có thể chia thành [2,2] và [2,2])
    ]
    
    for nums in test_cases:
        result = can_partition(nums)
        print(f"Mảng {nums}: {'Có' if result else 'Không'} thể chia thành 2 phần bằng nhau")

"""
Giải thích chi tiết:

1. Hàm can_partition(nums):
   - Input: Một mảng số nguyên nums
   - Output: True nếu có thể chia thành 2 phần có tổng bằng nhau, False nếu không thể

2. Các bước thực hiện:
   a) Kiểm tra điều kiện đầu tiên:
      - Tính tổng của mảng
      - Nếu tổng lẻ -> không thể chia đều -> return False
      - Nếu tổng chẵn -> target = tổng/2 (đây là tổng cần đạt được cho mỗi phần)

   b) Sử dụng quy hoạch động (Dynamic Programming):
      - Tạo bảng dp[n+1][target+1] để lưu kết quả
      - dp[i][j] = True nếu có thể tạo tổng j từ i phần tử đầu tiên
      
   c) Khởi tạo bảng dp:
      - Tổng 0 luôn có thể đạt được -> dp[i][0] = True
      
   d) Điền bảng dp:
      - Với mỗi phần tử i và tổng j:
        + Nếu nums[i-1] <= j: có thể chọn hoặc không chọn phần tử hiện tại
        + Nếu nums[i-1] > j: không thể chọn phần tử hiện tại
        
   e) Kết quả cuối cùng là dp[n][target]

3. Độ phức tạp:
   - Thời gian: O(n * target) với n là số phần tử và target là tổng/2
   - Không gian: O(n * target) để lưu bảng dp

4. Ví dụ:
   - [1,5,11,5]: Có thể chia thành [1,5,5] và [11], cùng có tổng là 11
   - [1,2,3,5]: Không thể chia đều vì tổng là 11 (lẻ)
   - [2,2,2,2]: Có thể chia thành [2,2] và [2,2], cùng có tổng là 4
"""
