# VIẾT BẰNG PYTHON
# Bài 112: Tạo hàm sắp xếp các phần tử của danh sách số theo thứ tự tăng dần.

def sort_list_ascending(numbers): 
    # Sắp xếp các phần tử của danh sách số theo thứ tự tăng dần.

    # Parameters:
    # numbers (list): Danh sách các số.

    # Returns:
    # list: Danh sách đã được sắp xếp theo thứ tự tăng dần.
    return sorted(numbers)

# Ví dụ sử dụng
numbers = [5, 3, 8, 1, 2, 9] # Danh sách số cần sắp xếp
sorted_numbers = sort_list_ascending(numbers) # Sắp xếp các phần tử của danh sách số theo thứ tự tăng dần
print(f"Danh sách đã sắp xếp: {sorted_numbers}") # In danh sách đã sắp xếp

# Giải thích:
# Hàm sorted(): Hàm sorted() trong Python sắp xếp một danh sách và trả về một danh sách mới theo thứ tự tăng dần.
# Tham số: numbers là danh sách các số cần sắp xếp.
# Kết quả: Hàm trả về danh sách đã được sắp xếp theo thứ tự tăng dần.