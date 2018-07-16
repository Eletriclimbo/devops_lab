a = list(input('Insert a: '))
b = list(input('Insert b: '))
if a[0] != '-' and b[0] == '-':
    b.pop(0)
    a.sort()
    a.reverse()
    b.sort()
    b.reverse()
    b.insert(0, "-")
    b = int("".join(str(x) for x in b))
    a = int("".join(str(e) for e in a))
    print("a=", a, "b=", b)
    mdiff = a - b
    print('Difference: ', mdiff)

elif a[0] == '-' and b[0] != '-':
    aa = []
    j = 0
    for i in range(len(a)):
        if a[i] == '0':
            aa.append(0)
            j += 1
    a.sort()
    a = a[j + 1:]
    a[1:1] = aa
    a.insert(0, "-")
    bb = []
    j = 0
    for i in range(len(b)):
        if b[i] == '0':
            bb.append(0)
            j += 1
    b.sort()
    b = b[j:]
    b[1:1] = bb
    b = int("".join(str(x) for x in b))
    a = int("".join(str(e) for e in a))
    print("a=", a, "b=", b)
    mdiff = a - b
    print('Difference: ', mdiff)

elif a[0] == '-' and b[0] == '-':
    aa = []
    j = 0
    for i in range(len(a)):
        if a[i] == '0':
            aa.append(0)
            j += 1
    a.sort()
    a = a[j + 1:]
    a[1:1] = aa
    a.insert(0, "-")
    b.sort()
    b.reverse()
    if b[-1] == '-':
        b.pop()
        b.insert(0, "-")
    b = int("".join(str(x) for x in b))
    a = int("".join(str(e) for e in a))
    print("a=", a, "b=", b)
    mdiff = a - b
    print('Difference: ', mdiff)

else:
    aa = []
    j = 0
    a.sort()
    a.reverse()
    for i in range(len(b)):
        if b[i] == '0':
            aa.append(0)
            j += 1
    b.sort()
    b = b[j:]
    b[1:1] = aa
    b = int("".join(str(x) for x in b))
    a = int("".join(str(e) for e in a))
    print("a=", a, "b=", b)
    mdiff = a - b
    print('Difference: ', mdiff)
