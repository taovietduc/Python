# VIẾT BẰNG PYTHON
# Bài 60: Tạo hàm kiểm tra số nguyên tố.

# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):

    if n <= 1: # Nếu n là số nguyên tố thì trả về False
        return False # Vì số nguyên tố phải lớn hơn 1
    for i in range(2, int(n**0.5) + 1): # Duyệt từ 2 đến căn bậc 2 của n 
        if n % i == 0: # Nếu n chia hết cho i thì n không phải là số nguyên tố
            return False # Trả về False
    return True # Nếu không chia hết cho i nào thì n là số nguyên tố

# Nhập số từ bàn phím
num = int(input("Nhập một số: ")) # Ép kiểu dữ liệu về int để có thể nhận số nguyên

if kiem_tra_so_nguyen_to(num): # Gọi hàm và kiểm tra số nguyên tố 
    print(f"{num} là số nguyên tố.") # In kết quả nếu là số nguyên tố
else:
    print(f"{num} không phải là số nguyên tố.") 
# In kết quả nếu không phải là số nguyên tố
