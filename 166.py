# Viết Bằng Python
# Bài 166: Tạo hàm kiểm tra xem hai chuỗi có chứa cùng tập hợp các ký tự hay không.

def have_same_characters(str1, str2):
    # Chuyển chuỗi thứ nhất thành một tập hợp ký tự duy nhất.
    # Ví dụ: "abcabc" -> {'a', 'b', 'c'}
    set1 = set(str1)

    # Chuyển chuỗi thứ hai thành một tập hợp ký tự duy nhất.
    # Ví dụ: "cba" -> {'a', 'b', 'c'}
    set2 = set(str2)

    # So sánh hai tập hợp. Nếu chúng bằng nhau, nghĩa là hai chuỗi
    # chứa cùng một tập hợp ký tự, bất kể thứ tự.
    return set1 == set2


# Kiểm tra thử với các ví dụ minh họa
# Ví dụ 1: Chuỗi "abc" và "cba" chứa cùng các ký tự {'a', 'b', 'c'} => Kết quả: True
print(have_same_characters("abc", "cba"))   # True

# Ví dụ 2: Chuỗi "abc" chứa {'a', 'b', 'c'}, nhưng "abcd" chứa thêm ký tự 'd' => Kết quả: False
print(have_same_characters("abc", "abcd")) # False

# Ví dụ 3: Chuỗi "xyz" và "zxy" chứa cùng các ký tự {'x', 'y', 'z'} => Kết quả: True
print(have_same_characters("xyz", "zxy"))  # True
