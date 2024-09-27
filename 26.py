# VIẾT BẰNG PYTHON
# In ra tam giác sao: Nhập số dòng và in ra tam giác sao.

# Nhập số dòng từ bàn phím
so_dong = int(input("Nhập số dòng: "))

# In tam giác sao
for i in range(1, so_dong + 1): # i chạy từ 1 đến so_dong
    print('*' * i)
