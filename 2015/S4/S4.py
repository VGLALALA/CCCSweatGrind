from queue import PriorityQueue


def take_input():
    hull, n_islands, n_routes = map(int, input().split())
    graph = [[] for _ in range(n_islands + 1)]

    for _ in range(n_routes):
        a, b, pt, dmg = map(int, input().split())
        graph[a].append((b, pt, dmg))
        graph[b].append((a, pt, dmg))
    start, end = map(int, input().split())
    return hull, n_islands, graph, start, end
def minDistance(distance, spf, N):
    min = 1e7
    min_index = -1
    for v in range(N):
        if distance[v] < min and spf[v] == False:
            min = distance[v]
            min_index = v

    return min_index
def dijkstra(graph, src, N, K, target):
    distance = [1e7] * (N + 1)
    distance[src] = 0
    hull = [0] * (N + 1)
    shortest_path_found = [False] * (N + 1)
    curnode = src
    while curnode != -1:
        curnode = minDistance(distance, shortest_path_found, N + 1)
        if curnode == target:
            print(distance[target])
            return
        shortest_path_found[curnode] = True
        for adj, adj_weight, hullval in graph[curnode]:
            new_hull = hull[curnode] + hullval
            if shortest_path_found[adj] == False and distance[adj] > distance[curnode] + adj_weight and new_hull < K:
                distance[adj] = distance[curnode] + adj_weight
                hull[adj] = new_hull

    print(-1)


hull, n_islands, graph, start, end = take_input()
dijkstra(graph, start, n_islands, hull, end)
