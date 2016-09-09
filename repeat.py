#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s * 3 # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

# Gather our code in a main() function
def main():
    print repeat(sys.argv[1], sys.argv[2])      ## gets parameters from main arguments
    print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()