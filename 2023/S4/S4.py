import heapq
def remove_road(graph, road):
    a1, a2, length, cost = road
    graph[a1] = [item for item in graph[a1] if item[0] != a2]
    graph[a2] = [item for item in graph[a2] if item[0] != a1]
def add_road(graph, road):
    a1, a2, length, cost = road
    graph[a1].append((a2, length, cost))
    graph[a2].append((a1, length, cost))

import heapq
def dj(graph, start, end, gone):
    queue = [(0, start, 0)]
    distances = {node: (float('infinity'), 0) for node in graph}
    distances[start] = (0, 0)
    visited = set()
    while queue:
        current_distance, current_node, current_weight = heapq.heappop(queue)
        if current_node == end:
            return current_distance, current_weight
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, distance_to_neighbor, weight_to_neighbor in graph[current_node]:
                if (current_node, neighbor) in gone or (neighbor, current_node) in gone:
                    continue
                if neighbor not in visited:
                    new_distance = current_distance + distance_to_neighbor
                    new_weight = current_weight + weight_to_neighbor
                    if new_distance < distances[neighbor][0] or \
                            (new_distance == distances[neighbor][0] and new_weight < distances[neighbor][1]):
                        distances[neighbor] = (new_distance, new_weight)
                        heapq.heappush(queue, (new_distance, neighbor, new_weight))
    return float('inf'), float('inf')


def thing(n,m,roads,graph):
    byebye = set()
    for road in roads:
        byebye.add(road)
        remove_road(graph, road)
        new_length, new_weight = dj(graph, road[0], road[1],byebye)
        if new_length > road[2]:
            byebye.remove(road)
            add_road(graph, road)
    out = sum(d for a, b, c, d in roads if (a, b, c, d) not in byebye)
    return out

def take_input():
    n, m = map(int, input().split())
    roads = []
    from collections import defaultdict
    graph = defaultdict(list)
    for _ in range(m):
        a1,a2,length,cost = map(int,input().split())
        graph[a1].append((a2,length,cost))
        graph[a2].append((a1, length, cost))
        roads.append((a1,a2,length,cost))
    return n, m, roads,graph
n, m, roads,graph = take_input()
print(thing(n, m, roads,graph))