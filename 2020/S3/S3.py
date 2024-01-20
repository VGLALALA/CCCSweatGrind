from collections import Counter
s1 = input()
s1cnt = Counter(s1)
s2 = input()
visited = {}
cnt = 0
for i in range(len(s2)-len(s1)+1):
    newpart = s2[i:i + len(s1)]
    if visited.get(newpart):
        continue
    visited[newpart] = 1
    partcnt = Counter(newpart)
    if partcnt != s1cnt:
        continue
    cnt += 1
print(cnt)
