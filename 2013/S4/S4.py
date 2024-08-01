import sys
def readin():
    rawinput = sys.stdin.readline
    n, m = map(int, rawinput().split())
    dic = {}
    for i in range(m):
        x,y = map(int, rawinput().split())
        if dic.get(x):
            dic[x].append(y)
        else:
            dic[x] = [y]
    p,q = map(int, rawinput().split())
    return dic,p,q
heightdic,p,q = readin()
def dfs(heightdic,start,goal):
    stack = [start]
    visited = set()
    while stack:
        state = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return True
        if state in heightdic:
            stack.extend(heightdic[state])
    return False
if dfs(heightdic,p,q):
    print("yes")
elif dfs(heightdic,q,p):
    print("no")
else: print("unknown")
