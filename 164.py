# Viết Bằng Python
# Bài 164: Viết hàm kiểm tra xem một chuỗi có phải là hoán vị của một chuỗi palindrome không.

def is_palindrome_permutation(s):
    # Tạo dictionary để đếm số lần xuất hiện của mỗi ký tự
    char_count = {}
    
    # Đếm số lần xuất hiện của từng ký tự trong chuỗi
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Đếm số ký tự có số lần xuất hiện lẻ
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    # Nếu độ dài chuỗi chẵn, không được có ký tự nào xuất hiện số lần lẻ
    # Nếu độ dài chuỗi lẻ, chỉ được có 1 ký tự xuất hiện số lần lẻ
    return odd_count <= 1

# Ví dụ sử dụng
print(is_palindrome_permutation("racecar"))  # True
print(is_palindrome_permutation("hello"))    # False
print(is_palindrome_permutation("aab"))      # True

"""
Giải thích chi tiết:

1. Hàm is_palindrome_permutation nhận vào một chuỗi s và kiểm tra xem nó có thể sắp xếp lại thành chuỗi palindrome không

2. Cách hoạt động:
   - Tạo dictionary char_count để đếm số lần xuất hiện của mỗi ký tự
   - Duyệt qua từng ký tự trong chuỗi và đếm số lần xuất hiện
   - Đếm số ký tự có số lần xuất hiện lẻ (odd_count)
   
3. Điều kiện để một chuỗi có thể là hoán vị của palindrome:
   - Nếu độ dài chuỗi chẵn: tất cả các ký tự phải xuất hiện số lần chẵn
   - Nếu độ dài chuỗi lẻ: chỉ được có đúng 1 ký tự xuất hiện số lần lẻ
   
4. Ví dụ:
   - "racecar" -> True vì có thể sắp xếp thành "racecar"
   - "hello" -> False vì không thể sắp xếp thành palindrome
   - "aab" -> True vì có thể sắp xếp thành "aba"
"""
