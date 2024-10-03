# VIẾT BẰNG PYTHON
# Tính tổng các số chẵn trong danh sách.

# Tính tổng các số chẵn trong danh sách
def main(): # Hàm main để chạy chương trình
    # Nhập số lượng phần tử
    n = int(input("Nhập số lượng phần tử trong danh sách: ")) 

    # Nhập danh sách các phần tử
    danh_sach = [] # Khởi tạo danh sách rỗng 
    for i in range(n): # Duyệt qua các phần tử của danh sách
        phan_tu = int(input(f"Phần tử {i+1}: ")) # Nhập phần tử từ bàn phím
        danh_sach.append(phan_tu) # Thêm phần tử vào danh sách

    # Tính tổng các số chẵn
    tong = sum([x for x in danh_sach if x % 2 == 0]) # Tính tổng các số chẵn trong danh sách

    # In tổng các số chẵn
    print("Tổng các số chẵn trong danh sách là:", tong) # In tổng các số chẵn

if __name__ == "__main__": # Kiểm tra xem có phải chạy chính chương trình không
    main()
