# VIẾT BẰNG PYTHON
# Bài 151: Tạo hàm tìm hai số trong danh sách sao cho tích của chúng là lớn nhất.

def find_max_product_pair(arr):
    # Kiểm tra nếu mảng có ít hơn 2 phần tử
    if len(arr) < 2:
        return None
    
    # Khởi tạo 2 số lớn nhất và 2 số nhỏ nhất
    max1 = max2 = float('-inf')  # 2 số lớn nhất
    min1 = min2 = float('inf')   # 2 số nhỏ nhất
    
    # Duyệt qua mảng để tìm 2 số lớn nhất và 2 số nhỏ nhất
    for num in arr: # Duyệt qua tất cả các phần tử của mảng
        if num > max1: # Kiểm tra nếu số hiện tại lớn hơn số lớn nhất
            max2 = max1 # Cập nhật số lớn thứ 2
            max1 = num # Cập nhật số lớn nhất
        elif num > max2: # Kiểm tra nếu số hiện tại lớn hơn số lớn thứ 2
            max2 = num # Cập nhật số lớn thứ 2
            
        if num < min1: # Kiểm tra nếu số hiện tại nhỏ hơn số nhỏ nhất
            min2 = min1 # Cập nhật số nhỏ thứ 2
            min1 = num # Cập nhật số nhỏ nhất
        elif num < min2: # Kiểm tra nếu số hiện tại nhỏ hơn số nhỏ thứ 2
            min2 = num # Cập nhật số nhỏ thứ 2
    
    # So sánh tích của 2 số lớn nhất và 2 số nhỏ nhất
    product1 = max1 * max2  # Tích 2 số dương lớn nhất
    product2 = min1 * min2  # Tích 2 số âm nhỏ nhất
    
    # Trả về cặp số có tích lớn hơn
    if product1 > product2: # Kiểm tra nếu tích 2 số dương lớn nhất lớn hơn tích 2 số âm nhỏ nhất       
        return (max1, max2) # Trả về cặp số dương lớn nhất
    return (min1, min2) # Trả về cặp số âm nhỏ nhất

# Test thử hàm
test_cases = [
    [1, 2, 3, 4, 5],           # Mảng các số dương
    [-5, -4, -3, -2, -1],      # Mảng các số âm  
    [-3, -2, 1, 2, 3],         # Mảng hỗn hợp
    [0, 1, 2, -5, -4]          # Mảng có số 0
]

for arr in test_cases: # Duyệt qua tất cả các mảng trong test_cases         
    result = find_max_product_pair(arr) # Gọi hàm tìm cặp số có tích lớn nhất
    if result: # Kiểm tra nếu kết quả khác None
        print(f"Mảng {arr}:") # In ra màn hình mảng hiện tại    
        print(f"Hai số có tích lớn nhất là {result}") # In ra màn hình hai số có tích lớn nhất
        print(f"Tích của chúng là: {result[0] * result[1]}\n") # In ra màn hình tích của hai số

"""
Giải thích chi tiết:

1. Hàm find_max_product_pair(arr):
   - Input: Mảng số nguyên arr
   - Output: Tuple chứa 2 số có tích lớn nhất

2. Các bước thực hiện:
   - Kiểm tra điều kiện mảng có ít nhất 2 phần tử
   - Khởi tạo biến:
     + max1, max2: lưu 2 số lớn nhất
     + min1, min2: lưu 2 số nhỏ nhất
   
   - Duyệt mảng để tìm:
     + 2 số lớn nhất (max1, max2)
     + 2 số nhỏ nhất (min1, min2)
   
   - So sánh:
     + Tích của 2 số dương lớn nhất
     + Tích của 2 số âm nhỏ nhất
     
   - Trả về cặp số có tích lớn hơn

3. Độ phức tạp:
   - Thời gian: O(n) với n là độ dài mảng
   - Không gian: O(1)

4. Test cases đa dạng:
   - Mảng chỉ có số dương
   - Mảng chỉ có số âm
   - Mảng có cả số âm và dương
   - Mảng có số 0
"""

