f = open("2.txt", "r").read()
ranges = (f.split(","))
nums = [i.split("-") for i in ranges]

# cleaning the data
for i in range(len(nums)):
    for j in range(2):
        if nums[i][j][0] == "\n":
            nums[i][j] = nums[i][j][1::]
        nums[i][j] = int(nums[i][j])


gap = []
for i in range(len(nums)):
    gap.append(nums[i][1] - nums[i][0])

# diving the string into multiple parts and find if it's possible
# take n = len(no) -> len(no) -> 1 

nos = []
flag = False
for i in range(len(nums)):
    for k in range(nums[i][0], nums[i][1]+1):
        k = str(k)

        for a in reversed(range(1, len(k)+1)):
            if len(k) % a == 0:
                n = len(k) // a
                parts = [k[i*n:(i+1)*n] for i in range(a)]
                flag = all(x == parts[0] for x in parts) and len(parts) != 1

                if flag:
                    nos.append(int(k))
                    # print("FUCK " , k, parts)
                    break

    if flag:
        # print("FUCK " , k)
        flag = False
        continue
            
print(sum(nos))