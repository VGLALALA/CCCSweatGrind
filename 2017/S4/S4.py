def handle_in():
    n,m,d = map(int,input().split())
    lst = []
    for i in range(1, m + 1):
        b = map(int,input().split())
        lst.append(b)
    lst = sorted(lst, key=lambda x: x[-1])
    return n,m,d,lst


def thing(edges):
    visited = []
    mst = []




print(handle_in())