# VIẾT BẰNG PYTHON
# Bài 70: Tạo hàm tính trung bình của danh sách.

def tinh_trung_binh(danh_sach): # Hàm tính trung bình với tham số danh_sach
    return sum(danh_sach) / len(danh_sach) # Trả về giá trị trung bình của danh sách

# Nhập danh sách các số từ người dùng
danh_sach = list(map(int, input("Nhập các số, cách nhau bằng dấu cách: ").split())) # Nhập danh sách các số từ bàn phím
# Tính trung bình và in kết quả
trung_binh = tinh_trung_binh(danh_sach) # Gọi hàm và lưu kết quả vào biến
print("Giá trị trung bình của danh sách là:", trung_binh) # In kết quả
