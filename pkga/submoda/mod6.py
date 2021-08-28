# ---------------------------------------------------------------------
'''Docstring of mod6.

Contains recreations of the four basic operations.'''

print("Importing module 6.")         # Always runs when module imported

def adder(a: float = 0, b: float = 0) -> float:
    '''Adds two real numbers together and returns the result.
    
    Arguments:
    a, b: Real numbers to be added. Defaults to 0.
    '''
    return a + b

def suber(a: float = 0, b: float = 0) -> float:
    '''Subtracts a real number from another and returns the result.
    
    Arguments:
    a: Real number being subtracted from. Defaults to 0.
    b: Real number being subtracted. Defaults to 0.
    '''
    return a - b

def muler(a: float = 0, b: float = 0) -> float:
    '''Multiplies two real numbers together and returns the result.
    
    Arguments:
    a, b: Real numbers to be multiplied. Defaults to 0.'''
    return a * b

def diver(a: float = 0, b: float = 1) -> float:
    '''Divides one real number by another and returns the result.
    
    Arguments:
    a: The dividend, a real number. Defaults to 0.
    b: The divisor, a real number. Defaults to 1.'''
    return a / b
