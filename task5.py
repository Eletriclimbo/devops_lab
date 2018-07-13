from collections import Counter
c = Counter(input()).most_common(3)
for x in range(3):
    print(c[x][0], c[x][1])
