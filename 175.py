# Viết Bằng Python
# Bài 175: Viết hàm loại bỏ tất cả các phần tử trùng lặp liên tiếp trong danh sách.

def remove_consecutive_duplicates(nums): # Hàm loại bỏ phần tử trùng liên tiếp
    if not nums: # Nếu danh sách rỗng thì trả về danh sách rỗng
        return []

    result = [nums[0]]  # Luôn thêm phần tử đầu tiên
    for i in range(1, len(nums)): # Duyệt từ phần tử thứ 2 đến cuối danh sách
        if nums[i] != nums[i - 1]: # Nếu phần tử hiện tại khác phần tử trước đó
            result.append(nums[i])  # Chỉ thêm khi không trùng phần tử trước đó
    return result

# Test
nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5] # Danh sách cần loại bỏ phần tử trùng liên tiếp
print(remove_consecutive_duplicates(nums))  # Output: [1, 2, 3, 4, 5]