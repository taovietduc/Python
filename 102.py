# VIẾT BẰNG PYTHON
# Bài 102: Tạo hàm tìm số lớn nhất thứ ba trong danh sách.

def tim_so_lon_thu_ba(danh_sach): # Hàm tìm số lớn thứ ba trong danh sách
    if len(danh_sach) < 3: # Nếu danh sách không đủ 3 phần tử
        return "Danh sách không đủ 3 phần tử" # Trả về thông báo lỗi
    
    # Loại bỏ các phần tử trùng lặp và sắp xếp theo thứ tự giảm dần 
    danh_sach_khong_trung = list(set(danh_sach)) # Loại bỏ các phần tử trùng lặp
    danh_sach_khong_trung.sort(reverse=True) # Sắp xếp theo thứ tự giảm dần
    
    return danh_sach_khong_trung[2]  # Trả về phần tử lớn thứ ba

# Ví dụ sử dụng
danh_sach = [4, 1, 5, 9, 3, 6, 5, 9, 7] # Danh sách các số
so_lon_thu_ba = tim_so_lon_thu_ba(danh_sach) # Gọi hàm tìm số lớn thứ ba
print("Số lớn thứ ba trong danh sách là:", so_lon_thu_ba) # In kết quả

# Kết quả
# Số lớn thứ ba trong danh sách là: 7
