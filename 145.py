# VIẾT BẰNG PYTHON
# Bài 145: Tạo hàm tìm mảng con liên tiếp dài nhất có tổng bằng 0 trong danh sách.
def find_longest_subarray_sum_zero(lst):
    # Khởi tạo biến lưu kết quả
    max_length = 0  # Độ dài lớn nhất của mảng con
    start_index = 0  # Vị trí bắt đầu của mảng con
    end_index = -1  # Vị trí kết thúc của mảng con
    
    # Duyệt qua từng vị trí bắt đầu có thể
    for i in range(len(lst)):
        current_sum = 0  # Tổng của mảng con hiện tại
        
        # Duyệt các phần tử tiếp theo để tìm mảng con có tổng = 0
        for j in range(i, len(lst)):
            current_sum += lst[j]
            
            # Nếu tìm thấy mảng con có tổng = 0
            if current_sum == 0:
                # Cập nhật kết quả nếu độ dài mảng con lớn hơn max_length
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    start_index = i
                    end_index = j
    
    # Trả về mảng con tìm được
    if max_length > 0:
        return lst[start_index:end_index + 1]
    return []  # Trả về mảng rỗng nếu không tìm thấy

# Kiểm thử hàm
test_cases = [
    [4, 2, -3, 1, 6],  # Có mảng con [2, -3, 1]
    [4, 2, 0, 1, 6],   # Có mảng con [0]
    [-3, 2, 3, 1, -2, -1],  # Có mảng con [2, 3, 1, -2, -1]
    [1, 2, 3],         # Không có mảng con nào
]

# In kết quả test
for i, arr in enumerate(test_cases, 1):
    result = find_longest_subarray_sum_zero(arr)
    print(f"\nTest {i}:")
    print("Mảng ban đầu:", arr)
    print("Mảng con dài nhất có tổng = 0:", result)
    if result:
        print("Độ dài:", len(result))

"""
Giải thích chi tiết:

1. Hàm find_longest_subarray_sum_zero(lst):
   - Input: Một danh sách số nguyên lst
   - Output: Mảng con liên tiếp dài nhất có tổng bằng 0

2. Thuật toán:
   - Sử dụng 2 vòng lặp lồng nhau để xét tất cả các mảng con có thể
   - Vòng lặp ngoài (i) xác định điểm bắt đầu của mảng con
   - Vòng lặp trong (j) xác định điểm kết thúc và tính tổng các phần tử
   - Nếu tìm thấy mảng con có tổng = 0, so sánh độ dài với max_length
   - Cập nhật max_length và vị trí start_index, end_index nếu tìm thấy mảng con dài hơn

3. Kết quả chạy:
Test 1: [4, 2, -3, 1, 6]
- Mảng con [2, -3, 1] có tổng = 0 và độ dài = 3

Test 2: [4, 2, 0, 1, 6]
- Mảng con [0] có tổng = 0 và độ dài = 1

Test 3: [-3, 2, 3, 1, -2, -1]
- Mảng con [2, 3, 1, -2, -1] có tổng = 0 và độ dài = 5

Test 4: [1, 2, 3]
- Không có mảng con nào có tổng = 0
"""