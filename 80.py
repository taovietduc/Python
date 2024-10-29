# VIẾT BẰNG PYTHON
# Bài 80: Tạo hàm kiểm tra một số có phải là số Armstrong không.

def kiem_tra_so_armstrong(n): # Hàm kiểm tra số Armstrong 
    # Chuyển số thành chuỗi để dễ dàng tính toán
    chuoi_n = str(n) # Chuyển số thành chuỗi để dễ dàng tính toán
    so_chu_so = len(chuoi_n) # Đếm số chữ số của số đó để lấy lũy thừa
    
    tong = 0 # Khởi tạo biến tổng để lưu tổng lũy thừa từng chữ số
    for chu_so in chuoi_n: # Duyệt từng chữ số trong chuỗi số
        tong += int(chu_so) ** so_chu_so  # Tính lũy thừa từng chữ số
    
    # Kiểm tra nếu tổng bằng chính số đó
    return tong == n 

# Kiểm tra
n = int(input("Nhập số cần kiểm tra: ")) # Nhập số cần kiểm tra từ bàn phím
if kiem_tra_so_armstrong(n): # Gọi hàm kiểm tra số Armstrong
    print(f"{n} là số Armstrong.") # In kết quả
else: # Ngược lại không phải số Armstrong
    print(f"{n} không phải là số Armstrong.") # In kết quả
