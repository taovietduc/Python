# VIẾT BẰNG PYTHON
# Bài 156: Tạo hàm tìm các từ có chung các chữ cái trong danh sách các từ cho trước.

def find_anagrams(words):
    # Tạo từ điển để lưu trữ các từ có cùng chữ cái
    anagram_dict = {}
    
    # Duyệt qua từng từ trong danh sách
    for word in words:
        # Sắp xếp các chữ cái của từ theo thứ tự và chuyển thành tuple để làm key
        sorted_word = tuple(sorted(word.lower()))
        
        # Thêm từ vào danh sách các từ có cùng chữ cái
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    # Trả về các nhóm từ có cùng chữ cái (chỉ lấy các nhóm có từ 2 từ trở lên)
    return [group for group in anagram_dict.values() if len(group) > 1]

# Test thử hàm
if __name__ == "__main__":
    # Test với một số ví dụ
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["hello", "world", "olleh"],
        ["python", "java", "typescript"]
    ]
    
    for words in test_cases:
        result = find_anagrams(words)
        print(f"\nDanh sách từ: {words}")
        if result:
            print("Các nhóm từ có chung chữ cái:")
            for group in result:
                print(group)
        else:
            print("Không có nhóm từ nào có chung chữ cái")

"""
Giải thích chi tiết:

1. Hàm find_anagrams(words):
   - Input: Một danh sách các từ
   - Output: Danh sách các nhóm từ có chung chữ cái (anagrams)

2. Các bước thực hiện:
   a) Tạo từ điển anagram_dict để lưu trữ các từ có cùng chữ cái:
      - Key: tuple các chữ cái đã sắp xếp
      - Value: danh sách các từ có cùng chữ cái

   b) Với mỗi từ trong danh sách:
      - Chuyển từ thành chữ thường và sắp xếp các chữ cái
      - Chuyển thành tuple để làm key (vì list không thể làm key của dict)
      - Thêm từ vào nhóm tương ứng trong từ điển

   c) Trả về kết quả:
      - Chỉ lấy các nhóm có từ 2 từ trở lên
      - Sử dụng list comprehension để lọc kết quả

3. Phần test:
   - Thử nghiệm với nhiều test case khác nhau
   - In ra danh sách từ gốc và các nhóm từ có chung chữ cái

4. Độ phức tạp:
   - Thời gian: O(n * k * log k), với n là số từ và k là độ dài từ dài nhất
   - Không gian: O(n * k)

5. Ví dụ:
   Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
   Output: [["eat", "tea", "ate"], ["tan", "nat"]]
   
   Giải thích:
   - "eat", "tea", "ate" có cùng chữ cái: a, e, t
   - "tan", "nat" có cùng chữ cái: a, n, t
   - "bat" không có từ nào chung chữ cái
"""
