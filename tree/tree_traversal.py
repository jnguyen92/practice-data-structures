__author__ = 'Nhuy'

# Tree Traversals: print node

# in order: visit left subtree, visit node, visit right subtree
def in_order(tree):
    aux_in_order(tree.root)

def aux_in_order(node):
    if not node.get_left() is None:
        aux_in_order( node.get_left() )

    print node

    if not node.get_right() is None:
        aux_in_order( node.get_right() )


# pre order: visit node, visit left subtree, visit right subtree
def pre_order(tree):
    aux_pre_order(tree.root)

def aux_pre_order(node):

    print node

    if not node.get_left() is None:
        aux_pre_order(node.get_left())

    if not node.get_right() is None:
        aux_pre_order(node.get_right())


# post order: visit left subtree, visit right subtree, visit node
def post_order(tree):
    aux_post_order(tree.root)

def aux_post_order(node):

    if not node.get_left() is None:
        aux_post_order(node.get_left())

    if not node.get_right() is None:
        aux_post_order(node.get_right())

    print node


# level order: visit root, visit nodes 1 level away, 2 levels, etc
from queue.queue import * # queue uses a node to add, so when we dequeue, must use get_data() to access to tree node (this can easily be changed later)

def level_order(tree):
    q = Queue()
    q.enqueue(tree.root)
    while not q.is_empty():
        current = q.dequeue()
        print current
        if not current.get_data().get_left() is None:
            q.enqueue(current.get_data().get_left())
        if not current.get_data().get_right() is None:
            q.enqueue(current.get_data().get_right())