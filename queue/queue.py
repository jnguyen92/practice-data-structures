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

    def has_next(self):
        return not (self.next is None)

    def __eq__(self, other_node):
        return self.data == other_node.get_data()

class Queue:

    def __init__(self):
        self.length = 0
        self.front = None
        self.back = None

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def __len__(self):
        return self.length

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.back = new_node

        else:
            self.back.set_next( new_node )
            self.back = new_node

        self.length += 1

    def dequeue(self):

        if self.is_empty():
            raise Exception("queue is emtpy")

        else:
            rm_node = self.front
            self.front = rm_node.get_next()

        self.length -= 1

        return rm_node
