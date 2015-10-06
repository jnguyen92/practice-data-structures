__author__ = 'Nhuy'


# root of heap = array[1]
# left child is array[2]
# right child is array[3]
# in array[k] left child is array[k*2], right child is array[k*2+1], parent is array[k/2]

class Priority_Queue:

    """
    Constructor: intialize the heap (array) and size
    """
    def __init__(self):
        self.heap = [None]
        self.size = 0

    """
    Return string representation
    """
    def __repr__(self):
        return "a heap"

    """
    Size functions:
    Returns: boolean (whether value is empty)
    """
    def is_empty(self):
        return self.size == 0

    """
    Enqueue: add data to queue
    Parameters: data to add
    Returns: NA
    """
    def enqueue(self, data):
        # intialize heap with 1st value
        if self.is_empty():
            self.heap.append(data)
            self.size += 1

        # adds data to heap
        else:
            self.heap.append(data)
            self.size += 1
            current_position = self.size

            # repositions the priority queue, so that bigger values are closer to the "top"
            # uses the parent/child relationships noted above to compare
            while current_position > 1 and data > self.heap[current_position/2]:
                self.heap[current_position] = self.heap[current_position/2]
                current_position /= 2

            self.heap[current_position] = data

    """
    Removal methods
    Returns: the edge object with the greatest weight

    Uses recursion to find the edge object with the greatest weight and rearrange the queue according to weight
    """
    def dequeue(self):
        # throw and exception if the queue is empty
        if self.is_empty():
            raise Exception("the queue is empty")

        # return the last object if queue is of size 1
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()

        # removes the edge object with the greatest weight and replaces it with the smallest child
        max = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1

        # recursively reorganizes the queue
        self.heap[1] = self.__aux_dequeue(1, self.heap[1])

        # return the max object
        return max


    # Recursive method to organize tree after removal of max object
    # Parameters: int for current location to be filled (index), int value in current position (value)
    # Returns: the object that should be placed in the position under consideration when function called
    def __aux_dequeue(self, index, value):
        # saves the position of the right and left child
        left_pos = index * 2
        right_pos = index * 2 + 1

        # if the current position has no children, it is in the smallest location and there is no smaller object
        if left_pos > self.size:
            return value

        # if the current position has 1 child, compare it to its child;
        # swap positions if it is smaller than its child
        # return its value if it is bigger than its child (don't swap)
        elif left_pos == self.size:
            if self.heap[left_pos] < value:
                return value
            else:
                temp = self.heap[left_pos]
                self.heap[left_pos] = value
                return temp

        # if the current position has 2 children, compare it to both children
        # swap positions with its biggest child if it is smaller than either child
        # return its value if it is bigger than both children (don't swap)
        else:
            if self.heap[left_pos] < value and self.heap[right_pos] < value:
                return value
            else:
                if self.heap[left_pos] > self.heap[right_pos]:
                    temp = self.heap[left_pos]
                    self.heap[left_pos] = self.__aux_dequeue(left_pos, value)
                else:
                    temp = self.heap[right_pos]
                    self.heap[right_pos] = self.__aux_dequeue(right_pos, value)
                return temp

