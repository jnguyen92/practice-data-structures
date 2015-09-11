__author__ = 'Nhuy'

from stack.stack import *

# Testing with parenthesis closing - parenthesis defined as (), {}, []
def is_valid_paren(string):
    # initialize the stack
    s = Stack()
    char = list(string)

    for i in char:
        # add openers to the stack
        if i in "({[":
            s.push(i)
        # check that closers are adequate closers
        elif i in ")}]":
            if match(open = s.peek().get_data(), close = i):
                s.pop()
            else:
                return False

    # after going through all the characters, confirm no openers in stack
    if s.is_empty():
        return True
    else:
        return False

# check accurate parenthesis close
def match(open, close):
    openers = "([{"
    closers = ")]}"
    return openers.index(open) == closers.index(close)



is_valid_paren("(((((())") # FALSE
is_valid_paren("()") # TRUE
is_valid_paren("(}") # FALSE
is_valid_paren("({)}") # FALSE
is_valid_paren("({[]})") # TRUE
is_valid_paren("(((((())") # FALSE
is_valid_paren("3 * { (5 + 8) * (10 - 7) }") # TRUE
is_valid_paren("3 * { (5 + 8) * (10 - 7) )") # FALSE






import re

# Testing with html tags - do not anything else to tags
def is_valid_html(string):
    # intialize the stack
    s = Stack()
    words = string.split("<")
    words = [w for w in words if len(w) > 0]

    for i in words:
        # adds the html tag to the stack (only the first tag)
        if not re.match("/", i):
            s.push( re.findall("\\w+", i)[0] )
        # compares the closing tag to the most recent open tag
        else:
            if s.peek().get_data() == re.findall("\w+", i)[0]:
                s.pop()
            else:
                return False

    # confirms stack is emtpy at end of string
    if s.is_empty():
        return True
    else:
        return False




is_valid_html("<head>This is the title</head>") # TRUE
is_valid_html("<html> <head>This is a title</head>") # FALSE
is_valid_html("<html>\n<head>\n<title>Example</title>\n</head>\n<body>\n<h1>Hello, world</h1>\n</body>\n</html>") # TRUE

