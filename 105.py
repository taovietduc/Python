# VIẾT BẰNG PYTHON
# Bài 105: Tạo hàm tính chu vi của một hình chữ nhật.

def tinh_chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong): 
# Hàm tính chu vi hình chữ nhật với 2 tham số chiều dài và chiều rộng của hình chữ nhật
    chu_vi = 2 * (chieu_dai + chieu_rong) # Công thức tính chu vi hình chữ nhật
    return chu_vi # Trả về giá trị chu vi của hình chữ nhật

# Ví dụ sử dụng
chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: ")) # Nhập chiều dài hình chữ nhật
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: ")) # Nhập chiều rộng hình chữ nhật
chu_vi = tinh_chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong) # Gọi hàm tính chu vi hình chữ nhật
print(f"Chu vi của hình chữ nhật là: {chu_vi}") # In kết quả chu vi hình chữ nhật

