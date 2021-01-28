# use on a sorted array
# divides list in half until val is found
# split in half each time use left edge and right edge and middle,
# evaluate if val < or > than middle and move it past left or right edge

list = [1,2,3,4,5,6]
val = 5 

def binarySearch(list,value):
    left_edge,right_edge = 0, len(list)-1
    while left_edge <= right_edge:
        middle = left_edge + (right_edge -1) // 2
        if list[middle] == value:
            return middle
        elif list[middle] < value:
            left_edge = middle + 1
        else:
            right_edge = middle - 1

    return -1
    
