
#Splits list into sorted and unsorted. Pushes smallest 
#unsorted element to front and swaps when finding the next 
#smallest in the unsorted list.
#keep track of smallest index
#keep building on from the front where i was and loop through unsorted j
#until next smallest ele is found then this can replace i and i is popped back to
#what j's position was

aList = [4,5,6,2,3]

for i in range(len(aList)):
    # whole
    smallest_index = i
    for j in range(i+1,len(aList)):
        # unsorted
        if aList[j] < aList[smallest_index]:
            smallest_index = j
    # swap
    aList[smallest_index], aList[i] = aList[i], aList[smallest_index]

