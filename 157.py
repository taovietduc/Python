# VIẾT BẰNG PYTHON
# Bài 157: Viết hàm đảo ngược các từ trong một câu nhưng giữ nguyên thứ tự các chữ cái trong mỗi từ.

def reverse_words(sentence):
    # Tách câu thành danh sách các từ
    words = sentence.split()
    
    # Đảo ngược thứ tự các từ trong danh sách
    words = words[::-1]
    
    # Nối các từ lại thành câu mới
    return ' '.join(words)

# Test thử hàm
if __name__ == "__main__":
    # Test với một số ví dụ
    test_cases = [
        "Hello World Python",
        "I love programming",
        "Keep calm and code on"
    ]
    
    for sentence in test_cases:
        result = reverse_words(sentence)
        print(f"\nCâu gốc: {sentence}")
        print(f"Câu sau khi đảo ngược: {result}")

"""
Giải thích chi tiết:

1. Hàm reverse_words(sentence):
   - Input: Một chuỗi (câu)
   - Output: Chuỗi mới với thứ tự các từ bị đảo ngược

2. Các bước thực hiện:
   a) Tách câu thành danh sách các từ:
      - Sử dụng phương thức split() để tách câu thành list các từ
      - Mặc định split() sẽ tách theo khoảng trắng

   b) Đảo ngược thứ tự các từ:
      - Sử dụng cú pháp slicing words[::-1] để đảo ngược list
      - Điều này không ảnh hưởng đến thứ tự các chữ cái trong mỗi từ

   c) Nối các từ lại thành câu:
      - Sử dụng phương thức join() để nối các từ lại với nhau
      - Các từ được nối bằng khoảng trắng ' '.join()

3. Ví dụ:
   Input: "Hello World Python"
   - Sau split(): ["Hello", "World", "Python"]
   - Sau đảo ngược: ["Python", "World", "Hello"]
   - Sau join(): "Python World Hello"
"""
