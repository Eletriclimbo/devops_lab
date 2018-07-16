b = []
while 1 == 1:
    word = input().split()
    if word[0] == 'insert':
        b.insert(int(word[1]), int(word[2]))
    elif word[0] == 'print':
        print(b)
    elif word[0] == 'remove':
        b.remove(int(word[1]))
    elif word[0] == 'append':
        b.append(int(word[1]))
    elif word[0] == 'sort':
        b.sort()
    elif word[0] == 'pop':
        b.pop()
    elif word[0] == 'reverse':
        b.reverse()
