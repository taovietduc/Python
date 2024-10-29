# VIẾT BẰNG PYTHON
# Bài 119: Tạo hàm kiểm tra một danh sách có phải là danh sách giảm dần hay không.

def is_descending(lst): # Hàm kiểm tra danh sách có phải là giảm dần hay không
    for i in range(len(lst) - 1): # Duyệt từ phần tử đầu đến phần tử trước phần tử cuối
        if lst[i] < lst[i + 1]:  # Nếu một phần tử nhỏ hơn phần tử tiếp theo
            return False # Thì danh sách không phải là giảm dần
    return True

# Ví dụ sử dụng hàm
lst = [9, 7, 5, 3, 1] # Danh sách giảm dần từ 9 đến 1
if is_descending(lst): # Kiểm tra danh sách có phải là giảm dần hay không
    print("Danh sách là giảm dần.") 
else: # Nếu không phải là giảm dần thì in ra danh sách không phải là giảm dần
    print("Danh sách không phải là giảm dần.")
