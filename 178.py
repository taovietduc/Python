# Viết Bằng Python
# Bài 178: Tạo hàm tìm ma trận con có tổng lớn nhất từ một ma trận 2D cho trước.

def max_sum_submatrix(matrix): # tìm ma trận con có tổng lớn nhất
    def kadane(arr): # tìm dãy con liên tục có tổng lớn nhất trong mảng arr
        max_sum, current_sum = float('-inf'), 0 
        for num in arr: # duyệt qua từng phần tử trong mảng arr để tìm dãy con liên tục có tổng lớn nhất    
            current_sum = max(num, current_sum + num)  # cập nhật tổng dãy con liên tục có tổng lớn nhất
            max_sum = max(max_sum, current_sum) # cập nhật tổng lớn nhất
        return max_sum  # trả về tổng lớn nhất  của dãy con liên tục trong mảng arr

    rows, cols = len(matrix), len(matrix[0])   # số hàng và số cột của ma trận
    max_sum = float('-inf') # khởi tạo tổng lớn nhất

    for left in range(cols):    # duyệt qua từng cột
        temp = [0] * rows
        for right in range(left, cols): # duyệt qua từng cột từ cột left đến cột cuối cùng
            for i in range(rows):   # duyệt qua từng hàng
                temp[i] += matrix[i][right] # cộng các phần tử của cột từ cột left đến cột right
            max_sum = max(max_sum, kadane(temp))    # cập nhật tổng lớn nhất của dãy con liên tục trong mảng temp
    return max_sum

matrix = [[1, 2, -1, -4, -20],  # ma trận 2 chiều 5x5
          [-8, -3, 4, 2, 1],
          [3, 8, 10, 1, 3],
          [-4, -1, 1, 7, -6]]
print(max_sum_submatrix(matrix))  # Output: 29
