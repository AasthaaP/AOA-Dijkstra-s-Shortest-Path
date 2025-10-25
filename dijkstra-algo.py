import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous

def get_path(previous, node):
    path = []
    while node is not None:
        path.insert(0, node)
        node = previous[node]
    return path

graph = {
    1: [(2, 1), (11, 1)],
    2: [(1, 1), (3, 1), (21, 1)],
    3: [(2, 1), (4, 1), (8, 2)],
    4: [(3, 1), (5, 1)],
    5: [(4, 1), (6, 2), (7, 1), (22, 1)],
    6: [(5, 2), (7, 1)],
    7: [(5, 1), (6, 1), (8, 1)],
    8: [(7, 1), (9, 1), (3, 2)],
    9: [(8, 1), (10, 1), (19, 1)],
    10: [(9, 1), (11, 1), (18, 2)],
    11: [(1, 1), (10, 1), (12, 2), (17, 1)],
    12: [(11, 2), (13, 2)],
    13: [(12, 2), (14, 2), (21, 1)],
    14: [(13, 2), (15, 1), (20, 1), (16, 1)],
    15: [(14, 1)],
    16: [(17, 2), (14, 1)],
    17: [(11, 1), (16, 2), (18, 2)],
    18: [(10, 2), (17, 2)],
    19: [(9, 1)],
    20: [(14, 1), (21, 2), (22, 1)],
    21: [(2, 1), (13, 1), (20, 2), (22, 2)],
    22: [(5, 1), (20, 1), (21, 2)],
}

source = 1
targets = [6, 8, 9, 15, 16, 22]

distances, previous = dijkstra(graph, source)

print(f"Final Shortest Path Information\n")
print(f"{'Destination Node':<18}{'Shortest Path Distance':<26}{'Shortest Path (one of)'}")
print("-" * 70)

for t in sorted(targets):  
    path = get_path(previous, t)
    path_str = " → ".join(map(str, path))
    print(f"Node {t:<5}{distances[t]:<25}{path_str}")

min_target = min(targets, key=lambda x: distances[x])
min_distance = distances[min_target]
print("\nCONCLUSION")
print(f"Node {min_target} is the most probable destination.")
print(f"It can be reached with the minimum total path weight of {min_distance}.")
