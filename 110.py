# VIẾT BẰNG PYTHON
# Bài 110: Tạo hàm kiểm tra một số có phải là số palindrome không.

def is_palindrome(num):
 
    # Kiểm tra xem một số có phải là số palindrome hay không.

    # Parameters:
    # num (int): Số nguyên cần kiểm tra.

    # Returns:
    # bool: True nếu số là palindrome, False nếu không.

    # Chuyển số thành chuỗi
    str_num = str(num)
    # Kiểm tra chuỗi có giống nhau khi đảo ngược hay không
    return str_num == str_num[::-1]

# Ví dụ sử dụng
number = 12321
if is_palindrome(number): # True nếu là số palindrome 
    print(f"{number} là số palindrome.")
else: # False nếu không phải là số palindrome
    print(f"{number} không phải là số palindrome.")
