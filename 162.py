# Viết Bằng Python
# Bài 162: Viết hàm đếm số lượng từ bắt đầu và kết thúc bằng nguyên âm trong chuỗi.

def count_vowel_words(s):
    """
    Đếm số từ bắt đầu và kết thúc bằng nguyên âm trong chuỗi
    
    Args:
        s: chuỗi cần đếm
        
    Returns:
        Số lượng từ thỏa mãn điều kiện
    """
    # Danh sách nguyên âm
    vowels = set('aeiouAEIOU')
    
    # Tách chuỗi thành các từ
    words = s.split()
    
    # Đếm số từ thỏa mãn
    count = 0
    for word in words:
        # Kiểm tra ký tự đầu và cuối có phải nguyên âm
        if word and word[0] in vowels and word[-1] in vowels:
            count += 1
            
    return count

# Test thử hàm
if __name__ == "__main__":
    test_cases = [
        "hello everyone",
        "apple inside orange",
        "this is a test",
        "eye area",
        ""
    ]
    
    for test in test_cases:
        result = count_vowel_words(test)
        print(f"Chuỗi: {test}")
        print(f"Số từ bắt đầu và kết thúc bằng nguyên âm: {result}\n")

"""
Giải thích chi tiết:

1. Hàm count_vowel_words(s):
   - Input: chuỗi s cần đếm
   - Output: số lượng từ bắt đầu và kết thúc bằng nguyên âm

2. Các bước thực hiện:
   a) Tạo tập hợp vowels chứa các nguyên âm (cả hoa và thường)
   
   b) Tách chuỗi thành các từ bằng phương thức split()
   
   c) Duyệt qua từng từ trong danh sách:
      - Kiểm tra từ không rỗng
      - Kiểm tra ký tự đầu tiên có trong tập vowels
      - Kiểm tra ký tự cuối cùng có trong tập vowels
      - Nếu thỏa mãn cả 3 điều kiện thì tăng biến đếm

3. Ví dụ:
   - "hello everyone" -> 0 từ
   - "apple inside orange" -> 2 từ (apple, inside)
   - "eye area" -> 2 từ (eye, area)
"""
