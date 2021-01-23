# go through list as many times as there are elements
# for each element, and swap 2 adjacents each time

list = [5,1,8,3,6,2,4]

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            # swap
            list[j],list[j+1] = list[j+1],list[j]