# Viết Bằng Python
# Bài 160: Viết hàm chuyển đổi một chuỗi từ định dạng camelCase sang snake_case.

def camel_to_snake(camel_str):
    """
    Chuyển đổi chuỗi từ định dạng camelCase sang snake_case
    
    Args:
        camel_str: chuỗi ở định dạng camelCase cần chuyển đổi
        
    Returns:
        Chuỗi đã được chuyển đổi sang định dạng snake_case
    """
    # Khởi tạo chuỗi snake_case rỗng
    snake_str = camel_str[0].lower()
    
    # Duyệt qua từng ký tự từ vị trí thứ 2
    for char in camel_str[1:]:
        if char.isupper():
            # Nếu gặp chữ hoa, thêm dấu gạch dưới và chuyển thành chữ thường
            snake_str += '_' + char.lower()
        else:
            # Nếu là chữ thường thì giữ nguyên
            snake_str += char
            
    return snake_str

# Test thử hàm
if __name__ == "__main__":
    test_cases = [
        "camelCase",
        "thisIsAVariable",
        "convertToSnakeCase",
        "simpleXML",
        "PDFLoader"
    ]
    
    for test in test_cases:
        result = camel_to_snake(test)
        print(f"camelCase: {test}")
        print(f"snake_case: {result}\n")

"""
Giải thích chi tiết:

1. Hàm camel_to_snake(camel_str):
   - Input: chuỗi ở định dạng camelCase
   - Output: chuỗi đã chuyển sang định dạng snake_case

2. Các bước thực hiện:
   a) Khởi tạo chuỗi kết quả với ký tự đầu tiên đã chuyển thành chữ thường
   
   b) Duyệt qua các ký tự còn lại trong chuỗi:
      - Nếu gặp chữ hoa (isupper()), thêm dấu '_' và chuyển thành chữ thường
      - Nếu là chữ thường, giữ nguyên
      
   c) Ví dụ chuyển đổi:
      - "camelCase" -> "camel_case"
      - "thisIsAVariable" -> "this_is_a_variable"
      - "PDFLoader" -> "pdf_loader"

3. Test cases đa dạng để kiểm tra các trường hợp:
   - Chuỗi camelCase thông thường
   - Chuỗi có nhiều chữ hoa liên tiếp
   - Chuỗi bắt đầu bằng chữ hoa
"""
