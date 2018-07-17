def main(l):
    age_array = []
    sex_array = []
    for j in range(l):
        m = input("Age : ")
        p = input("Sex : ")
        age_array.append(m)
        sex_array.append(p)
    sw, index = is_older_man(sex_array, age_array, l)
    if sw == 1:
        print(index)
    else:
        print(-1)


def is_older_man(sex_array, age_array, l):
    mym = int(0)
    index = int(l)
    sw = int(0)
    for i in range(index):
        if int(sex_array[i]) == 1:
            if mym == int(age_array[i]):
                if index > i:
                    index = i
            if mym < int(age_array[i]):
                mym = int(age_array[i])
                index = i
                sw = int(1)
    return sw, index


if __name__ == "__main__":
    print("Number of peoples: ")
    l = int(input())
    main(l)
