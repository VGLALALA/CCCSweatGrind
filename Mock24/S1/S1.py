import math

def min_marbles(n, k, s):

    if n == 0 or k > n:
        return 0
    elif k == 0:
        return n

    empty_slots = []
    current_empty_count = 1
    for i in range(n - 1):
        if s[i] == '0' and s[i + 1] == '0':
            current_empty_count += 1
        else:
            empty_slots.append(current_empty_count)
            current_empty_count = 1
    empty_slots.append(current_empty_count)

    max_empty_intervals = int(min(k, math.floor((n - 1) / 2)) if n % 2 == 0 else min(k, (n + 1) // 2))
    merged_marbles = sum([empty_slots[i] for i in range(max_empty_intervals)] + [1])

    return n - merged_marbles if k >= max_empty_intervals else n

n,k = map(int,input().split())
s = input()
print(min_marbles(n,k,s))
