from sys import stdin

rawinput = stdin.readline
m = int(rawinput())
n = int(rawinput())
changes = int(rawinput())
graph = []
for i in range(m):
        row = []
        for j in range(n):
            row.append('B')
        graph.append(row)
for i in range(changes):
    change, number = map(str,rawinput().split())
    number = int(number)
    if change == "R":
        for i in range(n):
            if graph[number-1][i] == "B":
                graph[number-1][i] = "G"
            else:
                graph[number-1][i] = "B"

    else:
        for i in range(m):
            if graph[i][number-1] == "B":
                graph[i][number-1] = "G"
            else:
                graph[i][number-1] = "B"
cnt = 0
for row in graph:
    for char in row:
        if char == "G":
            cnt += 1
print(cnt)
