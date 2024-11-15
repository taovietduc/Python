# VIẾT BẰNG PYTHON
# Bài 142: Tính trung bình cộng của các số chẵn trong danh sách.

def average_even_numbers(lst):  # Hàm tính trung bình cộng của các số chẵn trong danh sách
    even_numbers = [num for num in lst if num % 2 == 0] # Lọc ra các số chẵn trong danh sách
    if not even_numbers: # Nếu không có số chẵn nào thì trả về 0
        return 0 
    return sum(even_numbers) / len(even_numbers) # Trả về trung bình cộng của các số chẵn trong danh sách

# Ví dụ sử dụng
lst = [1, 2, 3, 4, 5, 6] # Danh sách số nguyên dương 
print("Trung bình cộng của các số chẵn:", average_even_numbers(lst))

# Kết quả
# Trung bình cộng của các số chẵn: 3.0 
# Giải thích: Trung bình cộng của các số chẵn trong danh sách là (2 + 4 + 6) / 3 = 12 / 3 = 4.0

