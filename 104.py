# VIẾT BẰNG PYTHON
# Bài 104: Tạo hàm tính trung bình của các số nguyên tố trong danh sách.

def la_so_nguyen_to(n): # Hàm kiểm tra số nguyên tố 
    if n < 2: # Nếu số nhỏ hơn 2 thì không phải số nguyên tố
        return False # Trả về False nếu không phải số nguyên tố
    for i in range(2, int(n**0.5) + 1): # Duyệt từ 2 đến căn bậc 2 của n
        if n % i == 0: # Nếu n chia hết cho i thì không phải số nguyên tố
            return False # Trả về False nếu không phải số nguyên tố
    return True # Trả về True nếu là số nguyên tố

def tinh_trung_binh_so_nguyen_to(danh_sach): # Hàm tính trung bình số nguyên tố
    tong = 0 # Khởi tạo biến tổng số nguyên tố
    dem = 0 # Khởi tạo biến đếm số nguyên tố
    for so in danh_sach: # Duyệt từng số trong danh sách
        if la_so_nguyen_to(so): # Nếu số đó là số nguyên tố
            tong += so # Cộng số đó vào tổng
            dem += 1 # Tăng biến đếm lên 1
    if dem == 0: # Nếu không có số nguyên tố
        return 0  # Trả về 0 nếu không có số nguyên tố
    return tong / dem # Trả về trung bình số nguyên tố

# Ví dụ sử dụng
danh_sach = [2, 3, 4, 5, 6, 7, 8, 9, 10] # Danh sách số cần tính trung bình số nguyên tố
trung_binh = tinh_trung_binh_so_nguyen_to(danh_sach) # Gọi hàm tính trung bình số nguyên tố
print(f"Trung bình của các số nguyên tố trong danh sách: {trung_binh}") # In kết quả
