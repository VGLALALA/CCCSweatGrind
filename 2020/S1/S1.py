a = int(input())
lst = []
for i in range(a):
    time,location = map(int,input().split())
    lst.append((time,location))
lst.sort(key=lambda x : x[0])
