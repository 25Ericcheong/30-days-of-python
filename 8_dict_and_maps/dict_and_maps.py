n = int(input())
phonebook = dict()

for i in range(n):
    line = input()
    line = line.split()
    
    # if key doesn't exist, we return default value of line[1]
    # in this case, building dict for first time so it won't
    phonebook[line[0]] = phonebook.get(line[0],line[1])

while 1:
    try:
        q = input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:
        break
