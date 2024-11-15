# VIẾT BẰNG PYTHON
# Bài 150: Viết hàm xác định xem một số có phải là số Catalan không.

def is_catalan(n):
    # Nếu n <= 0, không phải số Catalan
    if n <= 0: 
        return False
        
    # Tính số Catalan thứ i cho đến khi vượt quá n
    catalan = 1  # Số Catalan thứ 0
    i = 0  # Chỉ số hiện tại
    
    while catalan <= n:
        if catalan == n:  # Nếu tìm thấy số Catalan bằng n
            return True
        # Tính số Catalan tiếp theo theo công thức: C(i+1) = C(i) * 2*(2i+1)/(i+2)
        i += 1
        catalan = catalan * 2 * (2*i - 1) // (i + 1)
        
    return False  # Không tìm thấy số Catalan bằng n

# Test thử hàm
test_cases = [1, 2, 5, 14, 42, 132, 429, 7, 10]  # Các số test
for num in test_cases: # Duyệt qua các test case 
    result = is_catalan(num) # Kiểm tra số Catalan      
    print(f"Số {num} {'là' if result else 'không phải là'} số Catalan") # In ra kết quả

"""
Giải thích chi tiết:

1. Hàm is_catalan(n):
   - Input: Số nguyên n cần kiểm tra
   - Output: True nếu n là số Catalan, False nếu không phải

2. Các bước thực hiện:
   - Kiểm tra n <= 0: không phải số Catalan
   - Khởi tạo:
     + catalan = 1 (số Catalan đầu tiên C0)
     + i = 0 (chỉ số hiện tại)
   
   - Vòng lặp while:
     + So sánh catalan với n
     + Nếu bằng nhau -> return True
     + Tính số Catalan tiếp theo theo công thức:
       C(n+1) = C(n) * 2*(2n+1)/(n+2)
     + Nếu vượt quá n -> return False

3. Dãy số Catalan đầu tiên:
   1, 1, 2, 5, 14, 42, 132, 429, 1430,...

4. Test cases:
   - Kiểm tra các số trong dãy và ngoài dãy Catalan
   - In kết quả kiểm tra cho mỗi số
"""



