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
    """
    Constructor: initialize dictionary of nodes and number of nodes
    """
    def __init__(self):
        self.nodes = {}
        self.n_nodes = 0

    """
    Retrieval methods:
    Parameters: id
    Returns: node(s) requested
    """
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

    # returns all nodes
    def get_all_nodes(self):
        return self.nodes

    """
    Insertion Methods:
    Parameters: id
    Returns: NA
    """
    def add_node(self, id):
        # converts id to a string (if not already)
        i = str(id)

        # generate a new graph node from id
        new_node = Graph_Node(i)

        # exception handling for duplicated nodes
        if new_node.get_id() in self.nodes.keys():
            raise Exception("duplicated id")

        # adds node to dictionary by id/key
        else:
            self.nodes[ new_node.get_id() ] = new_node
            self.n_nodes += 1


    """
    Link generation methods: doubly linked
    Parameters: id of 2 graph nodes
    """
    def link_nodes(self, from_id, to_id):
        # obtains nodes
        from_node = self.get_node(from_id)
        to_node = self.get_node(to_id)

        # adds links for two nodes
        from_node.add_outgoing( to_node )
        to_node.add_incoming( from_node )

    """
    Visit Status Methods:
    mostly used in graph traversal methods
    """

    # Returns: boolean vector of visit status for each graph node
    def all_visited(self):
        visit_status = {key: value.is_visited() for key, value in self.nodes.items()}
        return visit_status

    # set all visit status to False, used before traversals
    def set_all_not_visited(self):
        for k in self.nodes.keys():
            self.nodes[k].set_visited(False)

    # change all distances to 0, used before traversals
    def clear_all_distances(self):
        for k in self.nodes.keys():
            self.nodes[k].set_distance(0)

    """
    Search methods
    """
    # test for strong connectivity
    # Returns: boolean - is it strongly connected?
    def is_strong_connected(self):
        result = []

        # loops through all nodes and runs dfs, finds the nodes that were not visited
        for k in self.nodes.keys():
            self.set_all_not_visited()
            dfs(self, k)
            not_connected = [n.get_id() for k, n in self.nodes.items() if not n.is_visited()]
            result.append( len(not_connected) == 0 )

        # if graph is strongly connected - all nodes should be visited with each iteration of loop
        return all(result)

    # tests for weak connectivity
    # Returns: boolean
    def is_weak_connected(self):
        result = []

        # loops through all nodes and runs 2-way dfs, finds the nodes that were not visited
        for k in self.nodes.keys():
            self.set_all_not_visited()
            dfs_2way(self, k)
            not_connected = [n.get_id() for k, n in self.nodes.items() if not n.is_visited()]
            result.append( len(not_connected) == 0 )

        # if the graph is weakly connected - all nodes should be visited with each iteration of loop
        return all(result)

    # finds a path from 1 node to another
    # Parameters: 2 strings indicating the start and end
    # Returns: boolean
    def is_path(self, from_id, to_id):
        # runs a dfs from the start position
        self.set_all_not_visited()
        dfs(self, from_id)

        # if there is a path, the to node should be marked visited
        return self.get_node(to_id).is_visited()

    # reachable nodes are the ones that are not returned by dfs
    # Parameters: string indicating start position
    # Returns: array of reachable nodes by id
    def nodes_from(self, from_id):
        # runs dfs from the start position
        self.set_all_not_visited()
        dfs(self, from_id)

        # loops through nodes and finds the ones that are visited
        reachable = [n.get_id() for k, n in self.nodes.items() if n.is_visited()]

        # removes the from id (obviously set to visited since we started from there)
        reachable.remove( str(from_id) )

        # returns the list of reachable nodes
        return reachable

    # shortest path for no weights using bfs variant: shortest path or -1 if it doesn't exist
    # Parameters: 2 strings, the start and end node by id
    # Returns: the length of the shortest path
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
                    # set the distance as 1 +  from_node distance, adds to queue
                    node.set_distance(1 + current.get_distance())
                    q.enqueue( node )
                    # if the node is the to_node, return the distance
                    if node.get_id() == str(to_id):
                        return node.get_distance()

        # if there is no path, return -1
        return -1


"""
Graph Traversals
"""

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
