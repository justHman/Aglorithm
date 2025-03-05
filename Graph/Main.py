import heapq

def dijkstra(graph, start):
    # Khởi tạo khoảng cách và hàng đợi ưu tiên
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def shortest_path(previous_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    
    if path[0] == start:
        return path
    else:
        return []  # Không tìm thấy đường đi

# Định nghĩa đồ thị dưới dạng danh sách kề
graph = {
    '0': {'1': 2.5, '2': 2, '3': 2.1},
    '1': {'0': 2.5, '4': 1},
    '2': {'0': 2, '4': 0.6, '5': 1.5},
    '3': {'0': 2.1, '5': 2.5},
    '4': {'1': 1, '2': 0.6, '6': 2.3},
    '5': {'2': 1.5, '3': 2.5, '6': 1.9, '7': 2},
    '6': {'4': 2.3, '5': 1.9, '7': 1.8, '8': 1.7},
    '7': {'5': 2, '6': 1.8, '8': 2},
    '8': {'6': 1.7, '7': 2}
}

start_node = '0'
end_node = '4'

distances, previous_nodes = dijkstra(graph, start_node)
path = shortest_path(previous_nodes, start_node, end_node)

print(f"Khoảng cách ngắn nhất từ {start_node} đến {end_node}: {distances[end_node]}")
print(f"Đường đi ngắn nhất: {path}")
