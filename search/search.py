__author__ = 'Nhuy'


"""
Sequential Search
Parameters: item
Returns: boolean
"""
def seq_search(arr, item):

    # loops through all items and compares it to the desired value
    for i in range( len(arr) ):
        if arr[i] == item:
            # if find it, return TRUE
            return True

    # after going through all values, and still in function - item doesn't exist
    return False

"""
Binary Search
Parameters: item
Returns: boolean
"""
def bin_search(arr, item):
    # exit strategy: if there is only 1 value left, it is either the one we want or not
    if len(arr) == 0:
        return False

    # recursively searches through halves of the array
    mid = len(arr)/2

    if item == arr[mid]:
        return True
    elif item > arr[mid]:
        return bin_search(arr[mid+1:], item)
    else:
        return bin_search(arr[:mid], item)