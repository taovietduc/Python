# VIẾT BẰNG PYTHON
# Bài 90: Tạo hàm kiểm tra danh sách có phải là danh sách tăng dần không.

# Hàm kiểm tra danh sách có phải là danh sách tăng dần không
def kiem_tra_tang_dan(danh_sach): # danh_sach là một list chứa các phần tử kiểu số nguyên
    for i in range(len(danh_sach) - 1): # Duyệt qua từng cặp phần tử liên tiếp trong danh sách
        if danh_sach[i] > danh_sach[i + 1]: # Nếu phần tử trước lớn hơn phần tử sau
            return False  # Nếu có phần tử sau nhỏ hơn phần tử trước, danh sách không tăng dần
    return True  # Nếu tất cả cặp phần tử thỏa mãn, danh sách là tăng dần

# Nhập danh sách từ người dùng
danh_sach = list(map(int, input("Nhập các phần tử của danh sách (cách nhau bởi dấu cách): ").split()))

# Kiểm tra danh sách có phải là tăng dần không
if kiem_tra_tang_dan(danh_sach): # Nếu hàm trả về True thì danh sách là tăng dần
    print("Danh sách là tăng dần.") 
else: # Nếu hàm trả về False thì danh sách không tăng dần
    print("Danh sách không phải là tăng dần.")


