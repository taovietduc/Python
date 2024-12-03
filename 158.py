# Viết Bằng Python
# Bài 158: Viết hàm kiểm tra xem một chuỗi có thể được tạo bằng cách lặp lại một đoạn con nào đó hay không.

def check_repeating_substring(s):
    """
    Kiểm tra xem chuỗi s có thể được tạo bằng cách lặp lại một đoạn con hay không
    
    Args:
        s: chuỗi cần kiểm tra
        
    Returns:
        True nếu chuỗi có thể được tạo bằng lặp lại đoạn con
        False nếu không thể
    """
    n = len(s)
    # Kiểm tra các độ dài có thể của đoạn con
    for length in range(1, n//2 + 1):
        # Chỉ xét các độ dài là ước của độ dài chuỗi
        if n % length == 0:
            # Lấy đoạn con đầu tiên có độ dài length
            substring = s[:length]
            # Số lần lặp cần thiết
            repeat_times = n // length
            # Tạo chuỗi bằng cách lặp lại đoạn con
            constructed = substring * repeat_times
            # So sánh với chuỗi gốc
            if constructed == s:
                return True
    return False

# Ví dụ sử dụng:
print("Test 1:", check_repeating_substring("abcabc"))  # True (lặp lại "abc")
print("Test 2:", check_repeating_substring("aaaa"))    # True (lặp lại "a")
print("Test 3:", check_repeating_substring("abcd"))    # False
print("Test 4:", check_repeating_substring("ababab"))  # True (lặp lại "ab")

