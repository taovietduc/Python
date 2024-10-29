# VIẾT BẰNG PYTHON
# Bài 71: Tạo hàm thêm phần tử vào từ điển.

def them_vao_tu_dien(tu_dien, khoa, gia_tri): 
# Hàm thêm phần tử vào từ điển với khóa và giá trị được truyền vào từ tham số
    tu_dien[khoa] = gia_tri # Thêm phần tử vào từ điển với khóa và giá trị được truyền vào
    return tu_dien # Trả về từ điển sau khi thêm phần tử vào từ điển

# Tạo một từ điển trống
tu_dien = {} # Khởi tạo một từ điển trống

# Nhập khóa và giá trị từ bàn phím
khoa = input("Nhập khóa: ")  # Nhập khóa từ bàn phím 
gia_tri = input("Nhập giá trị: ") # Nhập giá trị từ bàn phím 

# Thêm phần tử vào từ điển và in kết quả 
tu_dien = them_vao_tu_dien(tu_dien, khoa, gia_tri) # Gọi hàm thêm phần tử vào từ điển 
print("Từ điển sau khi thêm:", tu_dien) # In từ điển sau khi thêm phần tử vào từ điển
