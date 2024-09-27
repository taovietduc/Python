# VIẾT BẰNG PYTHON
# Tìm chữ cái đầu tiên và cuối cùng của chuỗi: Nhập một chuỗi và tìm chữ cái đầu tiên và cuối cùng.

# Nhập chuỗi từ ban phím
s = input("Nhập một chuỗi: ")

# Tìm chữ cái đầu tiên và cuối cùng
if len(s) > 0: # Kiểm tra xem chuỗi có rỗng không
    chu_cai_dau = s[0] # Lấy chữ cái đầu tiên
    chu_cai_cuoi = s[-1] # Lấy chữ cái cuối cùng
    print(f"Chữ cái đầu tiên là: {chu_cai_dau}")
    print(f"Chữ cái cuối cùng là: {chu_cai_cuoi}")
else:
    print("Chuỗi rỗng, không có ký tự để hiển thị.")
