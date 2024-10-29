# VIẾT BẰNG PYTHON
# Bài 63: Tạo hàm kiểm tra chuỗi đối xứng.

def kiem_tra_doi_xung(chuoi):
    # So sánh chuỗi với chuỗi đảo ngược của nó
    return chuoi == chuoi[::-1] # Trả về True nếu là đối xứng, ngược lại False

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi cần kiểm tra: ") # Nhập chuỗi từ bàn phím

if kiem_tra_doi_xung(chuoi): # Gọi hàm và kiểm tra chuỗi đối xứng
    print("Chuỗi là đối xứng.") # In kết quả nếu là đối xứng
else: # Ngược lại 
    print("Chuỗi không phải là đối xứng.") # In kết quả nếu không phải là đối xứng
