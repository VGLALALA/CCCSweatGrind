n = int(input())
pic = list(map(int,input().split()))
outlst = [0 for _ in range(n)]
def precalculate(lst):
    n = len(lst)
    abs_diffs = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            abs_diffs[i][j] = abs_diffs[j][i] = abs(lst[i] - lst[j])
    return abs_diffs
def asymmetric(lst):
    n = len(lst)
    total = 0
    for i in range(n//2):
        total += abs(lst[i] - lst[-(i+1)])
    if n % 2 != 0:
        total += 0
    return total

def thing(n,pic,graph):
    outlst = [0 for _ in range(n+1)]
    for piclen in range(1, n + 1):
        lowest = float('inf')
        for j in range(n - piclen + 1):
            newpic = pic[j:j + piclen]
            lowest = min(asymmetric(newpic), lowest)
        outlst[piclen-1] = lowest
    return ' '.join(map(str, outlst[:-1]))
diffgraph = precalculate(pic)
lst = thing(n,pic,diffgraph)
print(lst)
