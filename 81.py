# VIẾT BẰNG PYTHON
# Bài 81: Tạo hàm tìm bội chung nhỏ nhất của hai số.

def ucln(a, b): # Tìm ước chung lớn nhất của 2 số a và b
    while b != 0: # Nếu b khác 0
        a, b = b, a % b # a = b, b = a % b
    return a # Trả về a

def bcnn(a, b): # Tìm bội chung nhỏ nhất của 2 số a và b
    return abs(a * b) // ucln(a, b) # Trả về bội chung nhỏ nhất của 2 số a và b

# Kiểm tra
a = int(input("Nhập số thứ nhất: ")) # Nhập số thứ nhất
b = int(input("Nhập số thứ hai: ")) # Nhập số thứ hai 
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn(a, b)}") 
# In ra bội chung nhỏ nhất của 2 số a và b
