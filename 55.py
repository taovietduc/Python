# VIẾT BẰNG PYTHON
# Bài 55: Tạo từ điển từ chuỗi.

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập chuỗi: ")

# Tách chuỗi thành danh sách các từ
tu_danh_sach = chuoi.split() # Mặc định tách theo khoảng trắng (space)

# Tạo từ điển từ danh sách các từ
tu_dien = {} # Khởi tạo từ điển rỗng

# Duyệt qua các từ trong danh sách
for tu in tu_danh_sach: # Lặp qua từng từ trong danh sách từ đọc được từ chuỗi
    if tu in tu_dien: # Kiểm tra từ đã tồn tại trong từ điển chưa (nếu có) thì tăng giá trị
        tu_dien[tu] += 1  # Nếu từ đã tồn tại trong từ điển, tăng giá trị
    else:   # Nếu từ chưa tồn tại trong từ điển thì thêm vào từ điển với giá trị 1
        tu_dien[tu] = 1  # Nếu từ chưa tồn tại, thêm vào từ điển với giá trị 1

# In từ điển
print("Từ điển được tạo từ chuỗi:")
print(tu_dien)
