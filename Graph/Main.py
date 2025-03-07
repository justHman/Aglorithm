
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    traces = {node: None for node in graph}
    queue = [(0, start)]

    while queue:
        curent_distance, curent_node = queue.pop(0)
        if curent_distance > distances[curent_node]:
            continue
        for neighbor, weight in graph[curent_node].items():
            distance = curent_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                traces[neighbor] = curent_node
                queue.append((distance, neighbor))
    
    return distances, traces

graph = {
    'A': {'B': 3, 'C': 6},
    'B': {'A': 3, 'C': 1, 'D': 7},
    'C': {'A': 6, 'B': 1, 'D':4},
    'D': {'B': 7, 'C': 4}
}

start = 'A'
d, p = dijkstra(graph, start)
print(sum(d.values()))
print(p)