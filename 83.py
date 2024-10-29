# VIẾT BẰNG PYTHON
# Bài 83: Tạo hàm sắp xếp danh sách số theo thứ tự giảm dần với danh sách tự nhập từ bàn phím.

def sap_xep_giam_dan(danh_sach): # Hàm sắp xếp giảm dần danh sách số nguyên danh_sach và trả về danh sách đã sắp xếp
    return sorted(danh_sach, reverse=True) # Sắp xếp giảm dần và trả về danh sách đã sắp xếp

# Nhập danh sách số từ bàn phím
n = int(input("Nhập số lượng phần tử: ")) # Nhập số lượng phần tử của danh sách
danh_sach = [] # Khởi tạo danh sách rỗng để lưu trữ các phần tử
for i in range(n): # Duyệt qua từng phần tử và thêm vào danh sách
    so = int(input(f"Nhập phần tử thứ {i + 1}: ")) # Nhập phần tử thứ i từ bàn phím
    danh_sach.append(so) # Thêm phần tử vào danh sách số nguyên

# Sắp xếp giảm dần
danh_sach_sap_xep = sap_xep_giam_dan(danh_sach) # Sắp xếp danh sách giảm dần và lưu vào danh sách_sap_xep

# In danh sách sau khi sắp xếp
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_sap_xep) # In danh sách sau khi sắp xếp giảm dần
