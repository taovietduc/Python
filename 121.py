# VIẾT BẰNG PYTHON
# Bài 121: Tạo hàm tính tổng các số hoàn hảo trong một khoảng cho trước.

def is_perfect(num): # Hàm kiểm tra số hoàn hảo hay không                                   
    if num < 2: # Số hoàn hảo phải lớn hơn 1 nên trả về False nếu num < 2
        return False # Trả về False nếu num < 2
    sum_of_divisors = 1 # Khởi tạo sum_of_divisors = 1 vì 1 luôn là ước của mọi số
    for i in range(2, int(num ** 0.5) + 1): # Duyệt từ 2 đến căn bậc 2 của num + 1
        if num % i == 0: # Nếu num chia hết cho i thì i là ước của num 
            sum_of_divisors += i # Cộng i vào sum_of_divisors
            if i != num // i: # Nếu i khác num // i thì num // i cũng là ước của num
                sum_of_divisors += num // i # Cộng num // i vào sum_of_divisors
    return sum_of_divisors == num # Trả về True nếu sum_of_divisors == num, ngược lại trả về False

def sum_of_perfect_numbers(start, end): # Hàm tính tổng các số hoàn hảo trong khoảng từ start đến end
    total = 0
    for num in range(start, end + 1): # Duyệt từ start đến end + 1 để kiểm tra từng số
        if is_perfect(num): # Nếu num là số hoàn hảo thì cộng vào tổng 
            total += num # Cộng num vào tổng 
    return total

# Ví dụ sử dụng
start = 1 # Đầu khoảng
end = 10000 # Cuối khoảng   
print("Tổng các số hoàn hảo trong khoảng là:", sum_of_perfect_numbers(start, end)) 
# In ra tổng các số hoàn hảo trong khoảng từ 1 đến 10000
