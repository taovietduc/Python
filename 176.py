# Viết Bằng Python
# Bài 176: Tạo hàm tìm số lớn thứ ba trong danh sách mà không dùng hàm sẵn có.

def third_largest(nums): # Tạo hàm third_largest với tham số truyền vào là nums
    first, second, third = float('-inf'), float('-inf'), float('-inf')
    for num in nums: # Duyệt từng phần tử trong nums
        if num > first: # Nếu num lớn hơn first
            third, second, first = second, first, num # Gán third = second, second = first, first = num
        elif num > second and num < first: # Nếu num lớn hơn second và nhỏ hơn first
            third, second = second, num # Gán third = second, second = num
        elif num > third and num < second: # Nếu num lớn hơn third và nhỏ hơn second
            third = num
    return third if third != float('-inf') else None # Trả về third nếu third khác float('-inf') ngược lại trả về None

nums = [4, 1, 2, 9, 7, 3]
print(third_largest(nums))  # Output: 4
