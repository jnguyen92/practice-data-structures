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
        
    def set_prev(self, prevNode):
        self.prev = prevNode
    
    def get_prev(self):
        return self.prev
        
    def has_prev(self):
        return not (self.prev is None)
        
    def __eq__(self, other_node):
        return self.data == other_node.get_data()
