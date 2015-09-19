__author__ = 'Nhuy'

from graph.graph import *

g = Graph()

for i in range(6):
    g.add_node(i)

g.link_nodes(0, 2)
g.link_nodes(2, 3)
g.link_nodes(3, 4)
g.link_nodes(3, 1)
g.link_nodes(1, 0)
g.link_nodes(0, 4)
g.link_nodes(4, 5)

g.set_all_not_visited()
dfs(g, 0) # returns 0, 4, 5, 2, 3, 1 or 0, 2, 3, 1, 4, 5
g.set_all_not_visited()
bfs(g, 0) # prints 0, 4, 2, 5, 3, 1 (or slight switches due to which came first in storage array)

g.is_connected() # True
g.is_path(2, 4) # True
g.is_path(4, 5) # True
g.is_path(4, 2) # False
g.nodes_from(4) # 4,5
g.nodes_from(0) # all
# g.shortest_path(0, 5) # currently under construction


stat = Graph()

stat_classes = [609, 610, 849, 850, 998, 709, 710, 641, 642, 760, 761, "graduate!"]

for i in stat_classes:
    stat.add_node(i)

stat.link_nodes(609, 610)
stat.link_nodes(610, 709)
stat.link_nodes(610, 998)
stat.link_nodes(709, 710)
stat.link_nodes(849, 850)
stat.link_nodes(850, 998)
stat.link_nodes(641, 642)
stat.link_nodes(760, 761)
stat.link_nodes(998, "graduate!")
stat.link_nodes(642, "graduate!")

stat.is_connected() # False
stat.is_path("610", "graduate!") # True
# stat.is_path("849", "760") # False


stat.set_all_not_visited()
dfs(stat, 849)
