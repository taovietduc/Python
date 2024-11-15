# VIẾT BẰNG PYTHON
# Bài 129: Tạo hàm sắp xếp các chuỗi trong danh sách theo độ dài.

def sort_strings_by_length(strings): # Hàm sắp xếp chuỗi theo độ dài của chuỗi
    return sorted(strings, key=len)  # Sắp xếp danh sách theo độ dài của mỗi chuỗi

# Ví dụ sử dụng
strings = ["apple", "banana", "cherry", "kiwi", "grape"] # Danh sách chuỗi cần sắp xếp
print("Danh sách sắp xếp theo độ dài:", sort_strings_by_length(strings)) # In ra danh sách sau khi sắp xếp

# Kết quả
# ['kiwi', 'apple', 'banana', 'cherry', 'grape']
# Nhận xét: Chuỗi có độ dài ngắn nhất là "kiwi", dài nhất là "banana"
# Sắp xếp theo độ dài của chuỗi từ ngắn đến dài: ['kiwi', 'apple', 'cherry', 'grape', 'banana']