def linearSearch(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i

    return -1



arr = [3,4,5]
val = 5
linearSearch(arr,val)