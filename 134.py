# VIẾT BẰNG PYTHON
# Bài 134: Tạo hàm chuyển đổi từ số thập phân sang số La Mã.

def decimal_to_roman(num): # Hàm chuyển đổi từ số thập phân sang số La Mã
    # Danh sách các cặp giá trị thập phân và ký tự La Mã
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), # 1000, 900, 500, 400
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), # 100, 90, 50, 40
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I') # 10, 9, 5, 4, 1
    ]
    
    roman = "" # Chuỗi kết quả chứa số La Mã
    for value, symbol in roman_numerals: # Duyệt qua các cặp giá trị thập phân và ký tự La Mã
        while num >= value: # Nếu số thập phân lớn hơn hoặc bằng giá trị thập phân
            roman += symbol # Thêm ký tự La Mã vào chuỗi kết quả
            num -= value # Giảm giá trị thập phân đi giá trị thập phân tương ứng
    return roman

# Ví dụ sử dụng
decimal_number = 1994 # Số thập phân cần chuyển đổi sang số La Mã
print(f"Số La Mã của {decimal_number} là:", decimal_to_roman(decimal_number)) # In kết quả'

# Kết quả 
# Số La Mã của 1994 là: MCMXCIV
