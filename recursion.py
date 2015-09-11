__author__ = 'Nhuy'

# function to find factorial of a number
def factorial(N):
    if N < 0:
        return "factorials defined on positive numbers only"

    if N == 0 or N == 1:
        return 1

    else:
        return N * factorial(N-1)

# function to reverse a string
def reverse_string(string):
    if len(string) == 0:
        return ""

    else:
        return reverse_string(string[1:]) + string[:1]

# function to determine if a string is a palindrome
def is_palindrome(string):

    old_string = "".join( string.split() ).lower()
    new_string = reverse_string(old_string)
    return old_string == new_string

# function to convert numbers into strings
def num_to_str(num):
    string_num = "0123456789"
    if num == 0:
        return ""
    else:
        return num_to_str(num/10) + string_num[ num % 10 ]

# function to determine how many coins to given customer as change
def coin_machine():

# function to determine if maze is exitable
def maze():
