__author__ = 'Nhuy'

def seq_search(arr, item):

    for i in range( len(arr) ):
        if arr[i] == item:
            return True

    return False

def bin_search(arr, item):
    # exit strategy: if there is only 1 value left, it is either the one we want or not
    if len(arr) == 1:
        if item == arr[0]:
            return True
        else:
            return False

    # recursively searches through halves of the array
    mid = len(arr)/2

    if item > arr[mid]:
        return bin_search(arr[mid:], item)
    elif item < arr[mid]:
        return bin_search(arr[:mid], item)
    else:
        return True

