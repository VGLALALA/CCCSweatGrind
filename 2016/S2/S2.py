mode = int(input())
b = int(input())
c = input().split(" ")
lst1 = [int(i)for i in c]
d = input().split(" ")
lst2 = [int(i)for i in d]
lst1.sort()
lst2.sort()
if mode == 2:
    lst2.reverse()
rtn = 0
for a,b in zip(lst1,lst2):
    rtn += (max(a,b))
print(rtn)
