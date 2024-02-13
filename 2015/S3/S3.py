import sys
rawinput = sys.stdin.readline
gates = int(rawinput())
planes = int(rawinput())
airport = [0 for _ in range(gates)]
result = 0
for i in range(planes):
    plane = int(rawinput()) - 1
    while plane >= 0 and airport[plane] > 0:
        jump = airport[plane]
        airport[plane] += 1
        plane -= jump
    if plane < 0:
        break
    else:
        airport[plane] += 1
        result += 1
print(result)
