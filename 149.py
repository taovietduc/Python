# VIẾT BẰNG PYTHON
# Bài 149: Tạo hàm tìm độ dài dãy con đơn điệu dài nhất (tăng hoặc giảm) trong danh sách.

def longest_monotonic_subarray(arr):
    if not arr:  # Nếu mảng rỗng
        return 0  # Trả về 0
        
    n = len(arr)  # Lấy độ dài mảng
    # Khởi tạo mảng lưu độ dài dãy con tăng và giảm tại mỗi vị trí
    inc = [1] * n  # Mảng lưu độ dài dãy con tăng
    dec = [1] * n  # Mảng lưu độ dài dãy con giảm
    
    # Tìm độ dài dãy con tăng dài nhất kết thúc tại mỗi vị trí
    for i in range(1, n):
        if arr[i] > arr[i-1]:  # Nếu phần tử hiện tại lớn hơn phần tử trước
            inc[i] = inc[i-1] + 1  # Độ dài dãy con tăng tăng thêm 1
            
    # Tìm độ dài dãy con giảm dài nhất kết thúc tại mỗi vị trí        
    for i in range(1, n):
        if arr[i] < arr[i-1]:  # Nếu phần tử hiện tại nhỏ hơn phần tử trước
            dec[i] = dec[i-1] + 1  # Độ dài dãy con giảm tăng thêm 1
            
    # Trả về độ dài lớn nhất giữa dãy con tăng và giảm
    return max(max(inc), max(dec))

# Test thử hàm
test_cases = [
    [1, 2, 3, 1, 2],  # Dãy con tăng dài nhất: [1,2,3]
    [5, 4, 3, 2, 1],  # Dãy con giảm dài nhất: [5,4,3,2,1]
    [1, 2, 2, 3],     # Dãy con tăng dài nhất: [1,2,3]
    [1],              # Một phần tử
    []                # Mảng rỗng
]

# In kết quả test
for i, arr in enumerate(test_cases, 1): # Duyệt qua các test case
    result = longest_monotonic_subarray(arr) # Tìm dãy con đơn điệu dài nhất
    print(f"\nTest {i}:") # In ra test case thứ i 
    print(f"Mảng: {arr}")   # In ra mảng test
    print(f"Độ dài dãy con đơn điệu dài nhất: {result}") # In ra kết quả tìm được

"""
Giải thích chi tiết:

1. Hàm longest_monotonic_subarray(arr):
   - Input: Mảng số nguyên arr
   - Output: Độ dài dãy con đơn điệu (tăng hoặc giảm) dài nhất

2. Thuật toán:
   - Kiểm tra mảng rỗng -> trả về 0
   - Khởi tạo 2 mảng inc và dec để lưu độ dài dãy con tăng và giảm
   - Duyệt mảng:
     + Nếu arr[i] > arr[i-1]: cập nhật độ dài dãy con tăng
     + Nếu arr[i] < arr[i-1]: cập nhật độ dài dãy con giảm
   - Trả về giá trị lớn nhất giữa max(inc) và max(dec)

3. Kết quả test:
   [1,2,3,1,2] -> 3 (dãy con tăng [1,2,3])
   [5,4,3,2,1] -> 5 (dãy con giảm [5,4,3,2,1])
   [1,2,2,3] -> 3 (dãy con tăng [1,2,3])
   [1] -> 1
   [] -> 0
"""
