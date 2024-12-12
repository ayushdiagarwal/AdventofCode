import os
import re

file_obj = open("text.txt","r")
txt = file_obj.read()
arr = []
endline = 0
startline = 0
for i in range(len(txt)):
    if txt[i] == ":":
        startline = i+2
    if txt[i] == '\n':
        endline = i
        arr.append(txt[startline:endline])

file_obj.close()


# This is a very brute force method, its easy to find a much better way easily
dicts = {}

for i in range(len(arr)):
    dicts[i] = 1

for i in range(len(arr)):
    count = 0
    first, last = arr[i].split("|")
    wins = [int(j) for j in first.split()]
    gots = [int(j) for j in last.split()]

    for win in wins:
        for got in gots:
            if win == got:
                count +=1 


    # i 
    for _ in range(dicts[i]):
        for j in range(1,count+1):
            dicts[i+j] += 1 
    

sum = 0
for i in range(len(arr)):
    sum += dicts[i]
print(sum)

    
