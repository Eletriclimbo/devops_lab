print("Input first:")
a = list(input())
print("Input second")
b = list(input())
if b[0] == '-' and a[0] != '-':
    b.pop(0)
    a.sort()
    a.reverse()
    b.sort()
    b.reverse()
    b.insert(0, "-")
    a = int("".join(str(x) for x in a))
    b = int("".join(str(e) for e in b))
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)

elif a[0] == '-' and b[0] != '-':
    a.pop(0)
    b.sort()
    a.sort()
    a.insert(0, "-")
    b = int("".join(str(x) for x in b))
    a = int("".join(str(e) for e in a))
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)

elif a[0] == '-' and b[0] == '-':
    a.sort()
    a.reverse()
    if a[-1] == '-':
        a.pop()
        a.insert(0, "-")
    b.sort()
    b.reverse()
    if b[-1] == '-':
        b.pop()
        b.insert(0, "-")
    a = int("".join(str(x) for x in a))
    b = int("".join(str(e) for e in b))
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)

else:
    a.sort()
    a.reverse()
    b.sort()
    a = int("".join(str(x) for x in a))
    b = int("".join(str(e) for e in b))
    print("a=", a, "b=", b)
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)
