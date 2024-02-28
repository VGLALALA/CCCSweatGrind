def takeinput():
    r = int(input())
    c = int(input())
    p = [list(input()) for _ in range(r)]
    a = int(input())
    b = int(input())
    return r,c,p,a,b


def thing2(r, c, p, a, b):
    def helper(x, y):
        return 0 <= x < r and 0 <= y < c and p[x][y] != '*'
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total = 0
    values = {'S': 1, 'M': 5, 'L': 10}
    stack = [(a,b)]
    visited = set()
    while stack:
        x,y = stack.pop()
        if not helper(x, y) or (x,y) in visited:
            continue
        visited.add((x, y))
        if p[x][y] in values:
            total += values[p[x][y]]
        for dx,dy in dirs:
            nx,ny = x + dx,y + dy
            if (nx, ny) not in visited:
                stack.append((nx,ny))
    return total
r,c,p,a,b = takeinput()
print(thing2(r,c,p,a,b))
