obj = open("1.txt", "r")

import re

text = obj.read()

flag = False
arr = []
count = 0
for i in range(len(text)):
    if text[i] == '\n':
        arr.append(text[count:i])
        count = i+1

# we have all the words in the array     

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["1","2","3","4","5","6","7","8","9"]

# function will return true/false
def is_substring(string, sub):
    index = 0
    for i in range(len(string)):
        if string[i] == sub[index]:
            index +=1
        else:
            index = 0
        if index == len(sub):
            return True
        
    return False


# for i in range(len(arr)):
#     init = []
#     for word in words:
#         if(is_substring(arr[i],word)):
#             init.append(word)

#     print(init)

# one approach might be to change the letter to numbers in the question

def brute():
    arr = [
    "eightwothree",
    "zoneight234"
    ]
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    init = []

    for i in range(len(arr)):
        j = 0
        while j < len(arr[i]):
            index = 0
            for word in words:
                print(f"arr:{arr[i][j]}    word:{word[index]}")
                if(arr[i][j] == word[index]):
                    index += 1
                    j+=1 
                    if(index == (len(word))):
                        init.append(word)
                        index = 0
                else:
                    index = 0
                
            j+=1

    print(init)

def replace():
    arr = [
    "eightwothree",
    "zoneight234"
    ]


    for i in range(len(arr)):
        for j in range(len(words)):
            arr[i] = arr[i].replace(words[8-j], digits[8-j])


    nos = []
    deci = [48,49,50,51,52,53,54,55,56,57]
    for i in range(len(arr)):
        count = 0
        first = "0"
        flag = False
        flag_2 = False
        last = "0"
        for j in range(len(arr[i])):
            if ord(arr[i][j]) in deci:
                count += 1
                if not flag:
                    first = arr[i][j]
                    flag = True
                last = arr[i][j]
        no = int(first+last)
        print(no)
        nos.append(no)

    print(sum(nos))








# This method fucking works!

def wordtodigit(word):
    if(len(word)>1):
        for i in range(len(words)):
            if words[i] == word:
                word = word.replace(words[i],digits[i])

    return word


# arr = [
# "eightwothree",
# "2zoneight234"
# ]
digits = ["1","2","3","4","5","6","7","8","9"]

pat = "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9|0"
rev_pat = pat[::-1]
init = []
sum = 0
for i in range(len(arr)):
    first = re.search(pat, arr[i]).group()
    last = re.search(rev_pat, arr[i][::-1]).group()[::-1]

    first = wordtodigit(first)
    last = wordtodigit(last)
    ans = int(first+last)
    sum += ans

print(sum)

obj.close()

