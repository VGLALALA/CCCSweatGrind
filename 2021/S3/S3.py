a = int(input())
friends = []
for i in range(a):
    p,w,d = map(int,input().split())
    friends.append([p,w,d])
friends.sort(key = lambda x:x[0])


def calpersontime(p,w,d,concert):
    if abs(p - concert - 1) > d:
        return (abs(p - concert - 1) - d) * w
    return 0
def binarysearch(lst):
    left = lst[0][0]
    right = lst[-1][0]
    while left < right:
        mid = (right+left)//2
        lefttime = 0
        righttime = 0
        concerttime = 0
        for person in lst:
            p, w, d = person
            righttime += calpersontime(p,w,d,mid + 1)
            lefttime += calpersontime(p,w,d,mid - 1)
            concerttime += calpersontime(p,w,d,mid)
        if lefttime > concerttime and righttime > concerttime or concerttime == righttime or concerttime == lefttime:
            return concerttime
        if lefttime < righttime:
            right = mid
        elif righttime < lefttime:
            left = mid

if a == 1:
    print(0)
else:
    print(binarysearch(friends))

