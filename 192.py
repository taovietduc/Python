# Viết bằng Python
# Bài 192: Tạo thuật toán kiểm tra xem một đồ thị biểu diễn bằng danh sách cạnh có chu trình hay không.

class UnionFind: # Hợp nhất và tìm kiếm phần tử trong tập hợp
    def __init__(self, n): # khởi tạo n phần tử với các phần tử đều là cha của chính nó
        self.parent = list(range(n)) # cha của chính nó
        self.rank = [0] * n # rank của mỗi phần tử

    def find(self, x): # tìm kiếm phần tử x trong tập hợp
        if self.parent[x] != x: # nếu cha của x khác chính nó
            self.parent[x] = self.find(self.parent[x]) # tìm kiếm cha của cha của x
        return self.parent[x] # trả về cha của x

    def union(self, x, y): # hợp nhất hai tập hợp chứa x và y
        root_x = self.find(x) # tìm kiếm cha của x
        root_y = self.find(y) # tìm kiếm cha của y
        if root_x == root_y: # nếu cha của x và cha của y giống nhau
            return False  # Cycle detected
        if self.rank[root_x] > self.rank[root_y]: # nếu rank của cha của x lớn hơn rank của cha của y
            self.parent[root_y] = root_x # cha của y là x
        elif self.rank[root_x] < self.rank[root_y]: 
        # nếu rank của cha của x nhỏ hơn rank của cha của y
            self.parent[root_x] = root_y # cha của x là y
        else: # nếu rank của cha của x bằng rank của cha của y
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def has_cycle(n, edges): # kiểm tra xem đồ thị có chu trình hay không
    uf = UnionFind(n) # khởi tạo tập hợp với n phần tử
    for u, v in edges:
        if not uf.union(u, v): # hợp nhất hai tập hợp chứa u và v
            return True
    return False

edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)]
print(has_cycle(5, edges))  # Output: True

