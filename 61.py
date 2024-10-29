# VIẾT BẰNG PYTHON
# Bài 61: Tạo hàm tính giai thừa của số n.

# Hàm tính giai thừa của số n.
def tinh_giai_thua(n): # Hàm có tham số truyền vào là n
    if n == 0 or n == 1: # Nếu n = 0 hoặc n = 1 thì trả về 1
        return 1 # Vì 0! = 1! = 1   
    else: # Ngược lại
        return n * tinh_giai_thua(n - 1) # Trả về n * (n - 1)!

# Nhập số từ bàn phím
num = int(input("Nhập một số: ")) # Ép kiểu dữ liệu về int để có thể nhận số nguyên

# Gọi hàm và in kết quả
print(f"Giai thừa của {num} là {tinh_giai_thua(num)}") # In kết quả giai thừa của số n

# Kết quả
# Nhập một số: 4
# Giai thừa của 4 là 24