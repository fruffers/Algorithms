#insertion sort
#a[i] is end of sorted array, the element we will compare to all elements
#to left which is sorted array, keep swapping elements in the while loop
#and since a[i] is stored at the start it can be inserted when breaking
#out of the for loop, as an extra space was added onto the end of the list
#during while iteration when duplicates exist each time

arr = [3,5,1,2,8,6]
n = len(arr)

i = 1
j = 0
sort_end = 0

for i in range(1, n):
    #i is the element to sort against sorted array
    #so it's on the end of the sorted array
    #sort_end won't change
    sort_end = arr[i]
    j = i - 1
    while j >= 0 and sort_end < arr[j]:
        #sorts deck moving i into the right place
        #i is retained in the sort_end and is only
        #swapped out at the very end when breaking out
        #of the while loop
        arr[j+1] = arr[j]
        #step back through array
        j = j - 1
    arr[j+1] = sort_end
    