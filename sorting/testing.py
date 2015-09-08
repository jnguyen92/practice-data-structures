__author__ = 'Nhuy'

from sorting.sort import *
import numpy as np

np.random.seed(1)
x = np.random.randint(0,100, 20)
bubble_sort(x)

np.random.seed(1)
x = np.random.randint(0,100, 20)
selection_sort(x)

np.random.seed(1)
x = np.random.randint(0,100, 20)
insertion_sort(x)

np.random.seed(1)
x = np.random.randint(0,100, 20)
merge_sort(x) # failed

np.random.seed(1)
x = np.random.randint(0,100, 20)
quick_sort(x)

