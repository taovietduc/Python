# VIẾT BẰNG PYTHON
# In bảng cửu chương cho một số.

# Nhập một số từ người dùng
so = int(input("Nhập một số: "))

# In bảng cửu chương của số đó
print(f"Bảng cửu chương của {so}:") # f-string (formatted string) giúp chúng ta kết hợp biến vào chuỗi một cách dễ dàng
for i in range(1, 11): # range(1, 11) tạo ra một dãy số từ 1 đến 10 (không bao gồm 11)
    print(f"{so} x {i} = {so * i}") # in ra phép nhân của số với i

