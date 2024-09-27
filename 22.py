# VIẾT BẰNG PYTHON
# In các ký tự riêng biệt của chuỗi: Nhập một chuỗi và in các ký tự riêng biệt.

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập một chuỗi: ")

# Tạo một tập hợp để lưu các ký tự riêng biệt
ky_tu_rieng_biet = set(chuoi) # set() sẽ loại bỏ các phần tử trùng lặp

# In các ký tự riêng biệt
print("Các ký tự riêng biệt trong chuỗi là:")
for ky_tu in ky_tu_rieng_biet: # Duyệt qua từng ký tự trong tập hợp
    print(ky_tu)
