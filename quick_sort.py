numbers = [12,6,3,7,13,8]

def quick_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    # set the pivot point to the last item in the array
    # initialize a left and right partition as empty arrays
    pivot = arr.pop()
    left = []
    right = []

    # iterate over the arr and move an item into either the left or right partitions based on comparing the value of each item with the value of the pivot    
    for i in range(0, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # recursively call quick_sort() on each partition
    # concatente left and right array with pivot in the middle
    return quick_sort(left) + [pivot] + quick_sort(right)
            
print(quick_sort(numbers))

# make a tree of recursions, left branch will be valued less then pivot
# pivot can be any item in the array
# right branch will be any value greater than the pivot