# Viết bằng Python
# Bài 183: Kiểm tra ma trận có phải là ma trận tam giác trên hoặc tam giác dưới không.

def is_upper_triangle(matrix): # Kiểm tra ma trận có phải là ma trận tam giác trên không
    rows = len(matrix) # Số hàng của ma trận 
    for i in range(rows): # Duyệt qua từng hàng của ma trận
        for j in range(i): # Duyệt qua từng phần tử của hàng i
            if matrix[i][j] != 0:  # Nếu phần tử khác 0 thì không phải là ma trận tam giác trên
                return False 
    return True

def is_lower_triangle(matrix): # Kiểm tra ma trận có phải là ma trận tam giác dưới không
    rows = len(matrix) # Số hàng của ma trận
    for i in range(rows): # Duyệt qua từng hàng của ma trận
        for j in range(i+1, rows): # Duyệt qua từng phần tử của hàng i
            if matrix[i][j] != 0: # Nếu phần tử khác 0 thì không phải là ma trận tam giác dưới
                return False 
    return True


# Ví dụ
matrix1 = [ # Ma trận tam giác trên
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

matrix2 = [ # Ma trận tam giác dưới
    [1, 0, 0],
    [4, 5, 0],
    [6, 7, 8]
]

print("Ma trận là tam giác trên:", is_upper_triangle(matrix1)) 
print("Ma trận là tam giác dưới:", is_lower_triangle(matrix2))

# Kết quả
# Ma trận là tam giác trên: True
# Ma trận là tam giác dưới: True
# Như vậy, ma trận matrix1 là ma trận tam giác trên và matrix2 là ma trận tam giác dưới
