# Viết bằng Python
# Bài 200: Viết hàm kiểm tra xem danh sách có phải là một heap tối đa không.

def is_max_heap(arr): # Kiểm tra xem danh sách có phải là một heap tối đa không
    n = len(arr)
    for i in range((n - 2) // 2 + 1):  # duyệt từ n/2 đến 0 để kiểm tra từng nút
        if 2 * i + 1 < n and arr[i] < arr[2 * i + 1]: # nếu phần tử hiện tại nhỏ hơn con trái
            return False
        if 2 * i + 2 < n and arr[i] < arr[2 * i + 2]: # nếu phần tử hiện tại nhỏ hơn con phải
            return False
    return True

# Example usage
arr = [10, 9, 8, 7, 6, 5, 4] # Mảng đầu vào 
print(is_max_heap(arr))  # Output: True

arr = [10, 15, 8, 7, 6, 5, 4] # Mảng đầu vào
print(is_max_heap(arr))  # Output: False
