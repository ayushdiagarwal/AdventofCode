import os
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

n = len(arr[0])

# ord("*") = 42

# Adjacents way

# NO*NO
# NUMBER
#   *
# NUMBER

# for any two numbers, the coloumn index should have something in common and a * in between them to fulfill the condition


nos = [46,48,49,50,51,52,53,54,55,56,57]
sum = 1
for i in range(len(arr)):
    s = arr[i]

    # for absolute adjacent 
    adj = re.finditer(r'\d+\*\d+',s)

    matches = re.finditer(r'\d+',s)
    

print(sum)




            


            
              
        
            



# check upper, lower, left, right