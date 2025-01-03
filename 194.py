# Viết bằng Python
# Bài 194: Tạo hàm tính khoảng cách ngắn nhất giữa hai nút trong đồ thị sử dụng thuật toán Dijkstra.

import heapq # Thư viện hỗ trợ hàng đợi ưu tiên (Priority Queue)
 
def dijkstra(graph, start): # Hàm tìm đường đi ngắn nhất từ một nút đến các nút khác trong đồ thị
    dist = {node: float('inf') for node in graph} # Khởi tạo khoảng cách từ nút start đến các nút khác là vô cực
    dist[start] = 0 # Khoảng cách từ nút start đến chính nó là 0
    pq = [(0, start)]  # Priority queue: (distance, node)

    while pq: # Duyệt đến khi hết nút trong hàng đợi ưu tiên
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]: # Nếu khoảng cách hiện tại lớn hơn khoảng cách đã biết
            continue

        for neighbor, weight in graph[current_node]: # Duyệt qua các nút kề của nút hiện tại
            distance = current_dist + weight # Tính khoảng cách từ nút start đến nút kề
            if distance < dist[neighbor]: # Nếu khoảng cách mới nhỏ hơn khoảng cách đã biết
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

graph = { # Đồ thị có hướng với trọng số cạnh dương
    0: [(1, 2), (4, 1)],
    1: [(2, 3)],
    2: [(3, 1)],
    3: [(4, 2)],
    4: [(1, 4)]
}

distances = dijkstra(graph, 0) # Tính khoảng cách từ nút 0 đến các nút khác
print(distances)  # Output: {0: 0, 1: 2, 2: 5, 3: 6, 4: 1}
