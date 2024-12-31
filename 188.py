# Viết bằng Python
# Bài 188: Viết hàm kiểm tra xem một số có phải là số Harshad không.

def is_harshad(number): # number là số cần kiểm tra có phải là số Harshad không
    digits_sum = sum(int(digit) for digit in str(number))
    # tính tổng các chữ số của number
    return number % digits_sum == 0 
    # kiểm tra xem number chia hết cho tổng các chữ số của nó không


# Ví dụ
number = 18 # số cần kiểm tra có phải là số Harshad không
print(f"Số {number} có phải là số Harshad không? {is_harshad(number)}") 
# kiểm tra xem number có phải là số Harshad không

# Kết quả
# Số 18 có phải là số Harshad không? True
# Số 18 có tổng các chữ số là 1 + 8 = 9. 18 chia hết cho 9 nên 18 là số Harshad.
# Cách làm này cũng áp dụng được cho số âm.
# Ví dụ số -18 cũng là số Harshad vì tổng các chữ số của nó là 1 + 8 = 9 và -18 chia hết cho 9.
# Số 0 không phải là số Harshad vì không thể chia cho 0.
# Số 1 là số Harshad vì tổng các chữ số của nó là 1 và 1 chia hết cho 1.
# Số 10 không phải là số Harshad vì tổng các chữ số của nó là 1 + 0 = 1 và 10 không chia hết cho 1.