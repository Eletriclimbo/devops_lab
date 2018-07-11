from collections import Counter
c = Counter(input()).most_common(3)
b = sorted(c, key=lambda ff: (-ff[1], ff[0]))
for x in range(3):
    print(b[x][0], b[x][1])
