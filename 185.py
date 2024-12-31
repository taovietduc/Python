# Viết bằng Python
# Bài 185: Chuyển đổi ma trận thành danh sách xoắn ốc.

def spiral_matrix(matrix): # Hàm chuyển đổi ma trận thành danh
    result = [] # Khởi tạo danh sách kết quả 
    while matrix: # Vòng lặp chạy cho đến khi ma trận rỗng
        result += matrix.pop(0) # Thêm hàng đầu tiên vào danh sách kết quả
        if matrix and matrix[0]: # Kiểm tra ma trận còn phần tử không
            for row in matrix: # Duyệt qua các hàng còn lại
                result.append(row.pop())
        if matrix: # Kiểm tra ma trận còn phần tử không
            result += matrix.pop()[::-1]
        if matrix and matrix[0]: # Kiểm tra ma trận còn phần tử không
            for row in matrix[::-1]: # Duyệt qua các hàng còn lại
                result.append(row.pop(0))
    return result


# Ví dụ
matrix = [ # Ma trận cần chuyển đổi
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Danh sách xoắn ốc:", spiral_matrix(matrix))

# Kết quả
# Danh sách xoắn ốc: [1, 2, 3, 6, 9, 8, 7, 4, 5]
# Giải thích: Chuyển ma trận thành danh sách xoắn ốc ta được danh sách trên
# 1 2 3
# 4 5 6
# 7 8 9
# Duyệt theo chiều kim đồng hồ ta được danh sách trên
# 1 2 3 6 9 8 7 4 5
# Danh sách này chính là danh sách xoắn ốc của ma trận ban đầu