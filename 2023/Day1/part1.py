obj = open("1.txt", "r")

text = obj.read()

flag = False
arr = []
count = 0
for i in range(len(text)):
    if text[i] == '\n':
        arr.append(text[count:i])
        count = i+1

# we have all the words in the array
        

nos = []
deci = [48,49,50,51,52,53,54,55,56,57]
for i in range(len(arr)):
    count = 0
    first = "0"
    flag = False
    flag_2 = False
    last = "0"
    for j in range(len(arr[i])):
        if ord(arr[i][j]) in deci:
            count += 1
            if not flag:
                first = arr[i][j]
                flag = True
            last = arr[i][j]
    no = int(first+last)
    nos.append(no)

obj.close()
print(sum(nos))

# for i in range(len(arr)):
#     print(f"{arr[i]}: {nos[i]}")

