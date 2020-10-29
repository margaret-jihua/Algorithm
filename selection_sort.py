# arrays: 
    # reading: O(1)
    # insertion: O(n)
    # deletion: O(n)
# linked list:
    # reding: O(n)
    # insertion: O(1)
    # deletion: O(1)

# find smallest/largest item by iterating through the arr and move it to a new arr in order

def findSmallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr [i] < smallest:
            smallest = arr[i]
            index = i
    return index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selection_sort([5, 3, 6, 2, 10]))