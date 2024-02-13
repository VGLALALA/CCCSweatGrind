def usaco_i(N, cows):
    rtn = {}
    for window in range(2, N + 1):
        counter = [0] * (10 ** 5)
        for i in range(0, N - window + 1):
            if (i == 0):
                for j in range(i, i + window):
                    cow = cows[j]
                    counter[cow] += 1

                max_food = max(counter)
                if (max_food > window // 2):
                    index = counter.index(max_food)
                    rtn[index] = True
            else:
                counter[cows[i - 1]] -= 1
                counter[cows[i + window - 1]] += 1

                if (counter[cows[i + window - 1]] > window // 2):
                    rtn[cows[i + window - 1]] = True

    if (len(rtn) == 0):
        return -1
    else:
        out = ""
        for key in rtn.keys():
            out += (str(key) + " ")
        return out[:-1]


def take_input():
    N = int(input())
    for i in range(N):
        n = int(input())
        cows = list(map(int, input().split()))
        rtn = usaco_i(n, cows)
        print(rtn)


take_input()
'''
5
5
1 2 2 2 3
6
1 2 3 1 2 3
6
1 1 1 2 2 2
3
3 2 3
2
2 1

'''


