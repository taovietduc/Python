# VIẾT BẰNG PYTHON
# Bài 152: Tạo hàm tính tổng các phần tử lớn nhất và nhỏ nhất ở mỗi cấp độ của một cây nhị phân.

class Node: # Tạo cấu trúc Node cho cây nhị phân
    def __init__(self, data): # Constructor khởi tạo node với giá trị và con trỏ null
        self.data = data      # Giá trị của node
        self.left = None      # Con trỏ đến node con trái
        self.right = None     # Con trỏ đến node con phải

def sum_max_min_at_each_level(root): 
# Hàm tính tổng các phần tử lớn nhất và nhỏ nhất ở mỗi cấp độ của cây nhị phân
    # Nếu cây rỗng thì trả về   
    if not root: # Nếu cây rỗng thì trả về  
        print("Cây rỗng!") # In ra màn hình
        return
        
    # Sử dụng queue để duyệt BFS
    queue = [root] # Khởi tạo queue với root
    
    # Duyệt từng level của cây
    while queue:
        # Lấy số node ở level hiện tại
        level_size = len(queue) # Lấy số node ở level hiện tại
        
        # Khởi tạo giá trị max, min cho level hiện tại
        max_val = float('-inf') # Khởi tạo giá trị max, min cho level hiện tại      
        min_val = float('inf') # Khởi tạo giá trị min cho level hiện tại
        
        # Duyệt qua các node ở level hiện tại
        for _ in range(level_size):
            # Lấy node đầu queue
            node = queue.pop(0) # Lấy node đầu queue
            
            # Cập nhật max, min
            max_val = max(max_val, node.data) # Cập nhật giá trị max
            min_val = min(min_val, node.data) # Cập nhật giá trị min
            
            # Thêm các node con vào queue
            if node.left: # Nếu node con trái khác null
                queue.append(node.left) # Thêm node con trái vào queue  
            if node.right: # Nếu node con phải khác null
                queue.append(node.right) # Thêm node con phải vào queue
                
        # In tổng max + min của level hiện tại
        print(f"Level sum (max + min): {max_val + min_val}") # In tổng max + min của level hiện tại

# Test thử hàm
if __name__ == "__main__":
    # Tạo cây nhị phân mẫu
    root = Node(10) # Khởi tạo root với giá trị 10      
    root.left = Node(2) # Thêm node con trái với giá trị 2
    root.right = Node(15) # Thêm node con phải với giá trị 15
    root.left.left = Node(1) # Thêm node con trái của node con trái với giá trị 1
    root.left.right = Node(5) # Thêm node con phải của node con trái với giá trị 5
    root.right.left = Node(12) # Thêm node con trái của node con phải với giá trị 12
    root.right.right = Node(20) # Thêm node con phải của node con phải với giá trị 20
    
    print("Tổng max và min tại mỗi level:") # In ra màn hình
    sum_max_min_at_each_level(root) # Gọi hàm tính tổng max min tại mỗi level

"""
Giải thích chi tiết:

1. Cấu trúc Node:
   - data: giá trị của node
   - left, right: con trỏ đến node con trái và phải
   - Constructor khởi tạo node với giá trị và con trỏ null

2. Hàm sum_max_min_at_each_level():
   - Sử dụng BFS (Breadth-First Search) với queue để duyệt từng level
   - Tại mỗi level:
     + Lưu số lượng node của level hiện tại
     + Khởi tạo maxVal = -inf, minVal = inf
     + Duyệt qua tất cả node trong level:
       * Cập nhật max, min
       * Thêm các node con vào queue
     + In tổng của max và min tại level đó

3. Hàm main:
   - Tạo cây nhị phân mẫu để test
   - Gọi hàm tính tổng max min tại mỗi level

4. Độ phức tạp:
   - Thời gian: O(n) với n là số node trong cây
   - Không gian: O(w) với w là độ rộng lớn nhất của cây

5. Ví dụ cây nhị phân:
           10
         /    \
        2      15
       / \    /  \
      1   5  12   20

   Output:
   Level 0: 10 + 10 = 20
   Level 1: 2 + 15 = 17
   Level 2: 1 + 20 = 21
"""
