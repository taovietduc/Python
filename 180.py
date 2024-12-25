# Viết Bằng Python
# Bài 180: Tìm tất cả các đường đi từ góc trên trái đến góc dưới phải của một ma trận.

def all_paths(matrix, i, j, path, paths): # Tìm tất cả các đường đi từ góc trên trái đến góc dưới phải của một ma trận
    rows, cols = len(matrix), len(matrix[0])    # số hàng và số cột của ma trận
    if i == rows - 1 and j == cols - 1:
        paths.append(path + [matrix[i][j]]) # thêm đường đi vào paths
        return

    if i < rows - 1: # tìm đường đi từ hàng dưới 
        all_paths(matrix, i + 1, j, path + [matrix[i][j]], paths) # tìm đường đi từ hàng dưới
    if j < cols - 1: # tìm đường đi từ cột phải  
        all_paths(matrix, i, j + 1, path + [matrix[i][j]], paths) # tìm đường đi từ cột phải

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # ma trận 2 chiều 3x3 
paths = [] # khởi tạo mảng paths
all_paths(matrix, 0, 0, [], paths) # tìm tất cả các đường đi từ góc trên trái đến góc dưới phải của ma trận
print(paths)
# Output: [[1, 4, 7, 8, 9], [1, 4, 5, 8, 9], [1, 2, 5, 8, 9], [1, 2, 3, 6, 9]]
