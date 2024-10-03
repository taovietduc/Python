# VIẾT BẰNG PYTHON
# Tạo danh sách các số chẵn từ danh sách: Nhập một danh sách các số và tạo danh sách các số chẵn.

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: ")) # Nhập số lượng phần tử trong danh sách

# Tạo danh sách để lưu các phần tử
danh_sach = []

# Nhập các phần tử vào danh sách
print("Nhập các phần tử: ") # Nhập các phần tử
for i in range(n): # Vòng lặp for để nhập các phần tử vào danh sách
    phan_tu = int(input()) # Nhập phần tử từ bàn phím
    danh_sach.append(phan_tu) # Thêm phần tử vào danh sách

# Tạo danh sách các số chẵn
danh_sach_chan = [phan_tu for phan_tu in danh_sach if phan_tu % 2 == 0] 
# Tạo danh sách các số chẵn từ danh sách đã nhập vào trước đó 

# In danh sách các số chẵn
print("Danh sách các số chẵn là: ", danh_sach_chan)
