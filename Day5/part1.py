import re
import os

#seed-to-soil
#soil-to-fertilizer
#fertilizer-to-water
#water-to-light
#light-to-temperature
#temperature-to-humidity
#humidity-to-location

#destination source range

# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location

file_obj = open("example.txt","r")
txt = file_obj.read()
arr = []
count = 0
for i in range(len(txt)):
    if txt[i] == '\n':
        arr.append(txt[count:i])
        count = i+1

file_obj.close()

# using a linked list
class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head 
        total = 0
        while cur.next!=None:
            total +=1
            cur = cur.next

        return total 
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next 
            elems.append(cur_node.data)
        print(elems)

# need to find the location of these
seeds = [int(i) for i in arr[0].replace("seeds: ", "").split()]

# seed to soil map:
# soil-to-fertilizer map:
# water-to-light map:
# light-to-temperature map:
# temperature-to-humidity map:
# humidity-to-location map:


# destination source range

seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_him = []
him_to_loc = []

count = 0
flag = 0
for i in range(len(arr)):
    if arr[i] == "seed-to-soil map:":
        count = i
    elif arr[i] == "soil-to-fertilizer map:":
        seed_to_soil.append(arr[count+1: i-1])
        count = i
    elif arr[i] == "fertilizer-to-water map:":
        soil_to_fert.append(arr[count+1:i-1])
        count = i
    elif arr[i] == "water-to-light map:":
        fert_to_water.append(arr[count+1: i-1])
        count = i
    elif arr[i] == "light-to-temperature map:":
        water_to_light.append(arr[count+1:i-1])
        count = i
    elif arr[i] == "temperature-to-humidity map:":
        light_to_temp.append(arr[count+1:i-1])
        count = i
    elif arr[i] == "humidity-to-location map:":
        temp_to_him.append(arr[count+1:i-1])
        count = i
    if i == len(arr):
        him_to_loc.append(arr[count+1: i-1])






    
# i should only have a linked list for the seeds I care about
# if they fall in the range, find their corresponding thing and add them a seperate linked list
        

# any numbers which aren't mapped, are mapped to location same as their no
        
# I think I got it
        
# i care about the seeds only

lists = []
index = 0 
seeds_flags = [0 for _ in range(len(seeds))]
        
for i in range(len(seed_to_soil)):
    # destination source range

    for j in range(2):
        dest, source, rang = [int(z) for z in seed_to_soil[i][j].split(" ")]
        for k in range(len(seeds)):
            if seeds[k] in range(source, source+rang): # can replace this with mathematical expresssion
                lists.append(linked_list())
                lists[index].append(seeds[k])
                lists[index].append(dest+(seeds[k]-source))
                index+=1
                seeds_flags[k] = 1
            
        for k in seeds_flags:
            if seeds_flags[k] == 0:
                lists[index].append(seeds[k])
                lists[index].append(seeds[k])
                index +=1 
        
        # seeds_flags = [0 for _ in range(len(seeds))]


for list in lists:
    list.display()



        



