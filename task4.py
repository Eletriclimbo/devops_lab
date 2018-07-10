Age_array = list()
Sex_array = list()
print("Number of peoples: ")
l = int(input())
for j in range(int(l)):
    m = input("Age : ")
    p = input("Sex : ")
    Age_array.append(m)
    Sex_array.append(p)
max = int(0)
index = int(l)
sw = int(0)
for i in range(int(l)):
    if int(Sex_array[i]) == 1:
        if max == int(Age_array[i]):
            if index > i:
                print("ind")
                index = i
        if max < int(Age_array[i]):
            print ("MAX")
            max = int(Age_array[i])
            index = i
            sw = int(1)
else:
    print(-1)
if sw == 1:
    print(index)

