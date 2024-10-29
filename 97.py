# VIẾT BẰNG PYTHON
# Bài 97: Tạo hàm tính tổng các số lẻ trong một khoảng cho trước.

# Hàm tính tổng các số lẻ trong một khoảng
def tong_so_le(start, end): # start: khoảng bắt đầu, end: khoảng kết thúc
    tong = 0 # Khởi tạo biến tổng
    for i in range(start, end + 1): # Duyệt từ start đến end
        if i % 2 != 0:  # Kiểm tra nếu là số lẻ
            tong += i # Cộng số lẻ vào tổng
    return tong # Trả về tổng

# Nhập khoảng bắt đầu và kết thúc
start = int(input("Nhập khoảng bắt đầu: ")) # Nhập số bắt đầu của khoảng
end = int(input("Nhập khoảng kết thúc: ")) # Nhập số kết thúc của khoảng

tong = tong_so_le(start, end) # Gọi hàm tính tổng số lẻ trong khoảng
print(f"Tổng các số lẻ trong khoảng từ {start} đến {end} là: {tong}") 
# In kết quả tổng số lẻ trong khoảng

# Kết quả
# Nhập khoảng bắt đầu: 5
# Nhập khoảng kết thúc: 12
# Tổng các số lẻ trong khoảng từ 5 đến 12 là: 32 ( 5 + 7 + 9 + 11 = 32 )