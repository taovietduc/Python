# Viết bằng Python
# Bài 198: Tìm cặp phần tử có hiệu nhỏ nhất trong danh sách.

def find_min_difference_pair(arr): # Hàm tìm cặp phần tử có hiệu nhỏ nhất trong danh sách
    arr.sort() # Sắp xếp danh sách theo thứ tự tăng dần
    min_diff = float('inf') # khởi tạo min_diff = vô cực
    pair = None # khởi tạo cặp phần tử là None

    for i in range(len(arr) - 1): 
        diff = arr[i + 1] - arr[i] 
        if diff < min_diff: # nếu hiệu nhỏ hơn min_diff thì cập nhật min_diff và cập nhật cặp phần tử
            min_diff = diff # cập nhật min_diff = diff mới tìm được
            pair = (arr[i], arr[i + 1]) # cập nhật cặp phần tử mới tìm được

    return pair

arr = [1, 5, 3, 19, 18, 25] # khởi tạo danh sách arr
print(find_min_difference_pair(arr))  # Output: (18, 19)
