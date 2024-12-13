# Viết Bằng Python
# Bài 167: Viết hàm tìm ba số có tổng gần nhất với một số cho trước trong danh sách.

def three_sum_closest(nums, target):
    nums.sort()  # Bước 1: Sắp xếp danh sách
    closest_sum = float('inf')  # Khởi tạo tổng gần nhất là vô cực
    
    for i in range(len(nums) - 2):  # Duyệt qua từng phần tử
        left, right = i + 1, len(nums) - 1  # Hai con trỏ: left và right
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]  # Tính tổng hiện tại
            
            # Nếu tổng hiện tại gần với target hơn, cập nhật closest_sum
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            
            # Điều chỉnh con trỏ dựa trên giá trị tổng
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # Nếu tổng đúng bằng target, trả về ngay
    
    return closest_sum

# Ví dụ sử dụng
nums = [-1, 2, 1, -4]
target = 1
result = three_sum_closest(nums, target)
print(f"Tổng gần nhất với {target} là: {result}")
