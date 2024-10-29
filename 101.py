# VIẾT BẰNG PYTHON
# Câu 101: Tạo hàm tính tổng của một danh sách các số thực.

def tinh_tong_danh_sach_thuc(danh_sach): # danh_sach là một danh sách các số thực
    tong = sum(danh_sach) # Hàm sum() trả về tổng của các phần tử trong danh sách
    return tong # Trả về tổng của danh sách

# Ví dụ sử dụng
danh_sach = [1.5, 2.3, 4.7, 5.2] # Danh sách các số thực
tong = tinh_tong_danh_sach_thuc(danh_sach) # Gọi hàm và truyền danh sách vào
print("Tổng của danh sách là:", tong) # In kết quả
