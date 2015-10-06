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



class Linked_List:

    """
    Initialize the list: with head, tail and size
    """
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    """
    Iterator
    """
    def __iter__(self):
        current = self.head
        while not current is None:
            yield current
            current = current.get_next()

    """
    Representation & Printing of List
    """
    def __repr__(self):
        return "doubly linked list of size %i" % self.length

    def print_list(self):
        it = iter(self)
        for i in range(self.length):
            print it.next()

    """
    Size functions
    """
    def __len__(self):
        return self.length

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    """
    Method to find the node right before the specified index
    Parameters: the index (int)
    Returns: the node before the index
    """
    def __one_before(self, index):

        # generate the iterator
        index = index - 1
        it = iter(self)

        # iterate until find the node or until an error is thrown
        try:
            current = it.next()
            while index > 0:
                current = it.next()
                index -= 1
            return current
        except:
            return

    """
    Insert Methods
    Parameters: data to add & index (int) (for insert only)
    """
    # insert data at a specified location
    def insert(self, index, data):

        # generate a new node
        new_node = Node(data)

        # throw an exception
        if index > self.length:
            raise IndexError("index out of bounds")

        # initiate the list
        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        # insert at head
        elif index == 0:
            new_node.set_prev(None)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

        # insert at tail
        elif index == self.length:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node

        else:
            # get node before index
            b4_node = self.__one_before(index)
            # insert new node in between
            new_node.set_next( b4_node.get_next() )
            b4_node.get_next().set_prev(new_node)
            b4_node.set_next(new_node)
            new_node.set_prev(b4_node)

        # increment size of list
        self.length+= 1

    # insert data at the front of the list (index 0)
    def push(self, data):
        self.insert(0, data)

    # insert data at the end of the list
    def append(self, data):
        self.insert(self.length, data)


    """
    Removal Methods
    Parameters: data, node or index
    Returns:  removed node
    """
    # removes based on actual value
    # Returns: nothing - since you already know what the data is by specifying it
    def rm(self, data):
        # finds the index of the data
        i = self.index(data)

        # exception handling
        if i == -1:
            raise Exception("item does not exist")

        # removes the node
        else:
            node = self.get(i)
            self.remove(node)

    # removes based on the node
    # this remove only takes the node to be removed rather than a value - use rm for this
    def remove(self, rm_node):

        if self.is_empty():
            raise Exception("the list is empty")

        # throw error
        if rm_node is self.head is self.tail and self.length != 1:
            raise ValueError("object not in list")

        # remove only object
        elif rm_node is self.head is self.tail and self.length == 1:
            self.head = None
            self.tail = None

        # remove head
        elif rm_node is self.head:
            self.head = rm_node.get_next()
            self.head.set_prev(None)

        # remove tail
        elif rm_node is self.tail:
            self.tail = rm_node.get_prev()
            self.tail.set_next(None)

        # other options
        else:
            rm_node.get_prev().set_next(rm_node.get_next())
            rm_node.get_next().set_prev(rm_node.get_prev())

        # decrement list size
        self.length -= 1

        # return
        return rm_node

    # remove based on index
    def pop(self, index = None):

        # exception handling
        if self.is_empty():
            raise Exception("the list is empty")

        if index >= self.length:
            raise IndexError("index is out of bounds")

        # if no index specified, will pop the last value
        if index is None:
            index = self.length - 1

        # remove head
        if index == 0:
            return self.remove(self.head)

        # remove tail
        elif index == self.length - 1:
            return self.remove(self.tail)

        # remove other
        elif not (index is None):
            rm_node = self.get(index)
            return self.remove(rm_node)

    """
    Retrieval Methods
    Parameters: index to obtain data, data to look for
    Returns: removed data, if applicable; boolean for contain methods
    """
    # function to obtain data at a certain index
    def get(self, index):
        # exception handling
        if index > self.length:
            raise IndexError("index out of bounds")

        # returns first value
        if index == 0:
            return self.head

        # finds the node before specified index and returns the next node
        return self.__one_before(index).get_next()

    # finds the index of a data value
    def index(self, data):
        # initiate iterator
        it = iter(self)

        # loops through and finds data until it finds it and returns index, otherwise quits and returns -1
        try:
            for i in range(self.length):
                current = it.next()
                if current.get_data() == data:
                    return i
        except:
            return -1

    # finds whether data is in list at all
    def contains(self, data):
        return self.index(data) != -1

    def __contains__(self, data):
        return self.index(data) != -1