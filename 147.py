# VIẾT BẰNG PYTHON
# Bài 147: Tạo hàm tính tổng các số cách đều nhau trong danh sách với khoảng cách cho trước.

def sum_numbers_with_distance(lst, k):
    # Kiểm tra danh sách rỗng hoặc k không hợp lệ
    if not lst or k <= 0: 
        return 0 # Nếu danh sách rỗng hoặc k <= 0 thì trả về 0 
        
    total = 0  # Biến lưu tổng các số
    
    # Duyệt từ phần tử đầu tiên, cách nhau k phần tử
    for i in range(0, len(lst), k): # Duyệt từ phần tử đầu tiên, cách nhau k phần tử
        total += lst[i]  # Cộng phần tử vào tổng
        
    return total  # Trả về tổng

# Kiểm thử hàm
test_cases = [
    ([1, 2, 3, 4, 5], 2),  # Tổng các số cách 2 vị trí: 1 + 3 + 5 = 9
    ([1, 2, 3, 4, 5, 6], 3),  # Tổng các số cách 3 vị trí: 1 + 4 = 5 
    ([2, 5, 8, 1, 9, 3, 7], 2),  # Tổng các số cách 2 vị trí: 2 + 8 + 9 + 7 = 26
]

# In kết quả test
for i, (arr, k) in enumerate(test_cases, 1): # Duyệt từng test case
    result = sum_numbers_with_distance(arr, k) # Gọi hàm tính tổng các số cách đều nhau với khoảng cách k   
    print(f"\nTest {i}:") # In ra test thứ i 
    print(f"Mảng: {arr}") # In ra mảng 
    print(f"Khoảng cách k = {k}") # In ra khoảng cách k 
    print(f"Tổng các số cách {k} vị trí: {result}") # In ra kết quả tổng các số cách k vị trí 

"""
Giải thích chi tiết:

1. Hàm sum_numbers_with_distance(lst, k):
   - Input: 
     + lst: Danh sách số nguyên
     + k: Khoảng cách giữa các số cần tính tổng
   - Output: Tổng các số cách đều nhau k vị trí

2. Thuật toán:
   - Kiểm tra điều kiện đầu vào:
     + Nếu danh sách rỗng hoặc k <= 0 thì trả về 0
   - Khởi tạo biến total = 0 để lưu tổng
   - Sử dụng vòng lặp for với bước nhảy k:
     + Duyệt từ index 0, cách nhau k vị trí
     + Cộng dồn các phần tử vào total
   - Trả về tổng total

3. Kết quả chạy:
Test 1: [1, 2, 3, 4, 5], k = 2
- Các số cách 2 vị trí: 1, 3, 5
- Tổng = 1 + 3 + 5 = 9

Test 2: [1, 2, 3, 4, 5, 6], k = 3  
- Các số cách 3 vị trí: 1, 4
- Tổng = 1 + 4 = 5

Test 3: [2, 5, 8, 1, 9, 3, 7], k = 2
- Các số cách 2 vị trí: 2, 8, 9, 7
- Tổng = 2 + 8 + 9 + 7 = 26
"""
