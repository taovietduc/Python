# Viết bằng Python
# Bài 191: Viết thuật toán sinh số Fibonacci với độ phức tạp O(log n).

def multiply_matrix(a, b): # nhân hai ma trận 2x2 a và b với nhau 
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

def power_matrix(matrix, n): # tính lũy thừa ma trận 2x2 matrix^n   
    result = [[1, 0], [0, 1]]  # ma trận đơn vị 2x2 
    base = matrix # ma trận cơ sở 
    while n: # nếu n khác 0 
        if n % 2: # nếu n chia hết cho 2
            result = multiply_matrix(result, base) # nhân ma trận kết quả với ma trận cơ sở
        base = multiply_matrix(base, base) # nhân ma trận cơ sở với chính nó
        n //= 2 # chia n cho 2
    return result

def fibonacci(n): # hàm trả về số Fibonacci thứ n   
    if n <= 1: # nếu n <= 1 
        return n
    matrix = [[1, 1], [1, 0]] # ma trận Fibonacci
    result = power_matrix(matrix, n - 1) # lũy thừa ma trận Fibonacci^(n-1)
    return result[0][0] # trả về phần tử ở hàng 0, cột 0 của ma trận kết quả    

print(fibonacci(10))  # Output: 55
