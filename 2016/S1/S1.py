
from collections import Counter
a = input()
b = input()
DicA = Counter(a)
DicB = Counter(b)
val = 0
for key in DicA:
    if key not in DicB:
        val += DicA[key]
    elif DicA[key] > DicB[key]:
        val += DicA[key] - DicB[key]
if val == 0:
    print("A")
elif '*' not in DicB and val > 0:
    print("N")
elif DicB['*'] >= val:
    print("A")
else:
    print("N")