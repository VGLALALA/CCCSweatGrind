from queue import Queue

N, W, D = map(int, input().split())
route = [[] for _ in range(N + 1)]
wd = [200002] * (N + 1)
def bfs(n):
    vis = [False] * (N + 1)
    vis[n] = True
    wd[n] = 0
    q = Queue()

    q.put(n)
    while not q.empty():
        cs = q.get()
        for i in route[cs]:
            if not vis[i]:
                wd[i] = wd[cs] + 1
                vis[i] = True
                q.put(i)
for _ in range(W):
    m, n = map(int, input().split())
    route[n].append(m)
bfs(N)
sl = [0] * (N + 1)
cd = []
for a in range(1, N + 1):
    sl[a] = int(input())
    cd.append(a - 1 + wd[sl[a]])
for _ in range(D):
    s1, s2 = map(int, input().split())
    s1_od = s1 - 1 + wd[sl[s1]]
    s2_od = s2 - 1 + wd[sl[s2]]
    if s1_od in cd:
        cd.remove(s1_od)
    if s2_od in cd:
        cd.remove(s2_od)
    sl[s1], sl[s2] = sl[s2], sl[s1]
    cd.append(s1 - 1 + wd[sl[s1]])
    cd.append(s2 - 1 + wd[sl[s2]])
    print(min(cd))
