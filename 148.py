# VIẾT BẰNG PYTHON
# Bài 148:Viết hàm kiểm tra xem một chuỗi có thể chuyển thành chuỗi palindrome với tối đa một lần xóa ký tự không.

def is_palindrome(s, start, end): # Hàm kiểm tra chuỗi có phải palindrome từ vị trí start đến end
    # Kiểm tra chuỗi có phải palindrome từ vị trí start đến end
    while start < end: # Duyệt từ 2 đầu vào giữa 
        if s[start] != s[end]: # Nếu ký tự khác nhau
            return False # Trả về False
        start += 1 # Tăng start lên 1
        end -= 1 # Giảm end đi 1
    return True

def can_be_palindrome(s): # Hàm kiểm tra chuỗi có thể chuyển thành palindrome với tối đa 1 lần xóa ký tự    
    # Kiểm tra chuỗi rỗng
    if not s:  # Nếu chuỗi rỗng
        return True # Trả về True
        
    start = 0 # Vị trí đầu
    end = len(s) - 1 # Vị trí cuối
    
    # Duyệt từ 2 đầu vào giữa
    while start < end:
        if s[start] != s[end]: # Nếu ký tự khác nhau
            # Thử xóa 1 trong 2 ký tự
            # và kiểm tra phần còn lại có phải palindrome không
            return is_palindrome(s, start + 1, end) or is_palindrome(s, start, end - 1)
        start += 1 # Tăng start lên 1
        end -= 1 # Giảm end đi 1
        
    return True # Trả về True

# Test thử hàm
test_cases = [
    "abba",     # True - đã là palindrome
    "abca",     # True - xóa 'c' -> "aba" 
    "abcd",     # False - không thể tạo palindrome
    "aaa",      # True - đã là palindrome
    "abc",      # False - không thể tạo palindrome
]

for i, s in enumerate(test_cases, 1): # Duyệt từng test case
    result = can_be_palindrome(s) # Gọi hàm kiểm tra chuỗi có thể chuyển thành palindrome với tối đa 1 lần xóa ký tự
    print(f"\nTest {i}:") # In ra test thứ i
    print(f"Chuỗi: {s}") # In ra chuỗi
    print(f"Có thể tạo palindrome bằng cách xóa tối đa 1 ký tự: {result}") # In ra kết quả

"""
Giải thích chi tiết:

1. Hàm is_palindrome(s, start, end):
   - Input: chuỗi s và vị trí bắt đầu, kết thúc cần kiểm tra
   - Kiểm tra chuỗi có phải palindrome từ vị trí start đến end không
   - So sánh các ký tự đối xứng, nếu khác nhau -> False
   - Nếu duyệt hết mà các cặp đều giống nhau -> True

2. Hàm can_be_palindrome(s):
   - Input: chuỗi s cần kiểm tra
   - Duyệt từ 2 đầu vào giữa, so sánh các ký tự đối xứng:
     + Nếu giống nhau -> tiếp tục
     + Nếu khác nhau -> thử xóa 1 trong 2 ký tự và kiểm tra phần còn lại
   - Trả về True nếu có thể tạo palindrome, False nếu không thể

3. Kết quả test:
   "abba" -> True (đã là palindrome)
   "abca" -> True (xóa 'c' -> "aba")
   "abcd" -> False (không thể tạo palindrome)
   "aaa" -> True (đã là palindrome) 
   "abc" -> False (không thể tạo palindrome)
"""
