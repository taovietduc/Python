# VIẾT BẰNG PYTHON
# Bài 107: Tạo hàm kiểm tra một số có phải là số hoàn hảo không.

def kiem_tra_so_hoan_hao(n): # Hàm kiểm tra số hoàn hảo     
    if n <= 1: # Nếu số nhỏ hơn hoặc bằng 1 thì không phải số hoàn hảo
        return False 
    
    tong_uoc = 0 # Khởi tạo biến tổng ước bằng 0
    for i in range(1, n): # Duyệt từ 1 đến n - 1
        if n % i == 0: # Nếu n chia hết cho i thì i là ước của n
            tong_uoc += i # Cộng i vào tổng ước

    return tong_uoc == n # Trả về True nếu tổng ước bằng n, ngược lại trả về False

# Ví dụ sử dụng
so = int(input("Nhập số cần kiểm tra: ")) # Nhập số cần kiểm tra
if kiem_tra_so_hoan_hao(so): # Kiểm tra số hoàn hảo
    print(f"{so} là số hoàn hảo.") # In kết quả
else:   # Ngược lại không phải số hoàn hảo
    print(f"{so} không phải là số hoàn hảo.") # In kết quả

# Kết quả
# Nhập số cần kiểm tra: 28
# 28 là số hoàn hảo.

