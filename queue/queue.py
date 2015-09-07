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

### stack data: size and top ####
    def __init__(self):
        self.length = 0
        self.front = None
        self.back = None

### representation #####
    def __repr__(self):
        return "queue of size %i" % self.length

### size functions #####
    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def __len__(self):
        return self.length

### add data ####
    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.back = new_node

        else:
            self.back.set_next( new_node )
            self.back = new_node

        self.length += 1

### remove data #####
    def dequeue(self):

        if self.is_empty():
            raise Exception("queue is empty")

        else:
            rm_node = self.front
            self.front = rm_node.get_next()

        self.length -= 1

        return rm_node