__author__ = 'Nhuy'

def seq_search(arr, item):

    for i in range( len(arr) ):
        if arr[i] == item:
            return True

    return False

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