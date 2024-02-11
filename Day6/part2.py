time= 44826981
dis = 202107611381458

# time = 71530
# dis = 940200

def distance(sec):
    return (sec*(time-sec))

count = 0
for j in range(time):
    if distance(j) > dis:
        count +=1 
print(count)