__author__ = 'Nhuy'


# root of heap = array[1]
# left child is array[2]
# right child is array[3]
# in array[k] left child is array[k*2], right child is array[k*2+1], parent is array[k/2]

class Priority_Queue:
    def __init__(self):
        self.heap = [None]
        self.size = 0

    def __repr__(self):
        return "a heap"

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        if self.is_empty():
            self.heap.append(data)
            self.size += 1

        else:
            self.heap.append(data)
            self.size += 1
            current_position = self.size

            while current_position > 1 and data > self.heap[current_position/2]:
                self.heap[current_position] = self.heap[current_position/2]
                current_position /= 2

            self.heap[current_position] = data

    def dequeue(self):

        if self.is_empty():
            raise Exception("the queue is empty")

        if self.size == 1:
            self.size -= 1
            return self.heap.pop()

        max = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1

        self.heap[1] = self.__aux_dequeue(1, self.heap[1])
        return max


    def __aux_dequeue(self, index, value):
        left_pos = index * 2
        right_pos = index * 2 + 1

        # has no children
        if left_pos > self.size:
            return value

        # if it only has 1 child
        elif left_pos == self.size:
            if self.heap[left_pos] < value:
                return value
            else:
                temp = self.heap[left_pos]
                self.heap[left_pos] = value
                return temp

        # if it has 2 children
        else:
            # none of its children are smaller
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

