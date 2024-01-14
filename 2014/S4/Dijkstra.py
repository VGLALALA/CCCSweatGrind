"""
4 7
1 2 4
1 3 7
3 1 8
3 2 2
4 2 1
3 4 1
1 4 6
1 4
"""
from queue import PriorityQueue
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))
start, goal = map(int, input().split())
"[[(2, 4), (3, 7), (3, 8), (4, 6)], [(1, 4), (3, 2), (4, 1)], [(1, 7), (1, 8), (2, 2), (4, 1)], [(2, 1), (3, 1), (1, 6)]]"



def dijkstra(graph, src, N, target):
    distance = [1e7] * (N + 1)                              # Set all distance to the src = infity
    distance[src] = 0                                       # Set src to src = 0

    q = PriorityQueue()
    q.put((0, src))

    curnode = src

    while(curnode != -1):
        _, curnode = q.get()

        if (curnode == target):
            print(distance[target])
            return

        for adj, adj_weight in graph[curnode]:
            new_distance = distance[curnode] + adj_weight

            if (distance[adj] > new_distance):
                distance[adj] = distance[curnode] + adj_weight
                q.put((new_distance, adj))

    print(-1)
print(dijkstra(graph,start,N,M,goal))
