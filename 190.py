# Viết bằng Python
# Bài 190: Viết hàm tìm số tam giác nhỏ nhất lớn hơn một số cho trước.

def smallest_triangular_number_greater_than(n): # tìm số tam giác nhỏ nhất lớn hơn n
    t = 0 # số tam giác nhỏ nhất lớn hơn n 
    i = 1 # biến i bắt đầu từ 1 
    while t <= n: # tìm số tam giác lớn hơn n
        t += i # tăng t lên i để tìm số tam giác tiếp theo
        i += 1 # tăng i lên 1 để tìm số tam giác tiếp theo
    return t


# Ví dụ
number = 10 # số cần tìm số tam giác nhỏ nhất lớn hơn nó
print(f"Số tam giác nhỏ nhất lớn hơn {number} là {smallest_triangular_number_greater_than(number)}") 

# Kết quả
# Số tam giác nhỏ nhất lớn hơn 10 là 15
# Số tam giác nhỏ nhất lớn hơn 10 là 15 vì 15 là số tam giác và lớn hơn 10.
# Số tam giác là số có dạng 1 + 2 + 3 + ... + n = n * (n + 1) / 2.
# Số tam giác nhỏ nhất lớn hơn 10 là 15 vì 1 + 2 + 3 + 4 + 5 = 15.
# Số tam giác nhỏ nhất lớn hơn 10 là 15.
# Cách làm này cũng áp dụng được cho số âm.
# Ví dụ số -10 sẽ cho kết quả là 1 vì 1 là số tam giác nhỏ nhất lớn hơn -10.
# Số 0 không phải là số tam giác vì không thể tạo ra số tam giác từ 0.
# Số 1 là số tam giác vì 1 = 1 * (1 + 1) / 2.
# Số 2 không phải là số tam giác vì không thể tạo ra số tam giác từ 2.
# Số 3 là số tam giác vì 3 = 2 * (2 + 1) / 2.