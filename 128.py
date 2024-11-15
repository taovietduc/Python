# VIẾT BẰNG PYTHON
# Bài 128: Tạo hàm tìm số lẻ nhỏ nhất trong danh sách.

def smallest_odd_number(numbers):# Hàm tìm số lẻ nhỏ nhất trong danh sách
    odd_numbers = [num for num in numbers if num % 2 != 0]  # Lọc ra các số lẻ
    if odd_numbers: # Nếu có số lẻ trong danh sách thì trả về số lẻ nhỏ nhất
        return min(odd_numbers)  # Trả về số lẻ nhỏ nhất
    return None  # Trả về None nếu không có số lẻ

# Ví dụ sử dụng
numbers = [2, 4, 6, 7, 10, 9, 3] # Danh sách số nguyên dương bất kỳ
print("Số lẻ nhỏ nhất là:", smallest_odd_number(numbers)) # Số lẻ nhỏ nhất là: 3 

# Kết quả: Số lẻ nhỏ nhất là: 3 
# Như vậy số lẻ nhỏ nhất trong danh sách trên là 3
