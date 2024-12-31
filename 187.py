# Viết bằng Python
# Bài 187: Tạo hàm tìm số lớn nhất có thể tạo bằng cách sắp xếp lại các chữ số của một số.

def largest_number_from_digits(number): 
# number là số cần tìm số lớn nhất có thể tạo từ các chữ số của nó
    digits = sorted(str(number), reverse=True) # sắp xếp các chữ số của number giảm dần
    return int(''.join(digits)) # nối các chữ số lại và chuyển về kiểu số nguyên

# Ví dụ
number = 31245 # số cần tìm số lớn nhất có thể tạo từ các chữ số của nó
print(f"Số lớn nhất có thể tạo từ {number} là {largest_number_from_digits(number)}") 
# in ra số lớn nhất có thể tạo từ number 

# Kết quả
# Số lớn nhất có thể tạo từ 31245 là 54321
# Các chữ số của 31245 là 3, 1, 2, 4, 5. Sắp xếp chúng giảm dần ta được 5, 4, 3, 2, 1.
# Nối các chữ số lại ta được số lớn nhất có thể tạo từ 31245 là 54321
# Cách làm này cũng áp dụng được cho số âm.
# Ví dụ số -31245 sẽ cho kết quả là -54321.