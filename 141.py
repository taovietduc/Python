# VIẾT BẰNG PYTHON
# Bài 141: Tìm phần tử có tần suất xuất hiện cao nhất trong danh sách.

from collections import Counter # Sử dụng Counter để đếm số lần xuất hiện của các phần tử trong danh sách

def most_frequent_element(lst): # Hàm tìm phần tử có tần suất xuất hiện cao nhất trong danh sách
    if not lst: # Nếu danh sách rỗng thì trả về None (không có phần tử nào)
        return None # Trả về None (không có phần tử nào)
    count = Counter(lst) # Đếm số lần xuất hiện của các phần tử trong danh sách
    return max(count, key=count.get) # Trả về phần tử có tần suất xuất hiện cao nhất trong danh sách

# Ví dụ sử dụng
lst = [1, 2, 3, 4, 2, 3, 2, 5, 5] # Danh sách các phần tử     
print("Phần tử có tần suất xuất hiện cao nhất:", most_frequent_element(lst)) 
# In ra phần tử có tần suất xuất hiện cao nhất trong danh sách

# Kết quả
# Phần tử có tần suất xuất hiện cao nhất: 2
# Phần tử 2 xuất hiện 3 lần trong danh
# sách, nhiều hơn các phần tử khác