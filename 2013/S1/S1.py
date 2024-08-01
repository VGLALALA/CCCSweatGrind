n = int(input())
from collections import Counter
def checker(year):
    counter = Counter(year)
    for item in counter:
        if counter[item] > 1:
            return False
    return True
while True:
    n += 1
    if checker(str(n)):
        break
print(n)

#5'32"