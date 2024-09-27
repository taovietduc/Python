# VIẾT BẰNG PYTHON
# In ra hình vuông sao: Nhập số dòng và số cột và in ra hình vuông sao.

# Nhập số dòng và số cột từ bàn phím
so_dong = int(input("Nhập số dòng: "))
so_cot = int(input("Nhập số cột: "))

# In hình vuông sao
for i in range(so_dong):
    print('*' * so_cot)


