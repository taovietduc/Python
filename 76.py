# VIẾT BẰNG PYTHON
# Bài 76: Tạo hàm tạo danh sách các số nguyên tố từ danh sách.

def la_so_nguyen_to(n): # Hàm kiểm tra số nguyên tố
    if n <= 1: # 1 không phải số nguyên tố
        return False # Trả về False
    for i in range(2, int(n ** 0.5) + 1): # Duyệt từ 2 đến căn bậc 2 của n
        if n % i == 0: # Nếu n chia hết cho i
            return False # Trả về False vì n không phải số nguyên tố   
    return True # Trả về True nếu n là số nguyên tố

def loc_so_nguyen_to(danh_sach): # Hàm lọc số nguyên tố từ danh sách
    # Lọc các số nguyên tố từ danh sách
    return [x for x in danh_sach if la_so_nguyen_to(x)] 
    # Trả về danh sách các số nguyên tố

# Danh sách mẫu
danh_sach = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Danh sách mẫu có 11 phần tử

# Gọi hàm lọc số nguyên tố
danh_sach_nguyen_to = loc_so_nguyen_to(danh_sach) # Lọc số nguyên tố từ danh sách

# In kết quả
print("Danh sách các số nguyên tố là:", danh_sach_nguyen_to) # In danh sách các số nguyên tố
