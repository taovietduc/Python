# Viết bằng Python
# Bài 184: Tính tổng các phần tử nằm ở vị trí lẻ (theo chỉ số hàng và cột)
 
def sum_odd_positions(matrix): # Hàm tính tổng các phần tử ở vị trí lẻ
    total_sum = 0 # Khởi tạo biến tổng bằng 0 
    for i in range(len(matrix)): # Duyệt qua từng hàng của ma trận 
        for j in range(len(matrix[0])): # Duyệt qua từng cột của ma trận 
            if (i + j) % 2 != 0: # Nếu tổng chỉ số hàng và chỉ số cột là số lẻ
                total_sum += matrix[i][j] # Cộng giá trị phần tử vào tổng
    return total_sum  # Trả về tổng các phần tử ở vị trí lẻ


# Ví dụ
matrix = [ # Ma trận 3x3
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Tổng các phần tử ở vị trí lẻ:", sum_odd_positions(matrix))

# Kết quả
# Tổng các phần tử ở vị trí lẻ: 20
# Giải thích: Các phần tử ở vị trí lẻ là 2, 4, 6, 8
# Tổng các phần tử ở vị trí lẻ là 2 + 4 + 6 + 8 = 20
# Như vậy kết quả là 20
