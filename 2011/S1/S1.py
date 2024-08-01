n = int(input())
t_ratio = 0
s_ratio = 0
from collections import Counter
for i in range(n):
    quote = input()
    quote = quote.lower()
    quote_count = Counter(quote)
    t_ratio += quote_count['t']
    s_ratio += quote_count['s']
    #print(quote_count,quote)
if t_ratio > s_ratio:
    print("English")
else:
    print("French")
