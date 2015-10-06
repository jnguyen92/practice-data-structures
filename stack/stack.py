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

class Stack:
    
### stack data: size and top ####
    def __init__(self):
        self.length = 0
        self.top = None

### representation #####
    def __repr__(self):
        return "stack of size %i" % self.length

    """
    Size functions:
    Returns: size if stack or boolean (whether stack is empty)
    """
    def is_empty(self):
        return self.length == 0
        
    def size(self):
        return self.length    
    
    def __len__(self):
        return self.length

    """
    Push:
    Parameters: data to add
    Returns: NA
    """
    def push(self, data):
        # makes a new node from the data
        new_node = Node(data)        

        # intialize if added item is the first
        if self.length == 0:
            self.top = new_node

        # adds to stack otherwise
        else:
            new_node.set_next(self.top)
            self.top = new_node

        # increments the size by 1
        self.length += 1
        
    """
    Pop:
    Parameters: NA
    Returns: top-most item, removes item from stack
    """
    def pop(self):
        # exception handling for empty stack
        if self.is_empty():
            raise Exception("the stack is empty")

        # remove the top-most item
        else:
            rm_node = self.top
            self.top = rm_node.get_next()

        # decrements stack size
        self.length -= 1

        # returns data
        return rm_node

    """
    Peek:
    Parameters: NA
    Returns: top-most item
    """
    def peek(self):
        # exception handling
        if self.is_empty():
            raise Exception("the stack is empty")

        # returns top-most item
        else:
            return self.top
