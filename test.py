__author__ = 'Nhuy'

class iter_test:

    def __init__(self):
        self.x = [43,6,1,2,3,7,3,2]

    def __iter__(self):
        return self

    def gen(self):
        yield self

### python iterator
def gen(self):
    t = self.head
    while not t is self.tail:
        yield t
        t = t.get_next()