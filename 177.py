# Viết Bằng Python
# Bài 177: Viết hàm xoay một ma trận vuông 90 độ theo chiều kim đồng hồ.

def rotate_matrix(matrix): # Hàm xoay ma trận 90 độ theo chiều kim đồng hồ
    n = len(matrix) # Số hàng của ma trận
    for i in range(n // 2): # Duyệt từ hàng đầu đến hàng giữa của ma trận
        for j in range(i, n - i - 1): # Duyệt từ cột đầu đến cột cuối
            temp = matrix[i][j] # Lưu giá trị của ma trận
            matrix[i][j] = matrix[n - j - 1][i] # Đổi giá trị của ma trận
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1] # Đổi giá trị của ma trận
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1] # Đổi giá trị của ma trận
            matrix[j][n - i - 1] = temp # Đổi giá trị của ma trận
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Ma trận cần xoay
rotated = rotate_matrix(matrix) # Xoay ma trận
for row in rotated: # Duyệt từng hàng của ma trận
    print(row)
# Output: [7, 4, 1], [8, 5, 2], [9, 6, 3]
