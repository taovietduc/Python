# VIẾT BẰNG PYTHON
# Bài 72: Tạo hàm xóa phần tử khỏi từ điển.

def xoa_phan_tu(tu_dien, khoa): # Hàm xóa phần tử khỏi từ điển theo khóa cho trước 
    if khoa in tu_dien: # Kiểm tra xem khóa có tồn tại trong từ điển không
        del tu_dien[khoa] # Nếu có thì xóa phần tử có khóa đó
        print(f"Đã xóa khóa '{khoa}' khỏi từ điển.") # In thông báo
    else:
        print(f"Khóa '{khoa}' không tồn tại trong từ điển.") # Nếu không thì in thông báo
    return tu_dien # Trả về từ điển sau khi xóa

# Tạo một từ điển mẫu
tu_dien = {'apple': 3, 'banana': 2, 'orange': 5} # Từ điển mẫu

# Nhập khóa cần xóa từ người dùng
khoa = input("Nhập khóa cần xóa: ") # Nhập khóa cần xóa

# Xóa phần tử và in kết quả
tu_dien = xoa_phan_tu(tu_dien, khoa) # Gọi hàm xóa phần tử khỏi từ điển
print("Từ điển sau khi xóa:", tu_dien) # In từ điển sau khi xóa
