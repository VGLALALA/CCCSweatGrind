n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
start,goal = map(int,input().split())
from queue import PriorityQueue
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
def queuedijkstra(graph,start,goal,n):
    distance = [float('inf')]*(n+1)
    distance[start] = 0
    queue = PriorityQueue()
    queue.put((0,start))
    curnode = start
    while curnode != -1:
        _,curnode = queue.get()
        if curnode == goal:
            return distance[curnode]
        for neighbor,neighbor_weight in graph[curnode]:
            new_distance = distance[curnode] + neighbor_weight
            if distance[neighbor] > new_distance:
                distance[neighbor] = new_distance
                queue.put((new_distance,neighbor))
    return -1

print(queuedijkstra(graph,start,goal,n))


#Heap
import heapq
def heapdijkstra(src, target, N, graph):
    distances = [float('inf')] * (N+1)
    distances[src] = 0
    pq = [(0, src)]

    while pq:
        dist, curnode = heapq.heappop(pq)

        if curnode == target:
            return dist

        for adj, adj_weight, in graph[curnode]:

            new_distance = distances[curnode] + adj_weight

            if (distances[adj] > new_distance):
                heapq.heappush(pq, (new_distance, adj))
                distances[adj] = new_distance

    return float('inf')
