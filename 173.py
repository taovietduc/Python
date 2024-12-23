# Viết Bằng Python 
# Bài 173: Viết hàm tìm danh sách con có tổng lớn nhất mà không chứa các phần tử liên tiếp.

def max_non_adjacent_sum(nums): # tìm tổng lớn nhất không chứa các phần tử liên tiếp
    if not nums:
        return 0
    if len(nums) == 1:  # Nếu chỉ có 1 phần tử thì trả về ph
        return nums[0]  # Trả về phần tử đó luôn là lớn nhất

    incl = nums[0]  # Tổng bao gồm phần tử hiện tại
    excl = 0        # Tổng không bao gồm phần tử hiện tại

    for i in nums[1:]:
        new_excl = max(incl, excl)  # Tổng lớn nhất trước đó
        incl = excl + i  # Bao gồm phần tử hiện tại
        excl = new_excl

    return max(incl, excl)

# Test
nums = [3, 2, 7, 10] # 3 + 7 = 10  ; 2 + 10 = 12
print(max_non_adjacent_sum(nums))  # Output: 13 (3 + 10)
