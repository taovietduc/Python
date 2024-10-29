# VIẾT BẰNG PYTHON
# Bài 56: Kiểm tra số hoàn hảo.

# Hàm kiểm tra số hoàn hảo
def kiem_tra_so_hoan_hao(n): # n là số cần kiểm tra có phải số hoàn hảo không 
    tong_uoc = 0
    for i in range(1, n): # Duyệt các số từ 1 đến n-1 để kiểm tra ước của n 
        if n % i == 0:  # Kiểm tra nếu i là ước của n
            tong_uoc += i # Cộng i vào tổng các ướ của n 
    return tong_uoc == n  # Kiểm tra tổng các ước có bằng n không

# Nhập số từ bàn phím
so = int(input("Nhập một số: ")) # Nhập số cần kiểm tra từ bàn phím

# Kiểm tra và in kết quả
if kiem_tra_so_hoan_hao(so): # Gọi hàm kiểm tra số hoàn hảo
    print(f"{so} là số hoàn hảo.") # In kết quả nếu là số hoàn hảo
else: # Nếu không phải số hoàn hảo
    print(f"{so} không phải là số hoàn hảo.") # In kết quả nếu không phải số hoàn hảo

