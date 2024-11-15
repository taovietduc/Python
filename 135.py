# VIẾT BẰNG PYTHON
# Bài 135: Tính tổng các phần tử trên đường chéo phụ của ma trận.

def secondary_diagonal_sum(matrix): # Hàm tính tổng các phần tử trên đường chéo phụ của ma trận
    n = len(matrix) # Số hàng của ma trận (ma trận vuông)
    total = sum(matrix[i][n - i - 1] for i in range(n)) # Tính tổng các phần tử trên đường chéo phụ
    return total # Trả về tổng các phần tử trên đường chéo phụ

# Ví dụ sử dụng
matrix = [ # Ma trận vuông 3x3
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]
print("Tổng các phần tử trên đường chéo phụ là:", secondary_diagonal_sum(matrix)) 

# Kết quả: 15
# Giải thích: 3 + 5 + 7 = 15 
# Phần tử 3 nằm ở vị trí (0, 2)
# Phần tử 5 nằm ở vị trí (1, 1)
# Phần tử 7 nằm ở vị trí (2, 0)

