__author__ = 'Nhuy'
# Note: work on the iterator

## Testing doubly linked list
from linked_list.doubly_linked_list import *
l = Linked_List()

l.append(3)
l.append(5)
l.push("start")
l.append("end")
l.insert(1, "2nd")
l.print_list()
# should print out:
# start
# 2nd
# 3
# 5
# end

l.insert(l.size()+2, "hi")
# should error

l.pop(0)
l.pop()
l.pop(1)
l.print_list()
# should print out:
# 2nd
# 5

it = iter(l)
it.next()
l.remove(it.next())
l.print_list()
# should print out:
# 2nd

l.insert(1, 4)
l.append(8)
l.push("teehee")
l.print_list()
# should print out:
# teehee
# 2nd
# 4
# 8

it = iter(l)
it.next()
l.remove(it.next())
l.print_list()
# should print out:
# teehee
# 4
# 8

l.pop()
l.pop(0)
l.pop() # empty list after this
l.pop()
# should fail - empty list

l.append("testing")
l.rm("testing")