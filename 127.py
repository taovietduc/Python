# VIẾT BẰNG PYTHON
# Bài 127: Tạo hàm tìm số chẵn lớn nhất trong danh sách.

def largest_even_number(numbers):  # Hàm tìm số chẵn lớn nhất trong danh sách số nguyên
    even_numbers = [num for num in numbers if num % 2 == 0]  # Lọc ra các số chẵn
    if even_numbers: # Kiểm tra xem có số chẵn nào không trong danh sách
        return max(even_numbers)  # Trả về số chẵn lớn nhất
    return None  # Trả về None nếu không có số chẵn

# Ví dụ sử dụng
numbers = [1, 3, 5, 6, 8, 10, 7] # Danh sách số nguyên
print("Số chẵn lớn nhất là:", largest_even_number(numbers)) # Số chẵn lớn nhất là: 10 

# Kết quả: Số chẵn lớn nhất là: 10
# Lưu ý: Nếu không có số chẵn nào trong danh sách thì hàm trả về None
# Ví dụ: numbers = [1, 3, 5, 7] thì hàm trả về None
# Ví dụ: numbers = [1, 3, 5, 7, 9] thì hàm trả về None
