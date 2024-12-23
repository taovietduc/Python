# Viết Bằng Python
# Bài 172: Tạo hàm tìm khoảng cách nhỏ nhất giữa hai phần tử bất kỳ trong danh sách.

def min_distance(nums): # Hàm tìm khoảng cách nhỏ nhất giữa hai phần tử bất kỳ trong danh sách
    nums.sort() # Sắp xếp danh sách
    min_dist = float('inf') # Khởi tạo khoảng cách nhỏ nhất
    for i in range(len(nums) - 1): # Duyệt qua các phần tử trong danh sách
        min_dist = min(min_dist, abs(nums[i + 1] - nums[i]))
    return min_dist

# Test
nums = [4, 7, 10, 20, 15]
print(min_distance(nums))  # Output: 3 (7 và 10)
