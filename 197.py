# Viết bằng Python
# Bài 197: Hàm tìm số gần nhất với một số cho trước trong danh sách.

def find_closest(arr, target): # arr: list, target: int -> int 
    closest = arr[0] # Gán giá trị đầu tiên của mảng là giá trị gần nhất
    min_diff = abs(arr[0] - target) # Gán giá trị đầu tiên của mảng là giá trị nhỏ nhất
    for num in arr: # Duyệt qua từng phần tử trong mảng
        diff = abs(num - target) # Tính hiệu giữa phần tử và giá trị target
        if diff < min_diff: # Nếu hiệu nhỏ hơn giá trị nhỏ nhất
            closest = num   # Gán giá trị gần nhất bằng phần tử hiện tại
            min_diff = diff # Gán giá trị nhỏ nhất bằng hiệu giữa phần tử và giá trị target
    return closest

arr = [10, 22, 28, 29, 30, 40]  # Mảng số nguyên tăng dần
target = 54 # Số cần tìm gần nhất
print(find_closest(arr, target))  # Output: 40
