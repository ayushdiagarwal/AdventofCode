import copy

file_obj = open("example.txt","r")
txt = file_obj.read()
arr = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        arr.append([int(i) for i in txt[count:i]])
        count = i+1

file_obj.close()

print(arr)

# Implement Djisktra's algorithm
