# VIẾT BẰNG PYTHON
# Bài 123: Tạo hàm tính tổng các chữ số trong chuỗi.

def sum_of_digits_in_string(s): # Hàm tính tổng các chữ số trong chuỗi s truyền vào 
    total = sum(int(char) for char in s if char.isdigit())  # Chỉ cộng các ký tự là chữ số
    return total # Trả về tổng các chữ số trong chuỗi s

# Ví dụ sử dụng
s = "a1b2c3" # Chuỗi s chứa các chữ cái và chữ số
print("Tổng các chữ số trong chuỗi là:", sum_of_digits_in_string(s)) 
# In ra tổng các chữ số trong chuỗi s là 6
 