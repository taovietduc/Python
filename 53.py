# VIẾT BẰNG PYTHON
# Bài 53: Sắp xếp từ điển theo giá trị.

# Tạo từ điển trống
tu_dien = {} # hoặc tu_dien = dict() cũng được nhé

# Nhập số lượng phần tử trong từ điển
n = int(input("Nhập số lượng phần tử trong từ điển: ")) 

# Nhập từng cặp khóa và giá trị
for i in range(n): # range(n) tạo ra một dãy số từ 0 đến n-1
    khoa = input(f"Nhập khóa (tên trái cây) thứ {i+1}: ")
    gia_tri = int(input(f"Nhập giá trị (số lượng) cho '{khoa}': ")) # giá trị nhập vào là số nguyên nên dùng int()
    tu_dien[khoa] = gia_tri # thêm cặp khóa và giá trị vào từ điển

# Sắp xếp từ điển theo giá trị
tu_dien_sap_xep = dict(sorted(tu_dien.items(), key=lambda item: item[1])) # sắp xếp từ điển theo giá trị (item[1])

# In từ điển đã sắp xếp theo giá trị 
print("Từ điển sau khi sắp xếp theo giá trị là:") 
for khoa, gia_tri in tu_dien_sap_xep.items(): # duyệt từng cặp khóa và giá trị trong từ điển đã sắp xếp
    print(f"{khoa}: {gia_tri}") 
