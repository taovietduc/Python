# VIẾT BẰNG PYTHON
# Câu 86: Tạo hàm tìm phần tử lớn thứ hai trong danh sách.

# Hàm tìm phần tử lớn thứ hai trong danh sách
def tim_phan_tu_lon_thu_hai(danh_sach): # Hàm nhận vào một danh sách số nguyên
    if len(danh_sach) < 2:
        return None  # Không có phần tử lớn thứ hai nếu danh sách có ít hơn 2 phần tử

    max1 = max2 = float('-inf')  # Khởi tạo max1 và max2 với giá trị rất nhỏ

    for num in danh_sach: # Duyệt qua từng phần tử trong danh sách
        if num > max1:
            max2 = max1  # Cập nhật max2 bằng giá trị cũ của max1
            max1 = num  # max1 được cập nhật với phần tử lớn nhất mới
        elif max1 > num > max2:
            max2 = num  # Cập nhật max2 khi phần tử nhỏ hơn max1 nhưng lớn hơn max2

    return max2 if max2 != float('-inf') else None # Trả về max2 nếu tìm thấy, ngược lại trả về None

# Nhập danh sách từ người dùng
danh_sach = list(map(int, input("Nhập các phần tử của danh sách (cách nhau bởi dấu cách): ").split()))

# Tìm phần tử lớn thứ hai
lon_thu_hai = tim_phan_tu_lon_thu_hai(danh_sach) # Gọi hàm tìm phần tử lớn thứ hai trong danh sách

# In kết quả
if lon_thu_hai is not None: # Nếu tìm thấy phần tử lớn thứ hai
    print("Phần tử lớn thứ hai trong danh sách là:", lon_thu_hai)
else: # Nếu không tìm thấy phần tử lớn thứ hai
    print("Không tìm được phần tử lớn thứ hai.")
