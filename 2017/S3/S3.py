def takeinput():
    a = int(input())
    woods = list(map(int,input().split()))
    return a,woods
def thingy(a,woods):
    from collections import defaultdict
    visited = set()
    dic = defaultdict(int)
    for i in range(a):
        for j in range(i+1,a):
            newvalue = woods[i] + woods[j]
            if (i,newvalue) not in visited and (j,newvalue) not in visited:
                dic[newvalue] += 1
                visited.add((j,newvalue))
                visited.add((i,newvalue))
    max_value = max(dic.values())
    keys_with_max_value = [k for k, v in dic.items() if v == max_value]
    return max_value,len(keys_with_max_value)

a,woods = takeinput()
print(" ".join(map(str, thingy(a,woods))))

