__author__ = 'Nhuy'

from queue.queue import *
from stack.stack import *

class Graph_Node:

    def __init__(self, id):
        self.id = id
        self.out_nodes = {}
        self.in_nodes = {}
        self.visited = False
        self.distance = 0

    def __repr__(self):
        s = "%s is connected to: " % self.id
        for k in self.out_nodes.keys():
            s += self.out_nodes[k].get_id() + " | "
        return s

    def add_outgoing(self, other_node):
        self.out_nodes[other_node.get_id()] = other_node

    def add_incoming(self, other_node):
        self.in_nodes[other_node.get_id()] = other_node

    def get_outgoing(self):
        return self.out_nodes

    def get_incoming(self):
        return self.in_nodes

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_visited(self, visited):
        if not isinstance(visited, bool):
            raise Exception("invalid value")
        else:
            self.visited = visited

    def is_visited(self):
        return self.visited

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        if not isinstance(distance, int):
            raise Exception("invalid value")
        self.distance = distance

class Graph:
    # list of nodes to be held in a dictionary/hastable with id as values ########
    def __init__(self):
        self.nodes = {}
        self.n_nodes = 0

    # retrieval methods ###########
    def __contains__(self, id):
        i = str(id)
        return i in self.nodes.keys()

    # returns node if it exists or raises an exception
    def get_node(self, id):
        i = str(id)
        try:
            return self.nodes[i]
        except KeyError:
            raise Exception("node does not exist")

    def get_all_nodes(self):
        return self.nodes

    # insertion methods #####
    def add_node(self, id):
        i = str(id)
        new_node = Graph_Node(i)
        if new_node.get_id() in self.nodes.keys():
            raise Exception("duplicated id")
        else:
            self.nodes[ new_node.get_id() ] = new_node
            self.n_nodes += 1

    # link generation methods - doubly linked ######
    def link_nodes(self, from_id, to_id):
        from_node = self.get_node(from_id)
        to_node = self.get_node(to_id)

        from_node.add_outgoing( to_node )
        to_node.add_incoming( from_node )

    # visit status #########

    # returns boolean vector of visit status
    def all_visited(self):
        visit_status = {key: value.is_visited() for key, value in self.nodes.items()}
        return visit_status

    # change all visit status to False
    def set_all_not_visited(self):
        for k in self.nodes.keys():
            self.nodes[k].set_visited(False)

    # change all distances to 0
    def clear_all_distances(self):
        for k in self.nodes.keys():
            self.nodes[k].set_distance(0)

    # search methods #########

    # if there are no returned values from dfs for every key
    def is_strong_connected(self):
        result = []
        for k in self.nodes.keys():
            self.set_all_not_visited()
            dfs(self, k)
            not_connected = [n.get_id() for k, n in self.nodes.items() if not n.is_visited()]
            result.append( len(not_connected) == 0 )
        return all(result)

    # if there are no returned values from 2-way dfs for every key
    def is_weak_connected(self):
        result = []
        for k in self.nodes.keys():
            self.set_all_not_visited()
            dfs_2way(self, k)
            not_connected = [n.get_id() for k, n in self.nodes.items() if not n.is_visited()]
            result.append( len(not_connected) == 0 )
        return all(result)

    # if to_node is marked visited
    def is_path(self, from_id, to_id):
        self.set_all_not_visited()
        dfs(self, from_id)
        return self.get_node(to_id).is_visited()

    # reachable nodes are the ones that are not returned by dfs
    def nodes_from(self, from_id):
        self.set_all_not_visited()
        all_nodes = self.nodes.keys()
        dfs(self, from_id)
        reachable = [n.get_id() for k, n in self.nodes.items() if n.is_visited()]
        reachable.remove( str(from_id) )
        return reachable

    # shortest path for no weights using bfs variant: shortest path or -1 if it doesn't exist
    def shortest_path(self, from_id, to_id):
        self.set_all_not_visited()
        self.clear_all_distances()

        # initialize queue
        q = Queue()

        # find start node and add it to queue, set distance to 0
        start_node = self.get_node(from_id)
        start_node.set_distance(0)
        q.enqueue(start_node)

        while not q.is_empty():
            # retrieves first in line, signs guestbook
            current = q.dequeue().get_data()
            current.set_visited(True)

            # obtains all outgoing nodes adds it to queue if not visited
            outgoing = current.get_outgoing()
            for k in outgoing.keys():
                node = outgoing[k]
                if not node.is_visited():
                    # set the distance from from_node, adds to queue
                    node.set_distance(1 + current.get_distance())
                    q.enqueue( node )
                    # if the node is the to_node, return the distance
                    if node.get_id() == str(to_id):
                        return node.get_distance()

        # if there is no path, return -1
        return -1

# graph traversals: returns an array of keys referring to nodes that have not been visited

# depth-first search
def dfs(graph, start_id, print_val = False):
    # initialize the stack
    s = Stack()

    # find the start node and add it to stack
    start_node = graph.get_node(start_id)
    start_node.set_visited(True)
    s.push(start_node)

    # traverse graph
    while not s.is_empty():
        # retrieves top of stack, signs guestbook, and prints info
        current = s.pop().get_data()
        if print_val:
            print current.get_id()

        # adds outgoing nodes from current to stack
        outgoing = current.get_outgoing()
        for k in outgoing.keys():
            node = outgoing[k]
            if not node.is_visited():
                node.set_visited(True)
                s.push( node )

# breadth-first search
def bfs(graph, start_id, print_val = False):
    # initialize queue
    q = Queue()

    # find start node and add it to queue
    start_node = graph.get_node(start_id)
    q.enqueue(start_node)

    while not q.is_empty():
        # retrieves first in line, signs guestbook, print info
        current = q.dequeue().get_data()
        current.set_visited(True)
        if print_val:
            print current.get_id()

        # adds outgoing nodes from current to queue
        outgoing = current.get_outgoing()
        for k in outgoing.keys():
            node = outgoing[k]
            if not node.is_visited():
                q.enqueue( node )


# depth first search using preceders and sucessors for weak connections
def dfs_2way(graph, start_id, print_val = False):
    # initialize the stack
    s = Stack()

    # find the start node and add it to stack
    start_node = graph.get_node(start_id)
    start_node.set_visited(True)
    s.push(start_node)

    # traverse graph
    while not s.is_empty():
        # retrieves top of stack, signs guestbook, and prints info
        current = s.pop().get_data()
        if print_val:
            print current.get_id()

        # adds incoming nodes from current to stack
        incoming = current.get_incoming()
        for k in incoming.keys():
            node = incoming[k]
            if not node.is_visited():
                node.set_visited(True)
                s.push( node )

        # adds outgoing nodes from current to stack
        outgoing = current.get_outgoing()
        for k in outgoing.keys():
            node = outgoing[k]
            if not node.is_visited():
                node.set_visited(True)
                s.push( node )
