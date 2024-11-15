# VIẾT BẰNG PYTHON
# Bài 130: Tạo hàm tìm chữ cái đầu tiên không lặp lại trong một chuỗi.

def first_non_repeating_char(s): # Hàm tìm ký tự đầu tiên không lặp lại trong chuỗi s
    char_count = {}  # Tạo từ điển để đếm tần suất các ký tự

    # Đếm tần suất của mỗi ký tự
    for char in s: # Duyệt qua từng ký tự trong chuỗi s và đếm tần suất
        char_count[char] = char_count.get(char, 0) + 1 # Tăng tần suất lên 1

    # Tìm ký tự đầu tiên có tần suất là 1
    for char in s: # Duyệt qua từng ký tự trong chuỗi s và tìm ký tự đầu tiên có tần suất là 1
        if char_count[char] == 1: # Nếu tần suất của ký tự char là 1
            return char  # Trả về ký tự đầu tiên không lặp lại

    return None  # Trả về None nếu không có ký tự nào không lặp lại

# Ví dụ sử dụng
s = "aabbcde" # Chuỗi s cần kiểm tra ký tự đầu tiên không lặp lại
print("Chữ cái đầu tiên không lặp lại là:", first_non_repeating_char(s)) 
# In ra ký tự đầu tiên không lặp lại trong chuỗi s

# Kết quả:
# Chữ cái đầu tiên không lặp lại là: c
# Giải thích: Ký tự c là ký tự đầu tiên không lặp lại trong chuỗi s

