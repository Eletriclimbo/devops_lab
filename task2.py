a = list(input())
b = list(input())
a.sort()
a.reverse()
if a[-1] == '-':
    a.pop()
    a.insert(0, "-")
b.sort()
a = int("".join(str(x) for x in a))
b = int("".join(str(e) for e in b))
print("first=", a, "second=", b)
print("max", a-b)