# VIẾT BẰNG PYTHON
# Bài 133: Tạo hàm chuyển đổi từ số La Mã sang số thập phân.

def roman_to_decimal(roman): # Hàm chuyển đổi số La Mã sang số thập phân
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
    # Tạo một từ điển chứa giá trị của các ký tự La Mã
    total = 0 
    prev_value = 0 
    
    # Duyệt từng ký tự trong chuỗi từ phải sang trái
    
    for char in reversed(roman): # reversed() để duyệt từ phải sang trái
        value = roman_values[char] # Lấy giá trị tương ứng của ký tự La Mã
        
        # Nếu giá trị hiện tại nhỏ hơn giá trị trước đó, trừ nó đi
        
        if value < prev_value: # Nếu giá trị hiện tại nhỏ hơn giá trị trước đó
            total -= value # Trừ giá trị hiện tại ra khỏi tổng
        else:
            total += value # Cộng giá trị hiện tại vào tổng
        
        # Cập nhật giá trị trước đó
        prev_value = value # Cập nhật giá trị trước đó bằng giá trị hiện tại
    
    return total # Trả về tổng giá trị

# Ví dụ sử dụng
roman_number = "MCMXCIV" # Số La Mã cần chuyển đổi
print(f"Số thập phân của {roman_number} là:", roman_to_decimal(roman_number)) # In kết quả

# Kết quả
# Số thập phân của MCMXCIV là: 1994
