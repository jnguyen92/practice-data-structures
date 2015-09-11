__author__ = 'Nhuy'


class Tree_Node:
    def __init__(self, key = None, data = None, left_child = None, right_child = None):
        self.key = key
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return "%s: %s" % ( str(self.key), str(self.data) )

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

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

    def __eq__(self, other_node):
        return self.key == other_node.get_key()

    def __ge__(self, other_node):
        return self.key > other_node.get_key()

    def __le__(self, other_node):
        return self.key < other_node.get_key()


class BST:

    def __init__(self):
        self.root = None

    def __repr__(self):
        return "a binary search tree"

    def print_tree(self):
        self.__internal_print(self.root)

    def __internal_print(self, node):

        if not node.get_left() is None:
            self.__internal_print( node.get_left() )

        print node

        if not node.get_right() is None:
            self.__internal_print( node.get_right() )

    def insert(self, key, data):
        self.root = self.__internal_insert(self.root, key, data)

    def __internal_insert(self, node, key, data):
        if node is None:
            return Tree_Node(key, data)

        elif key == node.get_key():
            raise Exception("duplicated key")

        elif key < node.get_key():
            node.set_left( self.__internal_insert( node.get_left(), key, data) )
            return node

        else:
            node.set_right( self.__internal_insert( node.get_right(), key, data))
            return node


    #def remove(self, key):



    def lookup(self, key):
        return self.__internal_lookup(self.root, key)

    def __internal_lookup(self, node, key):
        if node is None:
            return False

        elif key == node.get_key():
            return True

        elif key < node.get_key():
            return self.__internal_lookup(node.get_left(), key)

        else:
            return self.__internal_lookup(node.get_right(), key)


