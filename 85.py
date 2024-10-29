# VIẾT BẰNG PYTHON
# Bài 85: Tạo hàm kiểm tra danh sách có chứa số âm không.

def kiem_tra_so_am(danh_sach): # Hàm kiểm tra số âm
    for so in danh_sach: # Duyệt từng phần tử trong danh sách
        if so < 0:  # Nếu phát hiện số âm
            return True
    return False # Nếu không có số âm

# Nhập danh sách từ ban phím
danh_sach = list(map(int, input("Nhập danh sách các số, cách nhau bởi dấu cách: ").split())) 
#.split() tách chuỗi thành list dựa vào dấu cách và map chuyển từng phần tử thành kiểu int

# Kiểm tra và in kết quả
if kiem_tra_so_am(danh_sach): # Nếu hàm trả về True thì in ra danh sách có chứa số âm
    print("Danh sách có chứa số âm.")
else: # Nếu hàm trả về False thì in ra danh sách không chứa số âm
    print("Danh sách không chứa số âm.")
