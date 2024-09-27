# VIẾT BẰNG PYTHON 
# In từ điển: Nhập một từ điển và in ra các khóa và giá trị của từ điển.

# Nhập từ điển từ bàn phím (có thể dưới dạng JSON)
tu_dien = eval(input("Nhập từ điển (dưới dạng {'key': 'value', ...}): ")) 
# eval() để chuyển chuỗi thành từ điển    

# In các khóa và giá trị của từ điển
print("Các khóa và giá trị trong từ điển là:")
for key, value in tu_dien.items(): # duyệt từng cặp khóa-giá trị
    print(f"{key}: {value}") # in khóa và giá trị

