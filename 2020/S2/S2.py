from queue import Queue


r = int(input())
c = int(input())
graph = []
for i in range(r):
    row = input().split()
    graph.append([int(i)for i in row])


def findcoord(val,visited,r,c):
    coords = []
    for i in range(1,val+1):
        if i < r or val//i < c:
            newcoord = (i,(val//i))
            if val % i == 0 and not visited.get((i,(val//i))):
                coords.append(newcoord)
    return coords

def thing(graph,r,c):
    goal = (r-1,c-1)
    queue = Queue()
    queue.put((0,0))
    visited = {}
    while queue:
        state = queue.get()
        visited[state] = 1
        row,col = state
        if state == goal:
            return "yes"
        x = graph[row][col]
        neighbors = findcoord(x,visited,r,c)
        for neighbor in neighbors:
            queue.put(neighbor)
    return "no"
print(thing(graph,r,c))
