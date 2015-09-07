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

### size functions #####
    def is_empty(self):
        return self.length == 0
        
    def size(self):
        return self.length    
    
    def __len__(self):
        return self.length

### add data ###
    def push(self, data):
        new_node = Node(data)        
        
        if self.length == 0:
            self.top = new_node
            
        else:
            new_node.set_next(self.top)
            self.top = new_node
        
        self.length += 1
        
### remove data ####
    def pop(self):
        if self.is_empty():
            raise Exception("the stack is empty")
            
        else:
            rm_node = self.top
            self.top = rm_node.get_next()
        
        self.length -= 1
        
        return rm_node

### view data ####
    def peek(self):
        if self.is_empty():
            raise Exception("the stack is empty")
            
        else:
            return self.top
