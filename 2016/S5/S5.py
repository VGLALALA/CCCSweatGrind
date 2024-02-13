def thing(gen,seq,n):
    remaining = gen
    while remaining:
        jump = findjump(remaining)
        remaining -= jump
        newseq = []
        for i in range(n):
            left = (i - jump) % n
            right = (i + jump) % n
            newseq.append(seq[left] ^ seq[right])
        seq = newseq
    seq = [str(num)for num in seq]
    return seq

def findjump(gen):
    cnt = 0
    if gen < 2:
        return 1
    while gen > 1:
        gen //= 2
        cnt += 1
    return 2 ** cnt

def takeinput():
    n,gen = map(int,input().split())
    seq = []
    numseq = input()
    for char in numseq:
        seq.append(int(char))
    return n,gen,seq
n,gen,seq = takeinput()
print("".join(thing(gen,seq,n)))
