print("Input first:")
a = list(input())
print("Input second")
b = list(input())
<<<<<<< HEAD
=======
print(a)
print(b)
>>>>>>> 758033402cf71471d8bdd7e4f17214ead4f7bfaa
if b[0] == '-' and a[0] != '-':
    b.pop(0)
    a.sort()
    a.reverse()
    b.sort()
    b.reverse()
    b.insert(0, "-")
    a = int("".join(str(x) for x in a))
    b = int("".join(str(e) for e in b))
<<<<<<< HEAD
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)

elif a[0] == '-' and b[0] != '-':
=======
    max = int(a) - int(b)
    print(max)

elif a[0] == '-' and b[0] != '-':
    print("2")
>>>>>>> 758033402cf71471d8bdd7e4f17214ead4f7bfaa
    a.pop(0)
    b.sort()
    a.sort()
    a.insert(0, "-")
    b = int("".join(str(x) for x in b))
    a = int("".join(str(e) for e in a))
<<<<<<< HEAD
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)

=======
    max = int(a) - int(b)
    print(max)
>>>>>>> 758033402cf71471d8bdd7e4f17214ead4f7bfaa
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
<<<<<<< HEAD
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)

=======
    print("a=", a, "b=", b)
    max = int(a) - int(b)
    print(max)
>>>>>>> 758033402cf71471d8bdd7e4f17214ead4f7bfaa
else:
    a.sort()
    a.reverse()
    b.sort()
    a = int("".join(str(x) for x in a))
    b = int("".join(str(e) for e in b))
    print("a=", a, "b=", b)
<<<<<<< HEAD
    mdiff = int(a) - int(b)
    print('\n', "Max difference:", mdiff)
=======
    max = int(a) - int(b)
    print(max)
>>>>>>> 758033402cf71471d8bdd7e4f17214ead4f7bfaa
