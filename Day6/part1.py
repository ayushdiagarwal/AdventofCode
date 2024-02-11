# Time:      7  15   30
# Distance:  9  40  200


time= [44,82, 69,81]
dis = [202,1076,1138,1458]

n = 3

def distance(sec, t):
    return (sec*(t-sec))
sum = 1 
for i in range(len(time)):
    count = 0
    for j in range(time[i]):
        if distance(j, time[i]) > dis[i]:
            count +=1 
    sum *= count
    count = 0

print(sum)
