# Viết Bằng Python
# Bài 161: Tạo hàm tìm chuỗi con có độ dài lớn nhất không chứa ký tự lặp lại.

def longest_substring_without_repeating(s):
    """
    Tìm chuỗi con dài nhất không chứa ký tự lặp lại
    
    Args:
        s: chuỗi đầu vào cần tìm
        
    Returns:
        Chuỗi con dài nhất không chứa ký tự lặp lại
    """
    # Khởi tạo các biến
    n = len(s)
    seen = {}  # Dict lưu vị trí xuất hiện gần nhất của mỗi ký tự
    start = 0  # Vị trí bắt đầu của chuỗi con hiện tại
    max_length = 0  # Độ dài lớn nhất tìm được
    max_start = 0  # Vị trí bắt đầu của chuỗi con dài nhất
    
    # Duyệt qua từng ký tự trong chuỗi
    for i in range(n):
        # Nếu ký tự đã xuất hiện và nằm sau vị trí start
        if s[i] in seen and seen[s[i]] >= start:
            # Cập nhật vị trí bắt đầu mới
            start = seen[s[i]] + 1
        else:
            # Cập nhật độ dài lớn nhất nếu chuỗi con hiện tại dài hơn
            if i - start + 1 > max_length:
                max_length = i - start + 1
                max_start = start
                
        # Lưu vị trí xuất hiện của ký tự hiện tại
        seen[s[i]] = i
        
    # Trả về chuỗi con dài nhất
    return s[max_start:max_start + max_length]

# Test thử hàm
if __name__ == "__main__":
    test_cases = [
        "abcabcbb",
        "bbbbb", 
        "pwwkew",
        "aab",
        "dvdf"
    ]
    
    for test in test_cases:
        result = longest_substring_without_repeating(test)
        print(f"Chuỗi gốc: {test}")
        print(f"Chuỗi con dài nhất không lặp: {result}")
        print(f"Độ dài: {len(result)}\n")

"""
Giải thích chi tiết:

1. Hàm longest_substring_without_repeating(s):
   - Input: chuỗi s cần tìm chuỗi con
   - Output: chuỗi con dài nhất không chứa ký tự lặp lại

2. Thuật toán sử dụng kỹ thuật cửa sổ trượt (sliding window):
   a) Sử dụng dict seen để lưu vị trí xuất hiện gần nhất của mỗi ký tự
   
   b) Duy trì một cửa sổ [start, i] không chứa ký tự lặp lại:
      - start: vị trí bắt đầu của chuỗi con hiện tại
      - i: vị trí đang xét
      
   c) Khi gặp ký tự đã xuất hiện:
      - Nếu vị trí xuất hiện trước >= start: cập nhật start mới
      - Ngược lại: mở rộng cửa sổ hiện tại
      
   d) Cập nhật độ dài lớn nhất và vị trí bắt đầu nếu cần

3. Ví dụ với "abcabcbb":
   - Bước 1: "abc" (độ dài 3)
   - Bước 2: gặp 'a' lặp -> cửa sổ mới "bca"
   - Bước 3: gặp 'b' lặp -> cửa sổ mới "cab"
   - Kết quả: "abc" (độ dài 3)
"""
