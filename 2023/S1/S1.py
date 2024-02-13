a = int(input())
r1 = list(map(int,input().split()))
r2 = list(map(int,input().split()))
prev1 = False
prev2 = False
out = 0
col = 0
for col1,col2 in zip(r1,r2):
    if col1 == 1 and col2 == 1:
        if prev1 and prev2:
            if col % 2 == 0:
                out += 0
            else:
                out += 2
        elif prev1 or prev2:
            out += 2
        else:
            out += 4
        prev1, prev2 = True, True
    elif col1 == 1:
        if prev1:
            out += 1
        else:
            out += 3
        prev1, prev2 = True, False
    elif col2 == 1:
        if prev2:
            out += 1
        else:
            out += 3
        prev1,prev2 = False,True
    else:
        prev1,prev2 = False,False
    col += 1
print(out)