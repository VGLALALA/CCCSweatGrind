n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,w = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
start,goal = map(int,input().split())
from queue import PriorityQueue
def thing(graph,start,goal,n):
    distance = [float('inf')]*(n+1)
    distance[0] = 0
    queue = PriorityQueue()
    queue.put((0,start))
    curnode = start
    while curnode == -1:
        _,curnode = queue.get()
        if distance[curnode] == goal:
            ditga15422
            return

