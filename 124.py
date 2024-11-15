# VIẾT BẰNG PYTHON
# Bài 124: Tạo hàm tìm chữ cái xuất hiện nhiều nhất trong một chuỗi.

from collections import Counter

def most_frequent_letter(s): # Hàm tìm chữ cái xuất hiện nhiều nhất trong chuỗi s
    s = s.lower()  # Đổi tất cả chữ cái thành chữ thường để không phân biệt hoa thường
    letters = [char for char in s if char.isalpha()]  # Lọc ra các chữ cái
    if not letters:  # Nếu không có chữ cái nào
        return None # Trả về None (không có chữ cái nào xuất hiện)
    frequency = Counter(letters)  # Đếm tần suất xuất hiện của mỗi chữ cái
    most_common_letter = frequency.most_common(1)[0][0]  # Lấy chữ cái xuất hiện nhiều nhất
    return most_common_letter # Trả về chữ cái xuất hiện nhiều nhất

# Ví dụ sử dụng
s = "Hello World!" # Chuỗi cần kiểm tra chữ cái xuất hiện nhiều nhất
print("Chữ cái xuất hiện nhiều nhất là:", most_frequent_letter(s)) 
# Kết quả: l (xuất hiện 3 lần)
