import sys
from sys import stdin
rawinput = stdin.readline

def cutcut(graph,phos):
    for node in range(len(graph)):
        while len(graph[node]) == 1 and node not in phos:
            adj = list(graph[node])[0]
            graph[adj].remove(node)
            graph[node].remove(adj)
            node = adj
    return graph

def bfs(start,graph):
    stack = [(start,0)]
    visited = {}
    length = 0
    node = start
    while stack:
        state,dis = stack.pop()
        visited[state] = 1
        if dis > length:
            node = state
            length = dis
        for neighbor in graph[state]:
            if neighbor not in visited:
                stack.append((neighbor,dis+1))
    return node,length

def findlength(graph):
    return sum(len(v) != 0 for v in graph) - 1
def thing(graph,phos):
    graph = cutcut(graph,phos)
    start,_ = bfs(list(phos)[0],graph)
    end,enddistance = bfs(start,graph)
    distance = (findlength(graph))*2-enddistance
    print(distance)


def takeinput():
    N, M = map(int, input().split())
    pho = set(map(int, input().split()))

    graph = [set() for _ in range(N)]  # create graph from input
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    return N, M, pho, graph
N, M, phos, graph = takeinput()
thing(graph,phos)
sys.exit()