a = int(input("First number: "))
b = int(input("Second number: "))
aa = "{0:b}".format(a)
bb = "{0:b}".format(b)
print(aa)
print(bb)
print(bin(a ^ b).count('1'))

