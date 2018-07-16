Age_array = []
Sex_array = []
print("Number of peoples: ")
l = int(input())
for j in range(int(l)):
    m = input("Age : ")
    p = input("Sex : ")
    Age_array.append(m)
    Sex_array.append(p)
mym = int(0)
index = int(l)
sw = int(0)
for i in range(int(l)):
    if int(Sex_array[i]) == 1:
        if mym == int(Age_array[i]):
            if index > i:
                index = i
        if mym < int(Age_array[i]):
            mym = int(Age_array[i])
            index = i
            sw = int(1)
if sw == 1:
    print(index)
else:
    print(-1)
