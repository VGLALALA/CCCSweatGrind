def takeinput():
    r = int(input())
    c = int(input())
    p = [list(input()) for _ in range(r)]
    a = int(input())
    b = int(input())
    return r,c,p,a,b
def thing(r,c,graph,a,b):
    def helper(x, y):
        return 0 <= x < r and 0 <= y < c and p[x][y] != '*'
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    values = {'S': 1, 'M': 5, 'L': 10}
    stack = [(a,b)]
    visited = set()
    cnter = 0
    while stack:
        state = stack.pop()
        x, y = state
        if not helper(x, y) or (x,y) in visited:
            continue
        visited.add(state)
        if p[x][y] in values:
            cnter += values[graph[x][y]]
        for dx,dy in dirs:
            nx,ny = dx + x, dy + y
            stack.append((nx,ny))
    return cnter
r,c,p,a,b = takeinput()
print(thing(r,c,p,a,b))

# 6
# 6
# **LMLS
# S*LMMS
# S*SMSM
# ******
# LLM*MS
# SSL*SS
# 5
# 1
