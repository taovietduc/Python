# VIẾT BẰNG PYTHON
# Bài 106: Tạo hàm kiểm tra hai chuỗi có phải là anagram hay không.

def kiem_tra_anagram(s1, s2):
    # Loại bỏ khoảng trắng và chuyển chuỗi về dạng chữ thường
    s1 = s1.replace(" ", "").lower() # replace(" ", "") để loại bỏ khoảng trắng trong chuỗi
    s2 = s2.replace(" ", "").lower() # lower() để chuyển chuỗi về dạng chữ thường (lowercase)

    # Kiểm tra độ dài của hai chuỗi
    if len(s1) != len(s2): # Nếu độ dài của hai chuỗi khác nhau thì không thể là anagram
        return False # Trả về False

    # Sắp xếp ký tự và so sánh
    return sorted(s1) == sorted(s2) # Sắp xếp ký tự của hai chuỗi và so sánh xem có giống nhau không

# Ví dụ sử dụng
chuoi1 = input("Nhập chuỗi thứ nhất: ") # Nhập chuỗi thứ nhất
chuoi2 = input("Nhập chuỗi thứ hai: ") # Nhập chuỗi thứ hai

if kiem_tra_anagram(chuoi1, chuoi2):    # Nếu hai chuỗi là anagram    
    print("Hai chuỗi là anagram.")     # In ra  
else:  # Nếu hai chuỗi không phải là anagram
    print("Hai chuỗi không phải là anagram.") # In ra
