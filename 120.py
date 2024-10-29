# VIẾT BẰNG PYTHON
# Bài 120: Tạo hàm tính tích các phần tử trong một danh sách.

def product_of_elements(lst): # Hàm tính tích các phần tử trong danh sách
    product = 1 # Khởi tạo giá trị tích bằng 1 để nhân từng phần tử vào
    for num in lst: # Duyệt từng phần tử trong danh sách lst 
        product *= num  # Nhân từng phần tử vào tích 
    return product # Trả về giá trị tích sau khi nhân hết các phần tử trong danh sách

# Ví dụ sử dụng
lst = [2, 3, 4] # Danh sách các phần tử cần tính tích   
print("Tích các phần tử trong danh sách là:", product_of_elements(lst)) 
# In ra giá trị tích của các phần tử trong danh sách lst là 24 (2*3*4 = 24)
