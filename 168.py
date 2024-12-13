# Viết Bằng Python
# Bài 168: Viết hàm tách một danh sách thành hai danh sách con, một chứa số chẵn và một chứa số lẻ.

def split_even_odd(numbers):    # Hàm tách danh sách thành số chẵn và lẻ
    even_numbers = []  # Danh sách chứa số chẵn
    odd_numbers = []   # Danh sách chứa số lẻ
    
    for num in numbers: # Duyệt qua từng số trong danh sách
        if num % 2 == 0:  # Kiểm tra số chẵn
            even_numbers.append(num)  # Thêm vào danh sách chẵn
        else:
            odd_numbers.append(num)   # Thêm vào danh sách lẻ
    
    return even_numbers, odd_numbers # Trả về danh sách chẵn và lẻ

# Ví dụ sử dụng
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # Danh sách số
even, odd = split_even_odd(numbers) # Tách danh sách thành số chẵn và lẻ
print(f"Số chẵn: {even}")   # In ra danh sách số chẵn
print(f"Số lẻ: {odd}")    # In ra danh sách số lẻ
