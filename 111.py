# VIẾT BẰNG PYTHON
# Bài 111: Tạo hàm tính tổng các phần tử trên đường chéo chính của ma trận.

def diagonal_sum(matrix): # Định nghĩa hàm diagonal_sum với tham số truyền vào là matrix
    """
    Tính tổng các phần tử trên đường chéo chính của ma trận.

    Parameters:
    matrix (list of list): Ma trận dưới dạng danh sách các danh sách.

    Returns:
    int: Tổng các phần tử trên đường chéo chính.
    """
    n = len(matrix)  # Kích thước của ma trận (giả sử là ma trận vuông)
    total = 0 # Khởi tạo biến tổng bằng 0
    for i in range(n): # Duyệt qua các dòng của ma trận
        total += matrix[i][i]  # Phần tử nằm trên đường chéo chính
    return total # Trả về tổng các phần tử trên đường chéo chính

# Ví dụ sử dụng
matrix =  [ # Ma trận vuông 3x3 (3 hàng, 3 cột)
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Tổng các phần tử trên đường chéo chính là: {diagonal_sum(matrix)}")

# Giải thích:
# Tham số matrix: Nhận vào một ma trận dưới dạng danh sách các danh sách (giả sử là ma trận vuông).
# Duyệt qua đường chéo chính: Phần tử trên đường chéo chính là các phần tử có chỉ số hàng và chỉ số cột giống nhau (tức là matrix[i][i]).
# Kết quả: Trả về tổng các phần tử trên đường chéo chính.