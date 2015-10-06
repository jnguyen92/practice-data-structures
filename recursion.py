__author__ = 'Nhuy'

# function to find factorial of a number
def factorial(N):
    # error handling
    if N < 0:
        return "factorials defined on positive numbers only"

    # base case: return 1
    if N == 0 or N == 1:
        return 1

    # recursively compute factorial n! = n * (n-1) * ... 2 * 1
    else:
        return N * factorial(N-1)

# function to reverse a string
def reverse_string(string):
    # base case: empty string return ""
    if len(string) == 0:
        return ""

    # recursive case: take the rest of the string append it to the "first" letter
    else:
        return reverse_string(string[1:]) + string[:1]

# function to determine if a string is a palindrome
def is_palindrome(string):
    # make the string lower case and remove all spaces
    old_string = "".join( string.split() ).lower()
    # compute new string - reversed
    new_string = reverse_string(old_string)
    # compare two strigns
    return old_string == new_string

# function to convert numbers into strings
def num_to_str(num):
    # place numbers into string, each number corresponds to its index in the string
    string_num = "0123456789"
    # base case, value = 0, return empty string
    if num == 0:
        return ""
    # take the "one's" digit and converts it into string, recursively computes for other digits
    else:
        return num_to_str(num/10) + string_num[ num % 10 ]
