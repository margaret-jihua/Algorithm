# Binary search is an algorithm; its input is a sorted list of elements. If an element you’re looking for is in that list, binary search returns the position where it’s located. Otherwise, binary search returns null.

# for a sorted list, find the middle index by dividing the length of the list to half. Check if the value of the middle index is the item we search for. If the value is greater than the item, we do search on the left half of the list, otherwise, we do search on the right half of the list.

# best case: mid is the one O(1)
# worse case start ot the end O(logn)
# average case O(logn)???

def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 11]

print(binary_search(my_list, 7))
print(binary_search(my_list, 2))