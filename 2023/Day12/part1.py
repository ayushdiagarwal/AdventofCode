# operational (.) or damaged (#) or unknown (?)
import copy

file_obj = open("example.txt","r")
txt = file_obj.read()
arr = []
dmgs = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        temp1, temp2 = (txt[count:i]).split()
        arr.append(temp1)
        dmgs.append([int(i) for i in temp2.split(",")])
        count = i+1

file_obj.close()

# find the number of continous damaged cells -> n
# also see if those damaged cells are followed by # -> m

# use simple pnc to find the number of ways # can be arranged in n




# to count the number of continous damaged cells
damages = []
for i in range(len(arr)):
    count = 0
    counts = []

    for j in range(len(arr[i])):
        if arr[i][j] == "?":
            count += 1
            if j == len(arr[i])-1:
                counts.append(count)
        else:
            if count != 0:
                counts.append(count)
                count = 0
    damages.append(counts)



# make a function to count the number of ? and # (continous) in a row

boths = []
for i in range(len(arr)):
    count = 0
    counts = []

    for j in range(len(arr[i])):

        if arr[i][j] == "?" or arr[i][j] == "#":
            if arr[i][j] == "#":
                if count>0:
                    count +=1
                    if j == len(arr[i])-1:
                        counts.append(count)
            elif arr[i][j] == "?":
                count += 1
                if j == len(arr[i])-1:
                    counts.append(count)

        else:
            if count != 0:
                counts.append(count)
                count = 0


    boths.append(counts)

print(arr)
print(damages)
print(boths)

# I can use bruteforce
