# Viết Bằng Python
# Bài 179: Viết hàm kiểm tra xem một ma trận có phải là ma trận đối xứng không.

def is_symmetric(matrix): # Hàm kiểm tra xem một ma trận có phải là ma trận đối xứng không
    n = len(matrix) # Số hàng của ma trận
    for i in range(n): # Duyệt từ hàng đầu đến hàng cuối của ma trận
        for j in range(n): # Duyệt từ cột đầu đến cột cuối của ma trận
            if matrix[i][j] != matrix[j][i]: # Nếu phần tử tại vị trí i, j khác phần tử tại vị trí j, i
                return False 
    return True # Trả về True nếu ma trận là ma trận đối xứng

matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(is_symmetric(matrix))  # Output: True
