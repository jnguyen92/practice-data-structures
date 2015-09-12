__author__ = 'Nhuy'

from tree.tree import *

t = BST()
keys = [13, 9, 16, 5, 12, 19]
for k in keys:
    t.insert(k, str(k))

t.print_tree()

t.lookup(12) # true and data
t.lookup(15) # false

t.insert(15, "15")
t.print_tree() # should now contain 15

t.remove(15)
t.print_tree() # should now not contain 15

t.remove(16)
t.print_tree() # should now not contain 16
t.root.get_right() # should be 19

t = BST()
keys = [13, 9, 16, 5, 12, 19, 15, 14]
for k in keys:
    t.insert(k, str(k))

t.print_tree()
t.remove(13) # remove root value and replace with smallest value in right subtree
t.print_tree() # should no longer contain 13
t.root # should be 14