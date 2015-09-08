__author__ = 'Nhuy'

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
    left_index = 0
    right_index = 0
    arr_index = 0

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

import numpy

def quick_sort(arr):

    aux_quick_sort(arr, 0, len(arr) - 1)

def aux_quick_sort(arr, low, high):

    arr, pivot = median_of_three(arr, low, high)

    if high - low <= 3:
        return arr

    arr, mid_index = reposition(arr, pivot, low, high - 2)

    aux_quick_sort(arr, 0, mid_index)
    aux_quick_sort(arr, mid_index, high)

    return arr

def median_of_three(arr, min_index, max_index):

    # obtain the values of the min, med, max
    three = [arr[min_index], arr[max_index], arr[(max_index - min_index) / 2 + min_index]]
    max_val = max( three )
    min_val = min( three )
    med_val = numpy.median( three )

    # put the min value on left, max value on right and med value in max - 1 position
    arr[min_index] = min_val
    arr[max_index ] = max_val
    arr[(max_index - min_index) / 2 + min_index] = arr[max_index - 1]
    arr[max_index - 1] = med_val

    # return array and pivot value
    return arr, med_val

def reposition(arr, pivot, low, high):

    pivot_index = high + 1

    # loop through indices and move all values less than pivot to left side,
    # values greater than pivot to right side
    while low < high:
        if arr[low] > pivot:
            temp = arr[high]
            arr[high] = arr[low]
            arr[low] = temp
            high -= 1
        else:
            low += 1

    # when we exit the loop, low = high; this value can be greater than or equal to pivot
    if arr[pivot_index] < arr[high]:
        arr[pivot_index] = arr[high]
        arr[high] = pivot
    else:
        arr[pivot_index] = arr[high + 1]
        arr[high + 1] = pivot

    # return
    return arr, high + 1
