# ---------------------------------------------------------------------
print("1. Importing...")
import mod1                                # Importing an entire script
a = mod1.collatz(29)                   # Use is <modulename>.<function>
print(a)

import mod2 as m2                              # Importing and renaming
a = m2.triangle(15)                     # Use becomes <name>.<function>
b = m2.fizzbuzz(a) 
print(a, b)

from mod3 import strodds                      # Importing a single name
a = strodds("abcdefgh")
print(a)

from mod3 import strevens as e   # Importing a single name and renaming
a = e("abcdefgh")
print(a)

import dira.mod4 as m4                     # Importing from a directory
a = m4.slope(1, 5, 2, 1)
print(a)

# Search order when importing:
# 1. Built in modules
# 2. Sys.path (current dir -> PYTHONPATH -> install-dependant default)
# Sys.path can be modified during runtime...

import os, sys                   # Importing multiple builtin libraries
dirb = os.path.join(os.path.dirname("__file__"), "dirb")
sys.path.append(dirb)        # Causes Python to check /dirb for scripts

import mod5                     # Importing from an arbitrary directory
a = mod5.distance(3, 3, 6, 7)
print(a)

import pkga.submodb.mod7 as m7               # Imports a custom package
a = m7.func1(8.0, 7.0)    # The package itself refers to sister scripts
b = m7.func2(6.0, 10.0)
print(a, b)

print(dir(), dir(mod1), dir(m2), dir(m4), dir(m7))      # Defined names