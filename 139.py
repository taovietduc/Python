# VIẾT BẰNG PYTHON
# Bài 139: Hàm kiểm tra chuỗi có phải là Pangram không.

def is_pangram(s): # Hàm kiểm tra chuỗi có phải là Pangram không
    # Chuyển chuỗi về chữ thường và tạo một tập hợp ký tự chữ cái
    s = s.lower() # Chuyển chuỗi về chữ thường
    alphabet = set("abcdefghijklmnopqrstuvwxyz") # Tạo tập hợp ký tự chữ cái
    return alphabet.issubset(set(s)) # Kiểm tra tập hợp ký tự chữ cái có phải là tập con của chuỗi không

# Ví dụ sử dụng
s = "The quick brown fox jumps over the lazy dog" # Chuỗi cần kiểm tra
print(f"Chuỗi có phải là Pangram không? {is_pangram(s)}") # Kết quả trả về True
