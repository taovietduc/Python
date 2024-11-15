# VIẾT BẰNG PYTHON
# Bài 140: Tạo hàm tính tổng các số chẵn trong một khoảng.

def sum_even_in_range(start, end): # start, end là các tham số truyền vào hàm sum_even_in_range
    total = 0 # total là biến lưu tổng các số chẵn trong khoảng từ start đến end
    for num in range(start, end + 1): 
    # Duyệt qua các số từ start đến end + 1 (vì range không lấy giá trị cuối cùng)
        if num % 2 == 0: # Nếu num chia hết cho 2 (là số chẵn) thì cộng vào tổng
            total += num # Cộng num vào tổng total 
    return total # Trả về tổng các số chẵn trong khoảng từ start đến end

# Ví dụ sử dụng
start = 1 # start = 1 là giá trị bắt đầu của khoảng
end = 10 # end = 10 là giá trị kết thúc của khoảng
print(f"Tổng các số chẵn từ {start} đến {end} là:", sum_even_in_range(start, end)) 

# Kết quả: Tổng các số chẵn từ 1 đến 10 là: 30
# Giải thích: Các số chẵn trong khoảng từ 1 đến 10 là 2, 4, 6, 8, 10. Tổng của chúng là 30
