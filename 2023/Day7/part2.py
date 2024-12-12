import os 
import re
import time

file_obj = open("text.txt","r")
txt = file_obj.read()
hands = []
bids = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        temp = (txt[count:i]).split()
        hands.append(temp[0])
        bids.append(int(temp[1]))
        count = i+1

file_obj.close()

# returns the counts
def ind(s):
    # AJJAQ
    # [2,2,1]
    temp = sorted(s) + ['Z']
    arr=[]
    count = 1
    for i in range(5):
        if temp[i+1] == temp[i]:
            count+=1 
        else:
            arr.append(count)
            count = 1

    return sorted(arr)[::-1]


# returns priority of the character # Joker is the weakest card now 
def prior(chr):
    order = ['A','K', 'Q', 'T', '9','8','7','6','5','4','3','2', 'J'][::-1]
    return order.index(chr)

def switch(i):
    bids[i+1],bids[i] = bids[i], bids[i+1]


# find the count of the largest number in the sequence other than J
def Jmakeit(s):
    s = sorted(s.replace("J", "")) + 'Z'
    max_count = 0 
    for i in range(len(s)):
        if s[i+1] == s[i]:
            count +=1 
        else:
            count = 0
        if count > max_count:
            max_count = count

    return max_count # might not need to return chr

# find the numbers of J and make it equal to the largest number in the ind 
def findJ(s):
    count_J = 0
    for i in range(len(s)):
        if s[i] == 'J':
            count_J +=1 
    return count_J

# in ind -> make ind[0] = ind[0] + findJ(s); ind.remove(findJ)
# returns the counts
def ind_J(s):
    # AJJAQ
    # [2,2,1]
    temp = sorted(s) + ['Z']
    arr=[]
    count = 1
    for i in range(5):
        if temp[i]!='J':
            if temp[i+1] == temp[i]:
                count+=1 
            else:
                arr.append(count)
                count = 1

    arr = sorted(arr)[::-1]
    count_J = findJ(s)
    
    # print(f"{arr}: {count_J}: {s}")
    
    #exception -> if s = "JJJJJ"
    if len(arr)!=0:
        if count_J!=0:
            arr[0] = arr[0] + count_J
            # arr.remove(count_J)
    else:
        arr = [5]

    return arr


def bubble(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            next = ind_J(arr[i+1]) # next element
            cur = ind_J(arr[i]) # current element
            if len(next) < len(cur):
                sorted = False
                arr[i+1], arr[i] = arr[i], arr[i+1]
                switch(i)
            # if length of both is same
            if len(next) == len(cur):
                # compares first element
                if next[0] > cur[0]:
                    sorted = False
                    arr[i+1], arr[i] = arr[i], arr[i+1]
                    switch(i)

                # J exchange won't be used in this one
                # checking for the priority order     
                elif next == cur:
                    for j in (range(len(arr[i]))):
                        if prior(arr[i+1][j])>prior(arr[i][j]):
                            sorted = False
                            arr[i+1], arr[i] = arr[i], arr[i+1]
                            switch(i)
                            break
                        elif prior(arr[i+1][j]) < prior(arr[i][j]):
                            break

                # compares second element
                elif next[0] == cur[0]:
                    if next[1] > cur[1]:
                        sorted = False
                        arr[i+1], arr[i] = arr[i], arr[i+1]
                        switch(i)

    return arr

start = time.time()
# print(bubble(hands))
bubble(hands)
end = time.time()

bids = bids[::-1]
sum = 0
for i in range(1,len(bids)+1):
    sum += i*bids[i-1]

print(sum)
print(f"time taken: {round(end-start)}")

        

