# ---------------------------------------------------------------------
print("1. List functions...")               # Use [] for defining lists
a = [1, 2]
print(a)
a.extend([3, 4])            # Extended concatenates list to end of list
print(a)
a.append([5, 6])         # By contrast, append inserts into one element
print(a)
a.insert(1, 7)                      # Insert can insert values mid-list
print(a)
a.remove(7)                             # Remove removes matching VALUE
print(a)
del(a[0])                                  # Del removes matching INDEX
print(a)
b = a.pop(-2)               # Pop removes matching INDEX and returns it
print(a, b)
b = a.index(3)                           # Index returns INDEX of VALUE
print(b)
b = [3, 1, 3, 2, 1, 2, 3, 1, 3]
c = b.count(1)          # Returns number of times VALUE appears in list
print(b, c)
b.sort()                                          # Sorts list's values
print(b)
a.clear()                                             # Clears the list
print(a)

# ---------------------------------------------------------------------
print("\n2. Stacks and queues...")
stack = []         # Adding and removing from RIGHT END of list is fast
stack.append(5)    # So lists work well as stacks from RIGHT END
stack.append(7)
stack.append(2)
print(stack.pop(), stack.pop(), stack.pop())

queue = []          # Adding and removing from LEFT END of list is SLOW
queue.append(5)     # So lists work poorly as queues, because no matter
queue.append(7)     # what, you must use pop(0) or insert(0), and both
queue.append(2)     # are slow since the whole list must be updated
print(queue.pop(0), queue.pop(0), queue.pop(0))

import collections
queue = collections.deque([])    # Use collections.deque to make queues
queue.append(5)                  # Either append+popleft
queue.append(7)                  # or leftappend+pop
queue.append(2)
print(queue.popleft(), queue.popleft(), queue.popleft())

# ---------------------------------------------------------------------
print("\n3. Map...")

# map(func, list) returns an object which applies func to all members
# of a list. That is to say, map(f, [x, y, z]) --> [f(x), f(y), f(z)]
# and map(g, [a, b, c], [x, y, z]) --> [g(a, x), g(b, y), g(c, z)]
# Can use built-in function, custom function or lambda function...

a = [[2, 3], [4, 7], [5, 12], [6, 18], [7, 25]]
b = map(sum, a)
print(a, list(b))                                   # In built function

a = [1, 2, 3, 4, 5]
def squarer(number):
    return number * number
b = map(squarer, a)
print(a, list(b))                                        # Def function

a = [3, 5, 1]
b = [2, 7, 6]
c = map(lambda x, y: (x - y) ** 2, a, b)
print(a, b, list(c))                 # Lambda function + multiple lists

# ---------------------------------------------------------------------
print("\n4. List comprehensions...")                # [.. for .. in ..]

a = [1, 2, 3, 4, 5]
b = [number ** 2 for number in a]
print(a, b)                                 # Simple list comprehension

a = [1, 2, 3]
b = [4, 5, 6]
c = [[numbera, numberb] for numbera in a for numberb in b]
print(a, b, c)           # List comprehension over product of two lists

a = [1, 4, 6, 9, 12, 13, 17, 19, 20]
b = [number for number in a if number % 2 == 1]
print(a, b)                     # List comprehension with a conditional

a = ["Cheese", "Cookies", "Honey", "Mayonnaise", "Mints", "Mustard", 
"Soda"]
b = [4.49, 2.00, 8.25, 3.99, 6.39, 2.36, 2.05]
c = [(item, price) for item, price in zip(a, b)]
print(a, b, c)       # List comprehension over two lists simultaneously

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[row[col] for row in a] for col in range(3)]
print(a, b)                                 # Nested list comprehension

c = list(zip(*a))
print(c)      # Same as above, but a preferred non-comprehension method

# ---------------------------------------------------------------------
print("\n5. Tuples...")                    # Use () for defining tuples

a = (1, 2, 3)                                           # Regular tuple
b = ((1, 2), 3, (5, 6, 7))                       # Nested, varied tuple
c = 1, 2, 3                                 # Brackets are not required
d = (1)                                               # Singleton tuple
e = 1,                           # Another single tuple, comma required
print(a, b, c, d, e)

# ---------------------------------------------------------------------
print("\n6. Sets...")                        # Use {} for defining sets

a = set()                             # Must use set() for an empty set
b = {1, 1, 3, 2, 4}    # Sets are UNORDERED and duplicates are combined
c = {2, 3, 6, 5}
d = b | c                                                          # OR
e = b & c                                                         # AND
f = b ^ c                                                         # XOR
g = b - c                                                  # Difference
h = {num ** 2 for num in range(1, 6)}               # Set comprehension
print(a, b, c, d, e, f, g, h)

# ---------------------------------------------------------------------
print("\n7. Dictionaries...")  # Use {key:value, ..} for defining dicts

a = {'a': 1, 'b': 2, 'c': 3}                    # Defining a dictionary
a['a'] = 4                                           # Changing a value
a['d'] = 5                                             # Adding a value
b = {'d': 6, 'e': 7, 'f': 8}
c = {key: value for key, value in (('g', 9), ('h', 10))}    # Dict comp
d = dict([('i', 11), ('j', 12)])   # Another way to create a dictionary
e = {**b, **c, **d}         # Merging dictionaries with tuple unpacking
print(a, b, c, d, e)