numbers = [12,6,3,7,13,8]

# def merge_sort(arr):
#     # Base case
#     if len(arr) <= 1:
#         return arr
#     # Divide
#     # spilt in half until arr length = 1
#     mid = round(len(arr)/2)
#     arr1 = arr[:mid]
#     arr2 = arr[mid:]
#     # Conquar
#     # compare the first value of two half array
#     return merge(merge_sort(arr1), merge_sort(arr2))


# def merge(arr1, arr2):
#     merged_arr = []
#     while len(arr1) and len(arr2):
#         if arr1[0] < arr2[0]:
#             merged_arr.append(arr1[0])
#             arr1.pop(0)
#         else:
#             merged_arr.append(arr2[0])
#             arr2.pop(0)
#     merged_arr += arr1
#     merged_arr += arr2
#     return merged_arr

# print(merge([2,5,6],[4,7,9,11,23]))

# print(merge_sort(numbers))

########################## White Board ##########################

nums = [3, 78, 42, 466, 324, 2, 12, 526, 34, 17, 24, 192, 348, 24, 1, 34, 12, 52, 53, 72, 143, 6, 535, 36]

# merge sort has two main section to it
# the first splits a larger list into two smaller lists
    # split each larger list into two halves specifically
        # we can do that by calculating the midpoint
# the second part will merge two smaller lists into a single larger list
    # I'll have to iterate through each item in the two lists and compare them all in a worst case scenario

# can I assume that the input will always be a list of integers?
# yes
# are negative numbers and zero acceptable?
# we'll go with possitive this time
# a single list for an input
# output will be the single list but sorted from least to greatest
# is it okay if I alter the original list? or do I need to return a completely new list?
# either is acceptable
# what happen if there is only one or zero items?
# if there are one or zero items, just return the list
# should I make this into a single fucntion for more practical use such as exporting it?
# up to me

# input is named lst
# one single fuction that contains the whole logic for performing merge sort
def merge_sort(lst):
    # spliting function definition
    def split(ls):
        # output? two lists that are equal halves of the ls input
        # I have ls and I want to solit it
        # seems like recursion would be more useful then iteration
        # I need a base case
        # otherwise perform the split
        # return merge()call in some fashion
        if len(ls) <= 1:
            return ls
        # // will ensure that we have an integer rather than float numbers 
        midpoint = len(ls) // 2
        left = ls[:midpoint] # does not include midpoint
        right = ls[midpoint:] # does include midpoint
        # merge() takes in two lists
        return merge(split(left), split(right))

    # merge function definition
    # merge is going to take two list as input
    # both input are sorted already
    def merge(ls1, ls2):
        # I need to compare each item in both lists in a worst case scenario
        # iteration
        output = []
        while len(ls1) and len(ls2):
            # inside of the while loop I'll be removing items from each list
            # so I was asking myself how do I compare an empty list with a non-empty list?
            # I can't - because there are no values to compare
            if ls1[0] < ls2[0]:
                output.append(ls1.pop(0))
            else:
                output.append(ls2.pop(0))
            # output the merged list that has been sorted
            return output + ls1 + ls2
        # Call split function
        return split(lst)

print(merge_sort(nums))