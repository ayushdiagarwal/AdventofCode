import re

file_obj = open("text.txt","r")
txt = file_obj.read()
arr = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        arr.append(txt[count:i])
        count = i+1

file_obj.close()

insts = arr[0].replace("L","0").replace("R", "1")

arr = arr[2:len(arr)]

for i in range(len(arr)):
    arr[i] = arr[i].replace("= (", "").replace(",","").replace(")", "")

roads = []

for i in range(len(arr)):
    roads.append(arr[i].split())

#lets go bruteforce
    
start = "AAA"
end = "ZZZ"

count = 0
thing = start
found = False
while not found:
    for a in range(len(insts)):
        for i in range(len(roads)):  
            if roads[i][0] == thing:
                thing = roads[i][int(insts[a])+1]
                # print(f"FOUND ONE: {thing}")
                count+=1
                if thing == end and a == len(insts)-1:
                    found = True

                break


print(count)
