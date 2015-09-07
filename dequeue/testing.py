__author__ = 'Nhuy'

from dequeue.dequeue import *

# Testing whether string is palindrome
def is_palindrome(string):
    # initialize the dequeue
    d = Dequeue()
    for i in string:
        if i != " ":
            d.add_rear(i)
    palindrome = True

    # check whether our string is a palindrome each value
    while d.size() > 1 and palindrome:
        palindrome =  d.remove_front() != d.remove_rear()

    return palindrome



is_palindrome("ATGTA")
is_palindrome("ATTGA")
is_palindrome("I PREFER PI")