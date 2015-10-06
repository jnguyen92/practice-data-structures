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

    def __eq__(self, other_node):
        return self.data == other_node.get_data()

class Queue:

    """
    Constructor: intialize the front, back and size
    """
    def __init__(self):
        self.length = 0
        self.front = None
        self.back = None

    """
    Queue Representation: "queue of size __"
    """
    def __repr__(self):
        return "queue of size %i" % self.length

    """
    Size functions:
    Returns: either the size (int) or whether queue is empty (boolean)
    """
    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def __len__(self):
        return self.length

    """
    Enqueue: adds data to "end of the line"
    Parameters: data to add (any type)
    Returns: NA
    """
    def enqueue(self, data):
        # creates a new node for the data
        new_node = Node(data)

        # if the queue is empty, initialize it
        if self.is_empty():
            self.front = new_node
            self.back = new_node

        # otherwise adds data to the end of the queue
        else:
            self.back.set_next( new_node )
            self.back = new_node

        # increments the size
        self.length += 1

    """
    Dequeue: removes the data at the "front of the line"
    Parameters: NA
    Returns: data at the front of the line
    """
    def dequeue(self):

        # exception handling
        if self.is_empty():
            raise Exception("queue is empty")

        # removes from the front of the line
        else:
            rm_node = self.front
            self.front = rm_node.get_next()

        # decrements the size
        self.length -= 1

        # returns the removed obj
        return rm_node