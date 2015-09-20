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

### list data: first item, last item, size ######
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

### iterations #####
    def __iter__(self):
        current = self.head
        while not current is None:
            yield current
            current = current.get_next()

### prints the values in the list #######
    def __repr__(self):
        return "doubly linked list of size %i" % self.length

    def print_list(self):
        it = iter(self)
        for i in range(self.length):
            print it.next()

### size functions ########
    def __len__(self):
        return self.length

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

### finds the node right before specified index #########
    def __one_before(self, index):
        index = index - 1
        it = iter(self)
        try:
            current = it.next()
            while index > 0:
                current = it.next()
                index -= 1
            return current
        except:
            return

### add functions ##########
    def insert(self, index, data):

        new_node = Node(data)

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

    def push(self, data):
        self.insert(0, data)

    def append(self, data):
        self.insert(self.length, data)

### remove functions ###########
    def rm(self, data):
        i = self.index(data)
        if i == -1:
            raise Exception("item does not exist")
        else:
            node = self.get(i)
            self.remove(node)

    # this remove only takes the node to be removed rather than a value
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

    def pop(self, index = None):

        if self.is_empty():
            raise Exception("the list is empty")

        if index >= self.length:
            raise IndexError("index is out of bounds")

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


### retrieve ########

    def get(self, index):
        if index > self.length:
            raise IndexError("index out of bounds")

        if index == 0:
            return self.head

        return self.__one_before(index).get_next()

    def index(self, data):
        it = iter(self)
        try:
            for i in range(self.length):
                current = it.next()
                if current.get_data() == data:
                    return i
        except:
            return -1

    def contains(self, data):
        return self.index(data) != -1

    def __contains__(self, data):
        return self.index(data) != -1