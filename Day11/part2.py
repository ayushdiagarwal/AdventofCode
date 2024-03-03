import copy
# make a replica of the line adjacent to it if it contains no galaxies

file_obj = open("input.txt","r")
txt = file_obj.read()
arr = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        arr.append(txt[count:i])
        count = i+1


file_obj.close()

def print_arr(arr):
    file_obj = open("output.txt","w")
    file_obj.write("\n".join(["".join(i) for i in arr]))


# convert string to list to make it mutable

arr = [list(arr[i]) for i in range(len(arr))]

# going rowise
emp_rows = []

for i in range(len(arr)):
    flag = True
    for j in range(len(arr[i])):
        if arr[i][j] == "#":
            flag = False
            break
    if flag:
        emp_rows.append(i)

# going colounwise
emp_cols = []

for i in range(len(arr)):
    flag = True
    for j in range(len(arr[i])):
        if arr[j][i] == "#":
            flag = False
            break

    if flag:
        emp_cols.append(i)

# print(emp_cols)
# print(emp_rows)

# now that we have the empty rows and columns, I need to add an array adjacent to it
# expand the universe

total_rows = len(arr)
total_cols = len(arr[0])

n = 1000000-1

# finding the indexes of the galaxies
# make a 2D matrix for storing the indexes
indexes = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "#":
            indexes.append([i,j])

# apparently, list comprehension references to the memory location instead of creating a list in new memory

# org_ind = [i for i in indexes] # shallow copy
org_ind = copy.deepcopy(indexes) # deep copy

for i in emp_rows:
    for j in range(len(indexes)):
        if indexes[j][0] > i:
            indexes[j][0] += n


# both rows and cols should be expanded simultaneously rather than one by one

# expanding the cols
for i in emp_cols:
    for j in range(len(indexes)):
        if org_ind[j][1] > i:
            indexes[j][1] += n

#expanded the universe

# now to find the distance between them

sum = 0
for i in range(len(indexes)):
    for j in range(i, len(indexes)):
        temp= abs(indexes[i][0]-indexes[j][0])+abs(indexes[i][1]-indexes[j][1])
        sum+=temp

print(sum)
