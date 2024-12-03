# Viết Bằng Python
# Bài 163: Tạo hàm tìm tất cả các cặp từ trong danh sách mà khi kết hợp lại tạo thành palindrome.

def find_palindrome_pairs(words):
    """
    Tìm tất cả các cặp từ trong danh sách mà khi kết hợp tạo thành palindrome
    
    Args:
        words: Danh sách các từ cần kiểm tra
        
    Returns:
        List các cặp từ tạo thành palindrome
    """
    result = []
    
    # Duyệt qua từng cặp từ trong danh sách
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:  # Không xét cùng một từ
                # Kết hợp 2 từ
                combined = words[i] + words[j]
                
                # Kiểm tra xem có phải palindrome không
                if is_palindrome(combined):
                    result.append((words[i], words[j]))
                    
    return result

def is_palindrome(s):
    """
    Kiểm tra một chuỗi có phải palindrome không
    """
    return s == s[::-1]

# Ví dụ sử dụng
words = ["abc", "cba", "ab", "ba", "xyz", "zyx"]
palindrome_pairs = find_palindrome_pairs(words)
print("Các cặp từ tạo thành palindrome:")
for pair in palindrome_pairs:
    print(f"{pair[0]} + {pair[1]} = {pair[0] + pair[1]}")

"""
Giải thích chi tiết:

1. Hàm find_palindrome_pairs:
   - Nhận vào một danh sách các từ
   - Sử dụng 2 vòng lặp lồng nhau để xét từng cặp từ
   - Với mỗi cặp từ, kết hợp chúng lại và kiểm tra xem có tạo thành palindrome không
   - Nếu tạo thành palindrome thì thêm cặp từ đó vào kết quả

2. Hàm is_palindrome:
   - Kiểm tra một chuỗi có phải palindrome không
   - Sử dụng kỹ thuật cắt chuỗi s[::-1] để đảo ngược chuỗi
   - So sánh chuỗi gốc với chuỗi đảo ngược

3. Ví dụ:
   - Với input ["abc", "cba", "ab", "ba", "xyz", "zyx"]
   - Kết quả sẽ có các cặp như:
     + "abc" + "cba" = "abccba" (palindrome)
     + "ab" + "ba" = "abba" (palindrome)
     + "xyz" + "zyx" = "xyzzyx" (palindrome)
"""
