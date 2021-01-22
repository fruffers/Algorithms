# divide and conquer recursive algorithm
# split list in left and right, keep splitting until getting down to one
# join elements up on each side sorting them on the way up
# eventually the left and right side will be merged and sorted
# O(logn)

arr = [4,1,8,3,0,2]
low = 0
high = len(arr)
helper = []

def mergeSort(low,high):
    # when getting to 1 single element
    # this will evaluate to false and 
    # the call stack is popped to return
    # up and the merging will begin
    if low < high:
        mid = low + (high-low)/2
        mergeSort(low,mid)
        mergeSort(mid+1,high)
        merge(low,mid,high)

def merge(low,mid,high):
    for i in range(low,high):
        helper[i] = arr[i]

    curSmallest = low
    highLow = mid+1
    # copy smallest value
    # from either left or right 
    # to original array
    while low <= mid and highLow <= high:
        if helper[low] <= helper[highLow]:
            arr[curSmallest] = helper[low]
            low+=1
        else:
            arr[curSmallest] = helper[highLow]
            highLow+=1
        curSmallest+=1
    # copy rest of left side into array if there are still
    # elements in it
    while curSmallest < mid:
        arr[curSmallest] = helper[low]
        curSmallest+=1
        low+=1







