import os
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

n = len(arr[0]) # length of each line
# check at which index does the number start and at whichi it ends and then check for one before and after it 
# can find if numbers using ascii or regex

nos = [46,48,49,50,51,52,53,54,55,56,57]
sum = 0
for i in range(len(arr)):
    s = arr[i]

    matches = re.finditer(r'\d+',s)
    for match in matches:
        flag = False
        line = i
        start,end = match.span()

            
        #left # right
        y = start
        z = end-1 
        if start - 1 >= 0:
            if ord(arr[i][start-1]) not in nos:
                flag = True
            y = start-1 
        if end != n:
            if ord(arr[i][end]) not in nos:
                flag = True
            z= end+1

        for j in range(y, z):
            if i-1 >=0:
                if ord(arr[i-1][j]) not in nos:
                    flag = True
            
            if i+1 < len(arr):
                if ord(arr[i+1][j]) not in nos:
                    flag = True

        if flag == True: 
            sum += int(match.group())

print(sum)




            


            
              
        
            



# check upper, lower, left, right