# Viết Bằng Python
# Bài 182: Tạo hàm tính tổng các số lẻ trên đường chéo chính của ma trận.

def sum_odd_diagonal(matrix): # Hàm tìm tổng các số lẻ trên đường chéo chính của ma trận
    if not matrix:    # Nếu ma trận rỗng thì trả về 0
        return 0

    rows = len(matrix)  # Số hàng của ma trận
    total_sum = 0    # Khởi tạo biến tổng

    for i in range(rows): # Duyệt qua các hàng của ma trận
        if matrix[i][i] % 2 != 0:  # Kiểm tra số lẻ
            total_sum += matrix[i][i]

    return total_sum # Trả về tổng các số lẻ trên đường chéo chính của ma trận


# Ví dụ
matrix = [ # Ma trận 3x3 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Tổng các số lẻ trên đường chéo chính:", sum_odd_diagonal(matrix))

# Kết quả
# Tổng các số lẻ trên đường chéo chính: 15
# Các số lẻ trên đường chéo chính của ma trận 3x3 là: 1, 5, 9
# Tổng các số lẻ trên đường chéo chính của ma trận 3x3 là 15
# Các số chẵn trên đường chéo chính của ma trận 3x3 là: 2, 6
# Các số chẵn trên đường chéo chính của ma trận 3x3 là 8
