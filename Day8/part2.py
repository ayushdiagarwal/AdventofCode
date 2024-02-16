import re

file_obj = open("example.txt","r")
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

# start with all the nodes ending with "A"
# start simultaneously from all the nodes ending with "A" until they all simultaneously end with "Z"

count = 0
found = False
start = []

for i in range(len(roads)):
    if roads[i][0][2] == "A":
        start.append(roads[i][0])

# the end conditon is that all elements of the array are 'Z'
def finish(arr):
    n = len(arr)

    flag = True
    for i in range(n-1):
        if arr[i] != 'Z':
            flag = False
            break

    return flag 

# while not found:
for i in range(1):
    ends = []
    for j in range(len(start)):
        # bloody hell a common kamekaze
        for i in range(len(insts)):
            thing = start[j]
            # find the next element for each 
            for a in range(len(roads)):
                if roads[a][0] == thing:
                    count+=1 
                    thing = roads[a][int(insts[i])+1]
                    if i == len(insts)-1:
                        ends.append(thing[2])
                        break
    
        if finish(ends):
            found = True

print(ends)
print(count)
            
            






