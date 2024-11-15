# VIẾT BẰNG PYTHON
# Bài 122: Tạo hàm kiểm tra một số có phải là số Armstrong không.

def is_armstrong(num): # Hàm kiểm tra số Armstrong 
    digits = list(map(int, str(num)))  # Tách các chữ số của số thành danh sách
    power = len(digits)  # Số lượng chữ số của số ban đầu
    total = sum(d ** power for d in digits)  # Tính tổng các chữ số lũy thừa bậc power
    return total == num # So sánh tổng với số ban đầu để kiểm tra số Armstrong
 
# Ví dụ sử dụng
num = 153 # Số cần kiểm tra  
if is_armstrong(num): # Kiểm tra số Armstrong 
    print(f"{num} là số Armstrong.") 
else: # Nếu không phải số Armstrong 
    print(f"{num} không phải là số Armstrong.")
