# Algorithm
This is my repo of learning some algorithms

## Book
https://zoracon.keybase.pub/Grokking_Algorithms.pdf

## Chapter 1 Binary Search

Binary search is a lot faster than simple search. Its input is a sorted list of elements, we need to find the middle index of the list by dividing the length of the list to half. If the element we are looking for is greater than the mid element, we do search on the left half of the list, otherwise, we do search on the right half of the list, until we find the element. If we don't find the element, it should return null. 

Run Time
- best case: mid is the one O(1)
- worse case start or the end O(logn)
- average case O(logn)???

## Chapter 2 Selection Sort

Selection sort algorithm sort a given list by finding it's smallest/largest item each time when it iterate through the list and insert it to a new list in order.

Run Time: O(n^2)

## Chapter 3 Recursion

- Recursion is when a function calls itself.
- Every recursive function has two cases: the base case
and the recursive case.
- A stack has two operations: push and pop.
- All function calls go onto the call stack.
- The call stack can get very large, which takes up a lot of memory

## Chapter 4 Quicksort

