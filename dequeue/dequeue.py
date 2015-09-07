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

### dequeue data: front, rear and size ####
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

### representation #####
    def __repr__(self):
        return "dequeue of length %i" % self.length

### size functions #####
    def __len__(self):
        return self.length

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

### add data ###
    def __add_first(self, new_node):
        self.front = new_node
        self.rear = new_node

    def add_front(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.__add_first(new_node)
        else:
            self.front.set_prev(new_node)
            new_node.set_next(self.front)
            self.front = new_node

        self.length += 1

    def add_rear(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.__add_first(new_node)
        else:
            self.rear.set_next(new_node)
            new_node.set_prev(self.rear)
            self.rear = new_node

        self.length += 1

### remove data ####
    def __rm_one(self):
        rm_node = self.front

        self.front = None
        self.rear = None

        return rm_node

    def remove_front(self):

        if self.is_empty():
            raise Exception("dequeue is empty")

        elif self.length == 1:
            rm_node = self.__rm_one()

        else:
            rm_node = self.front
            self.front = rm_node.get_next()

        self.length -= 1

        return rm_node

    def remove_rear(self):

        if self.is_empty():
            raise Exception("dequeue is empty")

        elif self.length == 1:
            rm_node = self.__rm_one()

        else:
            rm_node = self.rear
            self.rear = rm_node.get_prev()

        self.length -= 1

        return rm_node