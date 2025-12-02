file = open("1.txt", "r")

contents = file.read().split("\n")[:-1]
pos = 50

ans = 0
for i in contents:
    print(pos)
    no = i[1::]

    if i[0] == 'L':
        if pos == 0:
            pos = 100
        pos = pos - int(no)
    else:
        if pos == 100:
            pos = 0
        pos = pos + int(no)

    if pos >= 100 or pos <= 0:
        # ans += 1
        print(f"Ans = {ans} Pos: {pos}")
        n = abs(int(no)) // 100
        ans += n
        pos = pos % 100

    

print(pos)
print(ans)
