from collections import Counter
c = Counter(input('Insert: ')).most_common()
c = sorted(c, key=lambda t: (-t[1], t[0]))
for x in range(3):
    print(c[x][0], c[x][1])
