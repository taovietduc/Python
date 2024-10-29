# VIẾT BẰNG PYTHON
# Tạo hàm tính diện tích hình vuông.

# Hàm tính diện tích hình vuông
def tinh_dien_tich_hinh_vuong(canh): # canh: độ dài cạnh của hình vuông 
    return canh * canh

# Nhập độ dài cạnh từ người dùng
canh = float(input("Nhập độ dài cạnh của hình vuông: ")) # canh: độ dài cạnh của hình vuông 

# Tính và in kết quả
dien_tich = tinh_dien_tich_hinh_vuong(canh) # dien_tich: diện tích của hình vuông
print(f"Diện tích của hình vuông là: {dien_tich}") # In kết quả
