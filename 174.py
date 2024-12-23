# Viết Bằng Python
# Bài 174: Tìm danh sách con dài nhất trong danh sách mà tất cả các phần tử đều tăng dần.

def longest_increasing_subsequence(nums): # Hàm tìm dãy tăng dần dài nhất trong mảng
    if not nums:
        return []
    dp = [1] * len(nums)  # Độ dài dãy tăng dần tại mỗi phần tử
    prev = [-1] * len(nums)  # Truy vết phần tử trước đó

    for i in range(len(nums)): # Duyệt qua từng phần tử
        for j in range(i):  # Duyệt qua từng phần tử trước đó
            if nums[i] > nums[j] and dp[i] < dp[j] + 1: # Nếu phần tử i lớn hơn phần tử j và độ dài dãy tại i nhỏ hơn độ dài dãy tại j thì cập nhật lại độ dài dãy tại i
                dp[i] = dp[j] + 1 # Cập nhật độ dài dãy tại i
                prev[i] = j

    # Tìm vị trí có độ dài dãy tăng dần lớn nhất
    max_len = max(dp) # Độ dài dãy tăng dần lớn nhất
    idx = dp.index(max_len) # Vị trí có độ dài dãy tăng dần lớn nhất

    # Khôi phục dãy tăng dần
    result = [] # Dãy tăng dần
    while idx != -1:
        result.append(nums[idx])    # Thêm phần tử vào dãy tăng dần
        idx = prev[idx] # Cập nhật lại vị trí phần tử trước đó

    return result[::-1] # Trả về dãy tăng dần

# Test
nums = [10, 22, 9, 33, 21, 50, 41, 60]
print(longest_increasing_subsequence(nums))  # Output: [10, 22, 33, 50, 60]

