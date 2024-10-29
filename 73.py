# VIẾT BẰNG PYTHON
# Bài 73: Tạo hàm tính tổng các giá trị trong từ điển.

def tinh_tong_gia_tri(tu_dien): # Hàm tính tổng các giá trị trong từ điển
    tong = sum(tu_dien.values())  # Tính tổng các giá trị trong từ điển
    return tong # Trả về kết quả

# Tạo một từ điển mẫu
tu_dien = {'apple': 3, 'banana': 2, 'orange': 5} 
# Tạo một từ điển mẫu với các giá trị là số nguyên

# Tính tổng và in kết quả
tong = tinh_tong_gia_tri(tu_dien) # Gọi hàm và truyền vào từ điển
print("Tổng các giá trị trong từ điển là:", tong) # In kết quả
