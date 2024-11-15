# VIẾT BẰNG PYTHON
# Bài 143: Tạo hàm tìm tất cả các cặp số trong danh sách có tổng bằng một số cho trước.

def find_pairs_with_sum(lst, target_sum):
    # Hàm tìm tất cả các cặp số trong danh sách có tổng bằng target_sum
    pairs = []  # Khởi tạo danh sách rỗng để lưu các cặp số thỏa mãn
    n = len(lst)  # Lấy độ dài của danh sách đầu vào
    
    # Duyệt qua từng cặp số trong danh sách
    # Vòng lặp ngoài chạy từ phần tử đầu tiên đến kế cuối
    for i in range(n):
        # Vòng lặp trong chạy từ phần tử tiếp theo của i đến cuối
        # Điều này đảm bảo không lặp lại các cặp số và không so sánh số với chính nó
        for j in range(i + 1, n):
            # Kiểm tra nếu tổng của hai số bằng target_sum
            if lst[i] + lst[j] == target_sum:
                # Thêm cặp số thỏa mãn vào danh sách kết quả dưới dạng tuple
                pairs.append((lst[i], lst[j]))
                
    return pairs  # Trả về danh sách các cặp số có tổng bằng target_sum

# Ví dụ minh họa cách sử dụng hàm
numbers = [2, 4, 3, 5, 7, 8, 9]  # Danh sách số đầu vào
target = 12  # Số cần tìm tổng

# In ra các thông tin
print("Danh sách:", numbers)  # In danh sách đầu vào
print("Số cần tìm:", target)  # In số cần tìm tổng
print("Các cặp số có tổng bằng", target, "là:", find_pairs_with_sum(numbers, target))

# Kết quả chạy chương trình:
# Danh sách: [2, 4, 3, 5, 7, 8, 9]
# Số cần tìm: 12
# Các cặp số có tổng bằng 12 là: [(3, 9), (4, 8), (5, 7)]
# Giải thích: 
# - Cặp (3,9): 3 + 9 = 12
# - Cặp (4,8): 4 + 8 = 12  
# - Cặp (5,7): 5 + 7 = 12


