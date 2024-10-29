# VIẾT BẰNG PYTHON
# Bài 79: Tạo hàm tính tổng các số trong ma trận 3x3.
# Có 3 cách để giải bài toán này.
# Cách 1:
def sum_matrix(matrix): # hàm sum_matrix nhận vào 1 ma trận 3x3 và trả về tổng các phần tử trong ma trận đó
    sum = 0 # khởi tạo biến sum = 0 để lưu tổng các phần tử trong ma trận
    for row in matrix: # duyệt từng hàng trong ma trận matrix
        for element in row: # duyệt từng phần tử trong hàng đó
            sum += element # cộng phần tử đó vào biến sum
    return sum # trả về tổng các phần tử trong ma trận

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # khởi tạo ma trận 3x3 matrix  

print(sum_matrix(matrix)) # in ra tổng các phần tử trong ma trận matrix

# Cách 2:
def sum_matrix(matrix): # hàm sum_matrix nhận vào 1 ma trận 3x3 và trả về tổng các phần tử trong ma trận đó
    return sum([sum(row) for row in matrix]) 
# trả về tổng các phần tử trong ma trận bằng cách sử dụng list comprehension để duyệt từng hàng trong ma trận và tính tổng các phần tử trong hàng đó
 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # khởi tạo ma trận 3x3 matrix 

print(sum_matrix(matrix)) # in ra tổng các phần tử trong ma trận matrix

# Cách 3:
def sum_matrix(matrix): # hàm sum_matrix nhận vào 1 ma trận 3x3 và trả về tổng các phần tử trong ma trận đó
     return sum(sum(row) for row in matrix) 
# trả về tổng các phần tử trong ma trận bằng cách sử dụng list comprehension để duyệt từng hàng trong ma trận và tính tổng các phần tử trong hàng đó

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # khởi tạo ma trận 3x3 matrix

print(sum_matrix(matrix)) # in ra tổng các phần tử trong ma trận matrix

