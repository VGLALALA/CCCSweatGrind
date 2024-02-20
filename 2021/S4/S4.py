N, W, D = map(int, input().split())

walkways = {}
for _ in range(W):
    a, b = map(int, input().split())
    if not walkways.get(b):
        walkways[b] = []
    walkways[b].append(a)

subway = [0] + list(map(int, input().split()))

changes = []
for _ in range(D):
    changes.append(list(map(int, input().split())))
import heapq
def find_short_dic(n, walkway):
    from queue import Queue
    dic = {}
    if walkway.get(n) == None:
        return dic
    queue = Queue()
    queue.put((n, 0))
    visited = {}
    while not queue.empty():
        cur, time = queue.get()
        for node in walkway[cur]:
            if not visited.get(node):
                visited[node] = True
                if walkway.get(node):
                    queue.put([node, time + 1])
                dic[node] = time + 1
    return dic


def thing(walkways, swaplst, route, n, d):
    short_dic = find_short_dic(n, walkways)
    for i in range(d):
        station1, station2 = swaplst[i]
        route[station1], route[station2] = route[station2], route[station1]
        print(toschooltime(n, route, short_dic))


def toschooltime(n, route, short_dic):
    mintime = 400000
    for i in range(1, n + 1):
        station_d = route[i]
        if short_dic.get(station_d) != None:
            time = (i - 1) + short_dic[station_d]
            mintime = min(time, mintime)

    return mintime


thing(walkways, changes, subway, N, D)