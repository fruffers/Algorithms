# use merge sort on sorted arrays

# make array 3 size of arr1+arr2
# traverse 1 and 2 simultaneously
# check if 1 or 2 element is greater
# add greater ele to 3 and ++ the arr it came from to next ele
# repeat
# if end of one array is reached then put all the rest of the elements in the back

def mergeArrays(arr1,arr2):
    arr3 = [0 for i in range(len(arr1) + len(arr2))]
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        # push smallest element and move up respective arrays
        if arr1[i] < arr2[j]:
            k+=1
            i+=1
            arr3[k] = arr1[i]
        else:
            k+=1
            j+=1
            arr3[j] = arr2[j]
    # store remaining elements
    while i < len(arr1):
        i+=1
        k+=1
        arr3[k] = arr1[i]
    while j < len(arr2):
        j+=1
        k+=1
        arr3[k] = arr2[j]

