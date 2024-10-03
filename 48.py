# VIẾT BẰNG PYTHON
# Tạo ma trận 3x3 và tính tích của các phần tử.

def main(): # Hàm main để chạy chương trình 
    ma_tran = []  # Khởi tạo ma trận rỗng   
    tich = 1  # Biến để lưu tích các phần tử

    # Nhập các phần tử của ma trận 3x3
    print("Nhập các phần tử của ma trận 3x3:")
    for i in range(3): # Duyệt qua các hàng của ma trận 
        hang = [] # Khởi tạo hàng rỗng
        for j in range(3): # Duyệt qua các cột của ma trận
            phan_tu = int(input(f"Phần tử [{i}][{j}]: ")) # Nhập phần tử từ bàn phím 
            hang.append(phan_tu) # Thêm phần tử vào hàng    
            tich *= phan_tu  # Tính tích của các phần tử
        ma_tran.append(hang) # Thêm hàng vào ma trận 

    # In tích của các phần tử
    print("Tích các phần tử trong ma trận là:", tich) 

if __name__ == "__main__": # Kiểm tra xem chương trình có được chạy trực tiếp hay không
    main()

# OUTPUT
# Nhập các phần tử của ma trận 3x3:
# Phần tử [0][0]: 1
# Phần tử [0][1]: 2
# Phần tử [0][2]: 3
# Phần tử [1][0]: 4
# Phần tử [1][1]: 5
# Phần tử [1][2]: 6
# Phần tử [2][0]: 7
# Phần tử [2][1]: 8
# Phần tử [2][2]: 9
# Tích các phần tử trong ma trận là: 362880
