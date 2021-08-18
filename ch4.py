# ---------------------------------------------------------------------
x = input("1. Enter 0 or 1: ")           # IF .. ELIF .. ELSE statement

if x == "0":
    print("You entered zero.")
elif x == "1":
    print("You entered one.")
else:
    print("You didn't enter zero or one.")

# ---------------------------------------------------------------------
print("\n2. Printing foods different ways:")           # FOR statements

x = ["Apple", "Banana", "Carrot", "Date"]

for food in x:                             # Looping over list elements
    print(food)

for i in range(len(x)):                # Looping over a list of numbers
    print(i, x[i])

for i, food in enumerate(x):        # Looping over elements and numbers
    print(i, food)

y = {"Apple" : 0, "Banana" : 1, "Carrot" : 2, "Date" : 3}

for key in y:                            # Looping over dictionary keys
    print(y[key], key)

for key, value in y.items():  # Looping over dictionary keys and values
    print(value, key)

z = [0, 1, 2, 3]

for food, i in zip(x, z):       # Looping over two lists simultaneously
    print(i, food)

# ---------------------------------------------------------------------
print("\n3. Modifying lists while looping over them:")

x = [1, 2, 3, 4, 5]             # Ways to modify lists while looping...
print(x)

y = []                                              # Create a new list
for element in x:
    y.append(element * 2)
print(y)

for i, element in enumerate(x.copy()):               # Loop over a copy
    x[i] = element * 2
print(x)

# ---------------------------------------------------------------------
print("\n4.")            # FOR ... BREAK / CONTINUE ... ELSE statements

y = []
for i in range(1, 6):
    x = input(f"Enter string #{i} or \"q\" to quit: ")
    if x == "q":
        break                                # Immediately escapes loop
    elif x == "":
        print("Nothing, huh?")
        continue               # Immediately starts next loop iteration
    y.append(x)
else:                 # Only executes if loop finishes without breaking
    print("Nice! You entered five strings.")

print("Strings:", *y)        # Asterisk fills arguments with list items

# ---------------------------------------------------------------------
print("\n5. Printing with nested loops:")            # Nested FOR loops

x = ["Apple", "Banana", "Carrot", "Date"]
y = ["Tasty", "Bland"]

for food in x:                                  # Actually nested lists
    for quality in y:
        print(quality, food)

import itertools                   # Combining the lists before looping
for food, quality in itertools.product(x, y):
    print(quality, food)

# ---------------------------------------------------------------------
print("\n6. Printing numbers with while loops:")      # WHILE statement

x = 0                                               # Normal while loop
while x < 8:
    print(x)
    x = x + 1

x = 0                         # Endless loop that's escaped using BREAK
while True:
    print(x)
    x = x + 1
    if x >= 8:
        break

# ---------------------------------------------------------------------
print("\n7. Functions:")                    # DEF and RETURN statements

def a():                        # Function with no arguments, no return
    print("Function A.")

def b(thing, color):                          # Function with arguments
    print(f"Function B. The {thing} is {color}.")

def c(num1, num2):                # Functions with arguments and return
    return num1 + num2

def d(name, age=18, subject="math"):     # Function with default values
    print(f"My name is {name}. I am {age} years old and enjoy "
    f"{subject} class.")

def e(numlist=[]):                      # Function with mutable default
    numlist.append(1)
    print(numlist)

def f(*args):                    # Asterisk collects pos args into list
    print(f"The sum is {sum(args)}")

def g(**kwargs):      # Double asterisk collects keyword args into dict
    for kwarg, value in kwargs.items():
        print(f"The {kwarg} is {value}")

def h(number, *args, **kwargs):                    # Everything at once
    print(f"Number is {number}, args are {args}, kwargs are {kwargs}")

def i(arga, /, argb, *, argc):                      # Special arguments
    print(f"{arga} must be positional")
    print(f"{argb} can be anything")
    print(f"{argc} must be keyword")

def j(multiplier):                        # Returning a lambda function
    return lambda x: print(x * multiplier)

def k(func):                                # Passing a lambda function
    print(func(2))

a()                                # Include (), even with no arguments
b("sky", "azure")              # Positional arguments; must be in order
b(color="dark", thing="earth")      # Keyword arguments; can be any way
b("grass", color="green")             # Mixed arguments; pos before key
x = c(9, 7)                                   # Catching returned value
d("Alice")                          # Can ommit arguments with defaults
d("Bob", x, "science")                         # Can overwrite defaults
e()
e()             # Bewear! Mutable defaults can be accidentally changed!
f(1, 2, 5, 7, 19)                             # Any number of arguments
g(day="fine", time="right")           # Any number of keyword arguments
h(2, "a", "b", "c", first="d", last="e")        # All keyword arguments
i("AA", "BB", argc="CC")                # Strictly controlled arguments
x = j(3)                       # Stores a lambda function for use later
x(10)                                    # Executes the lambda function
k(lambda x: x + 5)       # Passes lambda function into another function

# ---------------------------------------------------------------------
pass                                               # PASS does nothing!
