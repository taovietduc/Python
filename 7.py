# VIẾT BẰNG PYTHON
# Tính diện tích hình chữ nhật: Nhập chiều dài và chiều rộng và in ra chu vi, diện tích của hình chữ nhật.

# Nhập chiều dài và chiều rộng từ bàn phím
a = float(input("Nhập chiều dài a: "))
b = float(input("Nhập chiều rộng b: "))

# Kiểm tra điều kiện chiều dài và chiều rộng phải lớn hơn 0
if a > 0 and b > 0:
    # Tính chu vi hình chữ nhật
    C = (a + b) * 2
    # Tính diện tích hình chữ nhật
    S = a * b
    # In kết quả
    print("Chu vi của hình chữ nhật là:", C)
    print("Diện tích của hình chữ nhật là:", S)
else:
    print("Chiều dài và chiều rộng phải lớn hơn 0.")