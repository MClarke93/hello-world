# ---------------------------------------------------------------------
'''Docstring of mod7.

Contains some prebuilt mathematical functions.'''

print("Importing module 7.")

import pkga.submoda.mod6 as m6      # Importing from within the package

def func1(a: float, b: float) -> float:
    '''For two numbers a and b, returns the result of 3a - 2b.

    Arguments:
    a, b: Real number variables of the function. Required.
    '''
    return m6.suber(m6.muler(3, a), m6.muler(2, a))

def func2(a: float, b: float) -> float:
    '''For two numbers a and b, returns the result of (a + b)/2.
    
    Arguments:
    a, b: Real number variables of the function. Required.'''
    return m6.diver(m6.adder(a, b), 2)
