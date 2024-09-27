# VIẾT BẰNG PYTHON
# Tính trung bình của danh sách: Nhập một danh sách các số và tính trung bình của chúng.

# Nhập danh sách các số từ bàn phím
danh_sach = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split())) 
# map() chuyển các phần tử trong danh sách thành số nguyên

# Tính tổng của danh sách
tong = sum(danh_sach) # sum() trả về tổng của các phần tử trong danh sách

# Tính trung bình
trung_binh = tong / len(danh_sach) # len() trả về số phần tử trong danh sách

# In kết quả
print("Trung bình của danh sách là:", trung_binh)
