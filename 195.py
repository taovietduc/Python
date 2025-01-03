# Viết bằng Python
# Bài 195: Viết hàm sắp xếp danh sách bằng thuật toán Merge Sort.

def merge_sort(arr): # Hàm sắp xếp danh sách bằng thuật toán Merge Sort
    if len(arr) > 1: # Nếu danh sách có nhiều hơn một phần tử
        mid = len(arr) // 2 # Tìm vị trí giữa của danh sách
        left = arr[:mid] # Chia danh sách thành hai phần
        right = arr[mid:] # Phần đầu từ 0 đến mid, phần sau từ mid đến cuối

        merge_sort(left) # Sắp xếp phần đầu
        merge_sort(right) # Sắp xếp phần sau

        i = j = k = 0 # Khởi tạo biến đếm cho 3 phần

        while i < len(left) and j < len(right): # Duyệt qua cả hai phần
            if left[i] < right[j]:  # So sánh giữa hai phần để sắp xếp
                arr[k] = left[i]
                i += 1
            else: # Nếu phần bên phải nhỏ hơn
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left): # Duyệt qua phần còn lại của phần trái
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right): # Duyệt qua phần còn lại của phần phải
            arr[k] = right[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10] # Danh sách cần sắp xếp
merge_sort(arr) # Sắp xếp danh sách
print(arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
