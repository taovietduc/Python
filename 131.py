# VIẾT BẰNG PYTHON
# Bài 131: Tạo hàm đếm số lần xuất hiện của một ký tự trong chuỗi.

def count_char_occurrences(s, char): # Hàm đếm số lần xuất hiện của ký tự
    return s.count(char)  # Sử dụng hàm count có sẵn để đếm số lần xuất hiện của ký tự

# Ví dụ sử dụng
s = "hello world" # Chuỗi cần kiểm tra số lần xuất hiện của ký tự
char = "o" # Ký tự cần kiểm tra số lần xuất hiện trong chuỗi
print(f"Số lần xuất hiện của '{char}' trong chuỗi là:", count_char_occurrences(s, char)) 
# In ra số lần xuất hiện của ký tự trong chuỗi 

# Kết quả
# Số lần xuất hiện của 'o' trong chuỗi là: 2
# Như vậy ký tự 'o' xuất hiện 2 lần trong chuỗi "hello world"