# VIẾT BẰNG PYTHON
# Bài 89: Tạo hàm đảo ngược danh sách.

# Hàm đảo ngược danh sách
def dao_nguoc_danh_sach(danh_sach): # danh_sach là tham số truyền vào, kiểu dữ liệu danh sách
    return danh_sach[::-1]  # Sử dụng slicing để đảo ngược danh sách

# Nhập danh sách từ người dùng
danh_sach = list(map(int, input("Nhập các phần tử của danh sách (cách nhau bởi dấu cách): ").split())) 
# Chuyển chuỗi nhập vào thành danh sách số nguyên    

# Gọi hàm đảo ngược danh sách
danh_sach_dao_nguoc = dao_nguoc_danh_sach(danh_sach) # Gán kết quả trả về của hàm vào danh_sach_dao_nguoc

# In danh sách sau khi đảo ngược
print("Danh sách sau khi đảo ngược:", danh_sach_dao_nguoc) # In danh sách sau khi đảo ngược
