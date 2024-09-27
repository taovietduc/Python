# VIẾT BẰNG PYTHON
# Tạo danh sách từ chuỗi: Nhập một chuỗi và tạo danh sách từ chuỗi đó.

# Nhập một chuỗi từ bàn phím
chuoi = input("Nhập một chuỗi: ") # Ví dụ: "Python là ngôn ngữ lập trình phổ biến nhất"

# Tạo danh sách từ chuỗi bằng cách tách chuỗi theo khoảng trắng
danh_sach_tu = chuoi.split() # Mặc định là tách theo khoảng trắng
# Nếu muốn tách theo dấu phẩy, thì sử dụng: chuoi.split(',')

# In danh sách các từ
print(f"Danh sách các từ là: {danh_sach_tu}")

# Kêt quả
# Nhập một chuỗi: Python là ngôn ngữ lập trình phổ biến nhất
# Danh sách các từ là: ['Python', 'là', 'ngôn', 'ngữ', 'lập', 'trình', 'phổ', 'biến', 'nhất']