__author__ = 'Nhuy'

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
    if not all( v.values() ):
        not_visit_node = [key for key, value in v.items() if value is False]

    if find_not_connected:
        if not all( v.values() ):
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
    if not all( v.values() ):
        not_visit_node = [key for key, value in v.items() if value is False]

    if find_not_connected:
        if not all( v.values() ):
            bfs(graph, not_visit_node[0])
    else:
        return not_visit_node

