# VIẾT BẰNG PYTHON 
# Tạo từ điển từ danh sách: Nhập một danh sách các từ và tạo từ điển từ danh sách đó.

# Nhập danh sách các từ từ người dùng
danh_sach = input("Nhập các từ cách nhau bởi dấu cách: ").split() 
# split() để tách các từ cách nhau bởi dấu cách

# Tạo từ điển đếm số lần xuất hiện của từng từ
tu_dien = {} # Khởi tạo từ điển rỗng

for tu in danh_sach: # Duyệt qua từng từ trong danh sách
    if tu in tu_dien: # Nếu từ đã có trong từ điển thì tăng số lần xuất hiện lên 1
        tu_dien[tu] += 1 # Tăng số lần xuất hiện lên 1
    else:
        tu_dien[tu] = 1 # Nếu từ chưa có trong từ điển thì thêm vào với số lần xuất hiện là 1 

# In từ điển
print("Từ điển từ danh sách là:")
print(tu_dien)
