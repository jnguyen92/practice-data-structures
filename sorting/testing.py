__author__ = 'Nhuy'

from sorting.sort import *
import random

random.seed(1)
x = [random.randint(0, 100) for i in range(20)]
x

bubs = list(x)
bubble_sort(bubs)

sel = list(x)
selection_sort(sel)

ins = list(x)
insertion_sort(ins)

merge = list(x)
merge_sort(merge) # failed

quick = list(x)
quick_sort(quick)

