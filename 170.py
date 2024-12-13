# Viết Bằng Python
# Bài 170: Tạo hàm tìm các bộ ba phần tử trong danh sách sao cho tổng của chúng bằng 0.

def three_sum(nums):
    nums.sort()  # Sắp xếp danh sách để dễ dàng loại trừ trùng lặp
    result = []

    for i in range(len(nums) - 2):
        # Bỏ qua các giá trị trùng lặp tại i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1  # Đặt hai con trỏ
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Loại bỏ các phần tử trùng lặp tại left và right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif current_sum < 0:
                left += 1  # Tăng giá trị tổng bằng cách di chuyển con trỏ trái
            else:
                right -= 1  # Giảm giá trị tổng bằng cách di chuyển con trỏ phải
    
    return result

# Ví dụ sử dụng
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(f"Các bộ ba có tổng bằng 0: {result}")
