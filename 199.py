# Viết bằng Python
# Bài 199: Tìm phần tử xuất hiện nhiều nhất trong danh sách sử dụng HashMap.

def find_most_frequent(arr): # tìm phần tử xuất hiện nhiều nhất trong mảng
    frequency = {}  # dictionary để lưu số lần xuất hiện của phần tử
    max_count = 0 # số lần xuất hiện nhiều nhất của phần tử
    most_frequent = None    # phần tử xuất hiện nhiều nhất

    for num in arr:  # đếm số lần xuất hiện của từng phần tử
        frequency[num] = frequency.get(num, 0) + 1 # tăng số lần xuất hiện của phần tử lên 1
        if frequency[num] > max_count: # nếu số lần xuất hiện của phần tử lớn hơn số lần xuất hiện nhiều nhất
            max_count = frequency[num]   # cập nhật số lần xuất hiện nhiều nhất
            most_frequent = num # cập nhật phần tử xuất hiện nhiều nhất

    return most_frequent

arr = [1, 3, 2, 1, 4, 1, 3, 3] # Mảng đầu vào 
print(find_most_frequent(arr))  # Output: 1
