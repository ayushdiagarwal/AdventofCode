# make a replica of the line adjacent to it if it contains no galaxies

file_obj = open("example.txt","r")
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

# now that we have the empty rows and columns, I need to add an array adjacent to it
# expand the universe

total_rows = len(arr)
total_cols = len(arr[0])

# expanding the rows
count = 0
for i in emp_rows:
    arr.insert(i, ["." for j in range(total_rows)])
    count+=1

# expanding the cols

count = 0
for i in range(len(arr)):
    for j in emp_cols:
        arr[i].insert(j+count, ".")
        count+=1
    count = 0


#expanded the universe
print_arr(arr)

# now, re-number the # into numbers

def no_it(arr):
    count = 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "#":
                arr[i][j] = str(count)
                count+=1



indexes = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "#":
            indexes.append((i,j))

print(indexes)


# now to find the distance between them

sum = 0
for i in range(len(indexes)):
    for j in range(i, len(indexes)):
        temp= abs(indexes[i][0]-indexes[j][0])+abs(indexes[i][1]-indexes[j][1])
        sum+=temp

print(sum)


total_cols = len(arr)-1
total_rows = len(arr[0])-1





# no need to use BFS in this
# Use BFS to find the shortest path

# returns all the number of a given node
def neighbors(node):

    i = node[0]
    j = node[1]
    niggs = []

    # checking for boundary cases
    if i>0:
        niggs.append((i-1,j))
    if i<total_rows-1:
        niggs.append((i+1,j))

    if j>0:
        niggs.append((i,j-1))
    if j<total_cols-1:
        niggs.append((i,j+1))

    return niggs

marked = [[False for _ in range(total_cols)] for _ in range(total_rows)]

def dfs(node):
    cur = node
    marked[node[0]][node[1]] = True
    for neighbor in neighbors(node):
        if not marked[node[0]][node[1]]:
            dfs(node)
