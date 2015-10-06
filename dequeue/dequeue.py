__author__ = 'Nhuy'

class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.data)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, nextNode):
        self.next = nextNode

    def get_next(self):
        return self.next

    def set_prev(self, prevNode):
        self.prev = prevNode

    def get_prev(self):
        return self.prev

    def __eq__(self, other_node):
        return self.data == other_node.get_data()

class Dequeue:

    """
    Constructor: initialize front, back, length
    """
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    """
    Representation: prints data type and length
    Returns: string
    """
    def __repr__(self):
        return "dequeue of length %i" % self.length

    """
    Size functions
    Returns: size (int) or whether structure is empty (boolean)
    """
    def __len__(self):
        return self.length

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0


    """
    Add data to list
    Parameters: data (any type)
    Returns: NA
    """
    # initialize the first node
    def __add_first(self, new_node):
        self.front = new_node
        self.rear = new_node

    # add to the front of the dequeue
    def add_front(self, data):
        # make a new node
        new_node = Node(data)

        # intialize of structure is empty
        if self.length == 0:
            self.__add_first(new_node)
        # otherwise add to front of queue
        else:
            self.front.set_prev(new_node)
            new_node.set_next(self.front)
            self.front = new_node

        # increment size
        self.length += 1

    def add_rear(self, data):
        # make new node
        new_node = Node(data)

        # initialize if structure is empty
        if self.length == 0:
            self.__add_first(new_node)

        # otherwise add to rear of the queue
        else:
            self.rear.set_next(new_node)
            new_node.set_prev(self.rear)
            self.rear = new_node

        # increment size
        self.length += 1

    """
    Remove data from the list
    Parameters: NA
    Returns: data (that was removed)
    """
    # Remove the last node
    def __rm_one(self):
        rm_node = self.front

        self.front = None
        self.rear = None

        return rm_node

    def remove_front(self):

        # exception handling for emtpy dequeue
        if self.is_empty():
            raise Exception("dequeue is empty")

        # remove last value
        elif self.length == 1:
            rm_node = self.__rm_one()

        # remove from front
        else:
            rm_node = self.front
            self.front = rm_node.get_next()

        # decrement size
        self.length -= 1

        # return value
        return rm_node

    def remove_rear(self):

        # exception handling for empty dequeue
        if self.is_empty():
            raise Exception("dequeue is empty")

        # remove last value
        elif self.length == 1:
            rm_node = self.__rm_one()

        # remove from rear
        else:
            rm_node = self.rear
            self.rear = rm_node.get_prev()

        # decrement size
        self.length -= 1

        # return value
        return rm_node