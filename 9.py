# VIẾT BẰNG PYTHON
# Tính diện tích hình tam giác

# Nhập chiều cao và đáy từ bàn phím
h = float(input("Nhập chiều cao của hình tam giác: "))
d = float(input("Nhập độ dài đáy của hình tam giác: "))

# Kiểm tra điều kiện chiều cao và đáy > 0
if h > 0 and d > 0:
    # Tính diện tích hình tam giác
    S = 0.5 * d * h
    # In kết quả
    print("Diện tích của hình tam giác là:", S)
else:
    print("Chiều cao và đáy phải lớn hơn 0.")
