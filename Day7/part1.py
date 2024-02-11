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


# returns priority of the character
def prior(chr):
    order = ['A','K', 'Q', 'J', 'T', '9','8','7','6','5','4','3','2'][::-1]
    return order.index(chr)

def switch(i):
    bids[i+1],bids[i] = bids[i], bids[i+1]


def bubble(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            next = ind(arr[i+1])
            cur = ind(arr[i])
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

                # compares second element
                if next[0] == cur[0]:
                    if next[1] > cur[1]:
                        sorted = False
                        arr[i+1], arr[i] = arr[i], arr[i+1]
                        switch(i)


                # checking for the priority order     
                if next == cur:
                    for j in (range(len(arr[i]))):
                        if prior(arr[i+1][j])>prior(arr[i][j]):
                            sorted = False
                            arr[i+1], arr[i] = arr[i], arr[i+1]
                            switch(i)
                            break
                        elif prior(arr[i+1][j]) < prior(arr[i][j]):
                            break

    return arr
start = time.time()
bubble(hands)
end = time.time()

bids = bids[::-1]
sum = 0
for i in range(1,len(bids)+1):
    sum += i*bids[i-1]

print(sum)
print(f"time taken: {round(end-start)}")


        

