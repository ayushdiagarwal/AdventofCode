import re

max_red = 12
max_green = 13
max_blue = 14


file_obj = open("text.txt","r")
txt = file_obj.read()
arr = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        arr.append(txt[count:i])
        count = i+1

file_obj.close()

# file -> arr

# now use to re to find all the green blue and red balls in each example
sum = 0
for i in range(len(arr)):


    flag = True


    all_reds = re.findall(r'\d+ red', arr[i])
    reds = [int(match.replace(" red", "")) for match in all_reds]

    for red in reds:
        if red > max_red:
            flag = False


    all_blues = re.findall(r'\d+ blue', arr[i])
    blues = [int(match.replace(" blue", "")) for match in all_blues]

    for blue in blues:
        if blue > max_blue:
            flag = False

    all_greens = re.findall(r'\d+ green', arr[i])
    greens = [int(match.replace(" green", "")) for match in all_greens]

    for green in greens:
        if green > max_green:
            flag = False

    if flag == True:
        sum += i+1

print(sum)
            
        

            
        