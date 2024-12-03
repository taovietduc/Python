# Viết Bằng Python
# Bài 165: Viết hàm mã hóa một chuỗi bằng cách thay thế mỗi ký tự thành ký tự tiếp theo trong bảng chữ cái (vòng lặp từ 'z' về 'a').

def encode_string(s):
    """
    Hàm mã hóa chuỗi bằng cách thay thế mỗi ký tự thành ký tự tiếp theo trong bảng chữ cái
    
    Args:
        s: chuỗi đầu vào cần mã hóa
        
    Returns:
        chuỗi đã được mã hóa
    """
    result = ""
    for char in s:
        # Kiểm tra nếu là chữ cái
        if char.isalpha():
            # Lấy mã ASCII của ký tự
            ascii_val = ord(char)
            
            # Xử lý chữ thường
            if char.islower():
                # Nếu là 'z' thì quay về 'a'
                if char == 'z':
                    result += 'a'
                else:
                    # Thay thế bằng ký tự kế tiếp
                    result += chr(ascii_val + 1)
                    
            # Xử lý chữ hoa        
            else:
                # Nếu là 'Z' thì quay về 'A' 
                if char == 'Z':
                    result += 'A'
                else:
                    # Thay thế bằng ký tự kế tiếp
                    result += chr(ascii_val + 1)
        else:
            # Giữ nguyên các ký tự không phải chữ cái
            result += char
            
    return result

# Test thử hàm
test_str = "Hello World! Z z"
print("Chuỗi gốc:", test_str)
print("Chuỗi sau khi mã hóa:", encode_string(test_str))
