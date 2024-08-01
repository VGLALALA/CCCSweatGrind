max_weight = int(input())
n = int(input())
bridge = []
total_cars = 0
for i in range(n):
    weight = int(input())
    bridge.append(weight)
    if len(bridge) > 4:
        bridge.pop(0)
    if sum(bridge) > max_weight:
        break
    else:
        total_cars += 1

print(total_cars)
#7'47"