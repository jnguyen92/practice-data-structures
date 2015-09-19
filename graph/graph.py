__author__ = 'Nhuy'

class Graph_Node:

# implement weights?
    def __init__(self, id):
        self.id = id
        self.out_nodes = {}
        self.in_nodes = {}
        self.visited = False

        self.weights = []

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

class Graph:
    # list of nodes to be held in a dictionary/hastable ########
    def __init__(self):
        self.nodes = {}
        self.n_nodes = 0

    # retrieval methods ###########
    def __contains__(self, id):
        i = str(id)
        return i in self.nodes.keys()

    # returns node if it exists or else returns -1
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

    # change all visit status to 0
    def set_all_not_visited(self):
        for k in self.nodes.keys():
            self.nodes[k].set_visited(False)

    # search methods #########

    # if there are no returned values from dfs
    def is_connected(self):
        self.set_all_not_visited()
        a_key = self.nodes.keys()[0]
        not_connected = dfs(self, a_key, False)
        return len(not_connected) == 0

    # if to node is marked visited
    def is_path(self, from_id, to_id):
        self.set_all_not_visited()
        dfs(self, from_id, False)
        return self.get_node(to_id).is_visited()

    # reachable nodes are the ones that are not returned by dfs
    def nodes_from(self, from_id):
        self.set_all_not_visited()
        all_nodes = self.nodes.keys()
        not_connected = dfs(self, from_id, False)
        # set difference
        reachable = list( set(all_nodes).difference(not_connected) )
        reachable.remove( str(from_id) )
        return reachable


    # shortest path for no weights
    def shortest_path(self, from_id, to_id):
        self.set_all_not_visited()

        # initialize queue
        q = Queue()

        # find start node and add it to queue
        start_node = self.get_node(from_id)
        q.enqueue(start_node)
        path = 1

        while not q.is_empty():
            # retrieves first in line, signs guestbook, print info
            current = q.dequeue().get_data()
            current.set_visited(True)

            # adds outgoing nodes from current to queue
            outgoing = current.get_outgoing()
            for k in outgoing.keys():
                node = outgoing[k]
                if str(to_id) == node.get_id():
                    return path += 1
                if not node.is_visited():
                    q.enqueue( node )

            path += 1

        return -1


from queue.queue import *
from stack.stack import *

# depth-first search
def dfs(graph, start_id, find_not_connected = True):
    # initialize the stack
    s = Stack()

    # find the start node and add it to stack
    start_node = graph.get_node(start_id)
    s.push(start_node)

    # traverse graph
    while not s.is_empty():
        # retrieves top of stack, signs guestbook, and prints info
        current = s.pop().get_data()
        current.set_visited(True)
        print current.get_id()

        # adds outgoing nodes from current to stack
        outgoing = current.get_outgoing()
        for k in outgoing.keys():
            node = outgoing[k]
            if not node.is_visited():
                s.push( node )

    # if the graph is not circular from the start_node, then we need to find those unvisited nodes
    v = graph.all_visited()
    not_visit_node = [key for key, value in v.items() if value is False]
    if find_not_connected and len(not_visit_node) > 0:
        dfs(graph, not_visit_node[0], find_not_connected)
    else:
        return not_visit_node


# breadth-first search
def bfs(graph, start_id, find_not_connected = True):
    # initialize queue
    q = Queue()

    # find start node and add it to queue
    start_node = graph.get_node(start_id)
    q.enqueue(start_node)

    while not q.is_empty():
        # retrieves first in line, signs guestbook, print info
        current = q.dequeue().get_data()
        current.set_visited(True)
        print current.get_id()

        # adds outgoing nodes from current to queue
        outgoing = current.get_outgoing()
        for k in outgoing.keys():
            node = outgoing[k]
            if not node.is_visited():
                q.enqueue( node )

    # if the graph is not circular from the start_node, then we need to find those unvisited nodes
    v = graph.all_visited()
    not_visit_node = [key for key, value in v.items() if value is False]
    if find_not_connected and len(not_visit_node) > 0:
        dfs(graph, not_visit_node[0], find_not_connected)
    else:
        return not_visit_node

