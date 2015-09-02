## Testing   doubly linked list
l = Linked_List()
l.append(Node(1))
l.append(Node(5))
l.push(Node("start"))
l.append(Node("end"))
l.insert(1, Node("2nd"))
#l.insert(l.size()+1, Node("hi")) # error
# it = iter(l)
#l.remove(index = 0)
l.pop(0)
l.pop()
l
l.pop(1)
l
#l.pop(5)

it = iter(l)
it.next()
l.remove(it.next())


l.insert(1, Node(4))
l.append(Node(8))
l.push(Node("teehee"))

it = iter(l)
it.next()
l.remove(it.next())