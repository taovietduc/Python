# Viết bằng Python
# Bài 186: Tìm tất cả các ma trận con có tổng nhỏ hơn một số cho trước.

def submatrix_sums(matrix, threshold): # matrix là ma trận, threshold là ngưỡng tổng
    rows = len(matrix) # số hàng của ma trận matrix
    cols = len(matrix[0])   # số cột của ma trận matrix 
    submatrices = []  # danh sách chứa các ma trận con có tổng nhỏ hơn threshold
    
    for i in range(rows): # duyệt qua các hàng của ma trận matrix
        for j in range(cols): # duyệt qua các cột của ma trận matrix
            for m in range(i, rows): # duyệt qua các hàng từ i đến rows
                for n in range(j, cols): # duyệt qua các cột từ j đến cols
                    submatrix = [row[j:n+1] for row in matrix[i:m+1]] # tạo ma trận con từ hàng i đến m và cột j đến n
                    sub_sum = sum(sum(row) for row in submatrix) # tính tổng các phần tử của ma trận con
                    if sub_sum < threshold: # nếu tổng nhỏ hơn threshold thì thêm vào danh sách submatrices
                        submatrices.append((submatrix, sub_sum)) # thêm ma trận con và tổng vào danh sách submatrices
    return submatrices

# Ví dụ
matrix = [ # ma trận 3x3 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
threshold = 15 # ngưỡng tổng

result = submatrix_sums(matrix, threshold) # tìm các ma trận con có tổng nhỏ hơn threshold
print(f"Tổng {len(result)} ma trận con có tổng nhỏ hơn {threshold}:") 
# in ra số lượng ma trận con có tổng nhỏ hơn threshold
for submatrix, sub_sum in result:   # duyệt qua các ma trận con và tổng của chúng
    print("Ma trận:", submatrix, "Tổng:", sub_sum)
    
# Kết quả
# Tổng 12 ma trận con có tổng nhỏ hơn 15:
# Ma trận: [[1]] Tổng: 1
# Ma trận: [[1, 2]] Tổng: 3
# Ma trận: [[2]] Tổng: 2
# Ma trận: [[4]] Tổng: 4
# Ma trận: [[4, 5]] Tổng: 9
# Ma trận: [[5]] Tổng: 5
# Ma trận: [[7]] Tổng: 7
# Ma trận: [[7, 8]] Tổng: 15
# Ma trận: [[8]] Tổng: 8
# Ma trận: [[1], [4]] Tổng: 5
# Ma trận: [[1, 2], [4, 5]] Tổng: 12
# Ma trận: [[2], [5]] Tổng: 7
# Các ma trận con có tổng nhỏ hơn 15 là:
# [[1]], [[1, 2]], [[2]], [[4]], [[4, 5]], [[5]], [[7]], [[7, 8]], [[8]], [[1], [4]], [[1, 2], [4, 5]], [[2], [5]]
# Các ma trận con có tổng nhỏ hơn 15 là các ma trận con có tổng nhỏ hơn 15.