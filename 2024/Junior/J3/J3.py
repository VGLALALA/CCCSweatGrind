
n = int(input())
scores = [int(input()) for _ in range(n)]
sc = {}
for score in scores:
    if score in sc:
        sc[score] += 1
    else:
        sc[score] = 1
sorted_scores = sorted(sc.keys(), reverse=True)
bronze_score = sorted_scores[2]
print(bronze_score, sc[bronze_score])

