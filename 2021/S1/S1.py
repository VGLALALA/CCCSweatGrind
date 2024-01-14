n = int(input())
heights = input().split()
heights = [int(i)for i in heights]
widths = input().split()
widths = [int(i)for i in widths]
prevhei = heights.pop(0)
sum = 0
for i,j in zip(heights,widths):
    sum += (prevhei + i)*j/2
    prevhei = i
print(sum)
