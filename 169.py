# Viết Bằng Python
# Bài 169: Tìm số dài nhất có thể tạo bằng cách chọn các phần tử liên tiếp trong danh sách.

def find_largest_consecutive_number(nums): # Hàm tìm số lớn nhất
    largest_number = "" # Khởi tạo số lớn nhất (dưới dạng chuỗi)
    
    # Duyệt qua tất cả các dãy con liên tiếp
    for i in range(len(nums)):
        current_number = "" # Khởi tạo số hiện tại (dưới dạng chuỗi)
        for j in range(i, len(nums)):
            current_number += str(nums[j])  # Ghép các phần tử liên tiếp lại
            # So sánh và cập nhật số lớn nhất
            if len(current_number) > len(largest_number) or (len(current_number) == len(largest_number) and current_number > largest_number):
                largest_number = current_number # Cập nhật số lớn nhất
                
    return int(largest_number)  # Trả về số lớn nhất (dưới dạng int)

# Ví dụ sử dụng
nums = [1, 23, 4, 56, 789]  
result = find_largest_consecutive_number(nums)
print(f"Số dài nhất có thể tạo: {result}")
