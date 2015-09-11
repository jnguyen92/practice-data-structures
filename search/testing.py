__author__ = 'Nhuy'

from search.search import *

test = range(10)

seq_search(test, 4) # TRUE
seq_search(test, 4.5) # FALSE

bin_search(test, 4) # TRUE
bin_search(test, 4.5) # FALSE
