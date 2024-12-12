file_obj = open("example.txt","r")
txt = file_obj.read()
arr = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        temp =txt[count:i]
        arr.append(temp)
        count = i+1

file_obj.close()

arr = [list(arr[i].replace("7", "K")) for i in range(len(arr))]




# for example, consider the cursor is currently at arr[i], arr[j]
# rows -> i
# coloums -> j
# |  N-S        arr[i-1] and arr[i+1]
# -  W-E        arr[j-1] and arr[j+1]
# L  N-E        arr[i-1] and arr[j+1]
# J  N-W        arr[i-1] and arr[j-1]
# 7  S-W        arr[i+1] and arr[j-1]
# F  S-E        arr[i+1] and arr[j+1]
# .  Ground


# S Starting position
# Find the farthest distance 
# every pipe connects two neighbours, you need to figure out which two neighbours 



# Starting from S, go over its neighbours and allot a number to each of them
# Now, S can have four neighbours at max, go through all of them and allot a number in place of each alphabet
# now each of the four would be a continous loop, so just go over it until the current pos runs out of places to go to (except where it camr from)
# this seems similar to a path finding algo

sym = ["|", "-", "L", "J", "K", "F"]

# this function should return the next location
# also need to check where we came from 
def next(i,j,pipe, last):

    if pipe=="|":
        # return (i-1, j),(i+1,j)
    
        if last == (i-1, j):
            print("down")
            return (i+1,j)
        else:
            print("up")
            return (i-1, j)
    if pipe=="-":
        # return (i,j-1), (i,j+1)
        if last == (i,j-1):
            return (i,j+1)
        else:
            return (i,j-1)
    if pipe=="L":
        # return (i-1, j), (i, j+1)
        if last == (i-1, j):
            return (i, j+1)
        else:
            return (i-1, j)
    if pipe=="J":   
        # return (i-1, j), (i, j-1)
        if last == (i-1, j):
            return (i, j-1)
        else:

            return (i-1, j)
    if pipe=="K":
        # return (i+1,j), (i, j-1)
    
        if last == (i+1,j):
            return (i, j-1)
        else:
            return (i+1,j)
    if pipe=="F":
        # return (i+1,j), (i, j+1)
    
        if last == (i+1,j):
            return (i, j+1)
        else:
            return (i+1,j)
    
    # ground
    # if pipe==".":
    #     return 



def second():

    for i in range(len(arr)):
        for j in range(len(arr[i])):

            # first step is to find "S"

            if arr[i][j] == "S":

                # now we can possibly have four neighbors of S
                # we will use a for loop but for now lets only work with one neighbor

                neighbors = [(i,j-1), (i, j+1), (i-1,j), (i+1,j)]
                last_node = (i,j)

                n = neighbors[1]

                # we have to find the next node and move onto that
                
                cur_node = arr[n[0]][n[1]]
                if cur_node != ".":
                    flag = False
                    next_node = (n[0], n[1]) #inital value of next node
                    count = 1
                    lasts = [last_node]
                    while not flag:
                        last_node = (next_node[0], next_node[1])
                        lasts.append(last_node)

                        
                        # i'm sending the same current node and next node
                        
                        next_node = next(next_node[0], next_node[1], cur_node, lasts[-2])
                        print(f"next: {next_node} \nlast: {last_node} \ncur: {cur_node} \n \n")

                        cur_node = arr[next_node[0]][next_node[1]]

                        # go out of the loop and move to the next neighbor
                        if arr[next_node[0]][next_node[1]] not in sym:
                            flag = True
                            print("flag changed")
                            # change neighbor
                        else:
                            arr[next_node[0]][next_node[1]] = str(count)
                            count+=1

                        # cur_node = arr[next_node[0]][next_node[1]]
                        # why the fuck can't I move this line to the bottom of the fucking code
                        

                    

                        
                        
second()
for i in range(len(arr)):
    print("".join(arr[i]))

                
