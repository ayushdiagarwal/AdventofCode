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

sum = 0
for i in range(len(arr)):
    count = 0
    first, last = arr[i].split("|")
    wins = [int(i) for i in first.split()]
    gots = [int(i) for i in last.split()]

    for win in wins:
        for got in gots:
            if win == got:
                if count == 0:
                    count = 1
                else:
                    count = count*2 

    sum += count

print(sum)







