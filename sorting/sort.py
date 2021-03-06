__author__ = 'Nhuy'


"""
Bubble sort: O(n^2) worst case
Parameters: array
Returns: sorted array (original array is sorted too)
"""
def bubble_sort(arr):

    # initialize outer loop params
    still_swap = True
    counter = len(arr)

    # enter outer loop: will stop when we have looped over all positions or
    # the previous loop did not do any swapping
    while counter > 0 and still_swap:
        still_swap = False

        # compare and swap
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
                still_swap = True

        # decrement outer loop counter
        counter -= 1

    # return sorted array
    return arr

"""
Selection sort: O(n^2) worse case
Parameters: array
Returns: sorted array (original array is sorted too)
"""
def selection_sort(arr):

    # loop through every position (except the last - since it will already be in order)
    for i in range(len(arr)-1):
        # set min index to the current position
        min_index = i

        # loop through and find the smallest value in other positions
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap current value with the min value
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    # return sorted array
    return arr

"""
Insertion sort: O(n^2) worst case, O(n) best case
Parameters: array
Returns: sorted array (original array is sorted too)
"""
def insertion_sort(arr):

    # loop through and insert value in corresponding position
    for i in range(1, len(arr)):
        # find value and location
        temp = arr[i]
        location = i

        # shift other values to create space for value
        while location > 0 and temp < arr[location - 1]:
            arr[location] = arr[location - 1]
            location -= 1

        # put in place the value
        arr[location] = temp

    # return sorted array
    return arr

"""
Merge sort: O(nlogn) all cases
Parameters: array
Returns: sorted array (original array is sorted too)
"""
def merge_sort(arr):

    # return an empty array if it is only 1 item
    if len(arr) == 1:
        return arr

    # split the array in half
    mid = len(arr)/2
    left = arr[:mid]
    right = arr[mid:]

    # merge sort the left and right half arrays
    left = merge_sort(left)
    right = merge_sort(right)

    # loop through the indices of the array
    left_index = right_index = arr_index = 0

    # recreate original array, adding from the sorted left and right in increasing order
    while right_index < len(right) and left_index < len(left):
        if right[right_index] < left[left_index]:
            arr[arr_index] = right[right_index]
            right_index += 1
        else:
            arr[arr_index] = left[left_index]
            left_index += 1
        arr_index += 1

    while right_index < len(right):
        arr[arr_index] = right[right_index]
        right_index += 1
        arr_index += 1

    while left_index < len(left):
        arr[arr_index] = left[left_index]
        left_index += 1
        arr_index += 1

    # return sorted array
    return arr


"""
Quick sort: O(nlogn) worst case using median of 3
Parameters: array
Returns: sorted array (original array is sorted too)
"""
def quick_sort(arr):

    aux_quick_sort(arr, 0, len(arr) - 1)

def aux_quick_sort(arr, low, high):

    # sets median of three (1st, middle, last) value to be the pivot, reorganizes by order
    arr, pivot = median_of_three(arr, low, high)

    # if array only has 3 values - median of three ensures that it is ordered
    if high - low <= 2:
        return arr

    # moves all values smaller than pivot before it, greater than pivot after it
    arr, mid_index = reposition(arr, pivot, low, high - 2)

    # quicksorts the halves
    aux_quick_sort(arr, 0, mid_index)
    aux_quick_sort(arr, mid_index, high)

    return arr

# median of 3: finds the median of 3 values and reorders those values where min_index = min value, max_index = max value
# max_index - 1 = mid_value
# Parameters: min_index & max_index to consider
# Returns: array in which min_index = min value, max_index = max value, max_index - 1 = mid_value
def median_of_three(arr, min_index, max_index):

    # obtain the values of the min, med, max
    three = [arr[min_index], arr[max_index], arr[(max_index - min_index) / 2 + min_index]]
    max_val = max( three )
    min_val = min( three )
    three.remove(max_val)
    three.remove(min_val)
    med_val = three[0]

    # put the min value on left, max value on right and med value in max - 1 position
    arr[min_index] = min_val
    arr[max_index ] = max_val
    arr[(max_index - min_index) / 2 + min_index] = arr[max_index - 1]
    arr[max_index - 1] = med_val

    # return array and pivot value
    return arr, med_val

# Reposition: moves all values greater than the pivot to the right of the pivot and all values less than pivot to the left of pivot
# Parameters: pivot (middle value), low (index of leftmost value), high (index of rightmost value)
def reposition(arr, pivot, low, high):

    # position of the pivot is just after the high
    pivot_index = high + 1

    # loop through indices and move all values less than pivot to left side, values greater than pivot to right side
    # stop when the pointers for high and low overlap - this is when everything is in place
    while low < high:
        # if the value at low index is greater than pivot, then swap it with the high value
        # decrement the high value to consider the next position
        if arr[low] > pivot:
            temp = arr[high]
            arr[high] = arr[low]
            arr[low] = temp
            high -= 1
        # otherwise increment the low value to consider the next position
        else:
            low += 1

    # when we exit the loop, low = high; this value can be greater than or equal to pivot
    # find out which it is and then put pivot in its right position
    # (all values < pivot to the left, all values > pivot to right of pivot)
    if arr[pivot_index] < arr[high]:
        arr[pivot_index] = arr[high]
        arr[high] = pivot
    else:
        arr[pivot_index] = arr[high + 1]
        arr[high + 1] = pivot

    # return the array and position of the pivot
    return arr, high + 1


"""
Heap sort: O(nlogn)
Parameters: array
Returns: sorted array (original array is sorted too)
"""
from priority_queue.heap import *

def heap_sort(arr):
    # initialize heap
    h = Priority_Queue()

    # add values to the heap which will organize it
    while len(arr) > 0:
        h.enqueue( arr.pop() )
    # remove values from heap (greatest first) and adds it to the beginning of the array
    while not h.is_empty():
        arr.insert(0, h.dequeue())

    # returns sorted array
    return arr
