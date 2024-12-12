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
# recursion

def func(arr):
    global flag
    new = []
    if not flag:
        for j in range(len(arr)-1):
            new.append(arr[j+1]-arr[j])
        lasts.append(new[-1])
        # Check that all elements in the list are zero rather than the sum you dumb cunt
        flag = True
        for i in range(len(new)):
            if new[i] != 0:
                flag = False
                break 
        # if sum(new) == 0: # fuck 
        #     flag = True
        func(new)

        
count = 0
for i in range(len(arr)):
    flag = False
    lasts = [arr[i][-1]]
    func(arr[i])
    t = sum(lasts)
    count+=t
    

print(count)
