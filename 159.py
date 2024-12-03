# Viết Bằng Python
# Bài 159: Tìm số lần xuất hiện của một từ bất kỳ trong một chuỗi mà không phân biệt chữ hoa/chữ thường.

def count_word_occurrences(text, word):
    """
    Đếm số lần xuất hiện của một từ trong chuỗi, không phân biệt chữ hoa/thường
    
    Args:
        text: chuỗi văn bản cần tìm kiếm
        word: từ cần đếm số lần xuất hiện
        
    Returns:
        Số lần xuất hiện của từ trong chuỗi
    """
    # Chuyển cả chuỗi và từ cần tìm về chữ thường
    text = text.lower()
    word = word.lower()
    
    # Tách chuỗi thành danh sách các từ
    words = text.split()
    
    # Đếm số lần xuất hiện của từ
    count = words.count(word)
    
    return count

# Test thử hàm
if __name__ == "__main__":
    # Một số ví dụ test
    test_cases = [
        ("Hello World Hello Python Hello", "hello"),
        ("The Quick Brown Fox Jumps Over The Brown Dog", "brown"),
        ("Python is amazing, PYTHON is fun, Python is powerful", "python")
    ]
    
    for text, word in test_cases:
        count = count_word_occurrences(text, word)
        print(f"\nVăn bản: {text}")
        print(f"Từ cần tìm: {word}")
        print(f"Số lần xuất hiện: {count}")

"""
Giải thích chi tiết:

1. Hàm count_word_occurrences(text, word):
   - Input: 
     + text: chuỗi văn bản cần tìm kiếm
     + word: từ cần đếm số lần xuất hiện
   - Output: số lần xuất hiện của từ trong chuỗi

2. Các bước thực hiện:
   a) Xử lý không phân biệt chữ hoa/thường:
      - Chuyển cả văn bản và từ cần tìm về chữ thường bằng lower()
      - Điều này đảm bảo "Hello", "HELLO", "hello" được xem là giống nhau

   b) Tách văn bản thành các từ:
      - Sử dụng split() để tách chuỗi thành list các từ
      - Mặc định split() tách theo khoảng trắng

   c) Đếm số lần xuất hiện:
      - Sử dụng phương thức count() của list để đếm số lần xuất hiện của từ
      - count() trả về số lần một phần tử xuất hiện trong list

3. Ví dụ:
   Input: 
   - text: "Hello World Hello Python Hello"
   - word: "hello"
   
   Các bước:
   - Sau lower(): "hello world hello python hello"
   - Sau split(): ["hello", "world", "hello", "python", "hello"]
   - count("hello"): 3
"""

