# VIẾT BẰNG PYTHON
# Kiểm tra chuỗi đối xứng: Nhập một chuỗi và kiểm tra xem nó có phải là chuỗi đối xứng không.

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập một chuỗi: ")

# Kiểm tra chuỗi đối xứng

if chuoi == chuoi[::-1]: # [::-1] sẽ đảo ngược chuỗi
    print("Chuỗi này là chuỗi đối xứng.")
else:
    print("Chuỗi này không phải là chuỗi đối xứng.")
