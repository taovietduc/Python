# VIẾT BẰNG PYTHON
# Tính giai thừa của một số: Nhập một số và tính giai thừa của nó.

# Nhập số từ bàn phím  
n = int(input("Nhập một số: "))

# Tính giai thừa
giai_thua = 1

if n < 0:
    print("Không có giai thừa của số âm.")
elif n == 0:
    print("Giai thừa của 0 là 1.")
else:
    for i in range(1, n + 1):
        giai_thua *= i
    print(f"Giai thừa của {n} là {giai_thua}.")

    