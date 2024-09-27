# VIẾT BẰNG PYTHON
# Tạo chuỗi từ danh sách: Nhập danh sách các từ và tạo chuỗi từ danh sách đó.

# Nhập danh sách các từ từ bàn phím
danh_sach = input("Nhập danh sách các từ (cách nhau bởi dấu cách): ").split() 

# .split() để tách các từ cách nhau bởi dấu cách

# Tạo chuỗi từ danh sách
s = ' '.join(danh_sach) # .join() để nối các từ trong danh sách lại với nhau, cách nhau bởi dấu cách

# In chuỗi đã tạo
print(f"Chuỗi được tạo là: {s}")
