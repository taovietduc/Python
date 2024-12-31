# Viết Bằng Python
# Bài 181: Viết hàm tìm tổng các phần tử trên biên của ma trận.

def sum_boundary(matrix): # Hàm tìm tổng các phần tử trên biên của ma trận
    if not matrix: # Nếu ma trận rỗng thì trả về 0
        return 0 

    rows = len(matrix) # Số hàng của ma trận 
    cols = len(matrix[0]) # Số cột của ma trận 
    total_sum = 0 # Khởi tạo biến tổng

    # Tổng các phần tử hàng đầu và hàng cuối
    for j in range(cols): # Duyệt qua các cột của ma trận
        total_sum += matrix[0][j] + matrix[rows - 1][j] # Cộng các phần tử ở hàng đầu và hàng cuối

    # Tổng các phần tử ở cột đầu và cột cuối (trừ các góc đã cộng trước đó)
    for i in range(1, rows - 1): # Duyệt qua các hàng từ hàng thứ 2 đến hàng trước hàng cuối
        total_sum += matrix[i][0] + matrix[i][cols - 1] # Cộng các phần tử ở cột đầu và cột cuối

    return total_sum # Trả về tổng các phần tử trên biên của ma trận


# Ví dụ
matrix = [ # Ma trận 3x3
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Tổng các phần tử trên biên:", sum_boundary(matrix)) # In ra tổng các phần tử trên biên của ma trận

# Kết quả
# Tổng các phần tử trên biên: 25
# Tổng các phần tử trên biên của ma trận 3x3 là 1 + 2 + 3 + 4 + 6 + 7 + 8 + 9 = 25
# Các phần tử trên biên của ma trận 3x3 là: 1, 2, 3, 4, 6, 7, 8, 9
# Các phần tử ở giữa ma trận là: 5
# Tổng các phần tử trên biên của ma trận 3x3 là 25

