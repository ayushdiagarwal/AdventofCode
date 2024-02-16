file_obj = open("input.txt","r")
txt = file_obj.read()
arr = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        temp =[ int(i) for i in txt[count:i].split()]
        arr.append(temp)
        count = i+1

file_obj.close()

# Add values to the front than the back 

# recursion
def func(arr):
    global flag
    new = []
    if not flag:
        for j in range(len(arr)-1):
            new.append(arr[j+1]-arr[j])
        firsts.append(new[0])
        # Check that all elements in the list are zero rather than the sum you dumb cunt
        flag = True
        for i in range(len(new)):
            if new[i] != 0:
                flag = False
                break 
        # if sum(new) == 0: # fuck 
        #     flag = True
        func(new)

        
sum = 0
for i in range(len(arr)):
    count = 0
    flag = False
    firsts = [arr[i][0]]
    func(arr[i])

    n = len(firsts)
    for i in range(1,n+1):
        count = firsts[n-i]-count
    sum += count

print(sum)
