__author__ = 'Nhuy'


class Tree_Node:
    # tree node: key, data, left child, right child
    def __init__(self, key = None, data = None, left_child = None, right_child = None):
        self.key = key
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    # representation #######
    def __repr__(self):
        return "%s: %s" % ( str(self.key), str(self.data) )

    # related to key of node #######
    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    # related to data of node #########
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    # related to left & right children of node ########
    def set_left(self, child_node):
        self.left_child = child_node

    def set_right(self, child_node):
        self.right_child = child_node

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def has_left(self):
        return not self.left_child is None

    def has_right(self):
        return not self.right_child is None

    # comparison methods ##########
    def __eq__(self, other_node):
        return self.key == other_node.get_key()

    def __ge__(self, other_node):
        return self.key > other_node.get_key()

    def __le__(self, other_node):
        return self.key < other_node.get_key()


class BST:

    """
    Constructor: initalize the tree with the root node
    """
    def __init__(self):
        self.root = None

    """
    Representation:
    prints the tree
    """
    def __repr__(self):
        if self.root is None:
            return "an empty binary search tree"
        else:
            return "a binary search tree"

    # print methods (using in order traversal) ######
    def print_tree(self):
        if self.root is None:
            print "an empty binary search tree"

        self.__internal_print(self.root)

    def __internal_print(self, node):

        if not node.get_left() is None:
            self.__internal_print( node.get_left() )

        print node

        if not node.get_right() is None:
            self.__internal_print( node.get_right() )

    """
    Insertion methods: recursively inserts data into tree by the key; keys should be unique
    Parameters: key (int) and data (any type)
    Returns: NA
    """
    def insert(self, key, data):
        self.root = self.__internal_insert(self.root, key, data)

    # Parameters: node (node object to add to), key (int), data (any type)
    # Returns: node with the new data added
    def __internal_insert(self, node, key, data):
        # base cases: tree has no children or duplicate key value
        if node is None:
            return Tree_Node(key, data)

        elif key == node.get_key():
            raise Exception("duplicated key")

        # recursive cases: finds the correct parent node to connect to
        elif key < node.get_key():
            node.set_left( self.__internal_insert( node.get_left(), key, data) )
            return node

        else:
            node.set_right( self.__internal_insert( node.get_right(), key, data))
            return node

    """
    Removal methods: recursively deletes data from tree by key
    Parameters: key (int)
    Returns: NA
    """
    def remove(self, key):
        self.root = self.__internal_remove(self.root, key)

    # Parameters: node (node object to adjust after removal), key (int)
    # Returns: node corresponding to the key or None if the key doesn't exist
    def __internal_remove(self, node, key):
        # base case: node doesn't exist, do nothing
        if node is None:
            return None

        # node does exist, returns it and replace it if necessary
        elif key == node.get_key():
            # if it has no children, do nothing
            if node.get_left() is None and node.get_right() is None:
                return None

            # if it has 2 children, replace it with the smallest value in its right subtree
            # and remove the smallest value from its original location
            elif not node.get_left() is None and not node.get_right() is None:
                small = self.__internal_smallest( node.get_right() )
                removed_value = self.__internal_remove( node.get_right(), small.get_key() )
                small.set_left( node.get_left() )
                small.set_right( removed_value )
                return small

            # if it has 1 child, replace it with is child
            elif node.get_left() is None:
                return node.get_right()

            else:
                return node.get_left()

        # recursive case: find the node to be deleted, if it exists
        elif key < node.get_key():
            node.set_left( self.__internal_remove( node.get_left(), key) )
            return node

        else:
            node.set_right( self.__internal_remove( node.get_right(), key) )
            return node

    # Finds the smallest node in the subtree from the node (leftmost value
    # Parameters: node to start from
    # Returns: the smallest node
    def __internal_smallest(self, node):
        current = node
        while not current.get_left() is None:
            current = current.get_left()
        return current

    # search keys ##########
    """
    Lookup methods: finds a specified key
    Parameters: a key (int)
    Returns: False if key doesn't exist, tuple of True and data (any type) if key exists in tree
    """
    def lookup(self, key):
        return self.__internal_lookup(self.root, key)

    # recursive function to lookup key
    # Parameters: the key
    def __internal_lookup(self, node, key):
        # if cannot find the node, it doesn't exist so return False
        if node is None:
            return False

        # if node exists, returns True and the data in a tuple
        elif key == node.get_key():
            return True, node.get_data()

        # look in left & right children for the node
        elif key < node.get_key():
            return self.__internal_lookup(node.get_left(), key)

        else:
            return self.__internal_lookup(node.get_right(), key)

