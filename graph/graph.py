__author__ = 'Nhuy'

class Graph_Node:

    def __init__(self, data):
        self.data = data
        self.successors = []
        self.weights = []
        self.visited = False

    def add_successor(self, other_node, weight = 1):
        self.successors.append(other_node)
        self.weights.append(weight)

    def get_successors(self):
        return iter(self.successors)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_visited(self, visited):
        self.visited = visited

    def get_visited(self):
        return self.visited

class Graph:

     def __init__(self):
        self.nodes = []
        self.length = 0