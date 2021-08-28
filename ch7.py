# ---------------------------------------------------------------------
print("1. Inserting variables in strings string...")

a, b = 7, 13

# Method 1: Prefix with f and use {<evaluated expression>} in text.
s = f"Your lucky numbers are {a} and {b}!"
print(s)

# Method 2: Append format.(<variables...>) and use {} in text.
s = "Your lucky numbers are {} and {}!".format(a, b)
print(s)
s = "Your lucky numbers are {1} and {0}!".format(a, b)
print(s)
s = "Your lucky numbers are {x} and {y}!".format(x = a, y = b)
print(s)

# Method 3: Append % <tuple of variables> and use % <format> in text.
s = "Your lucky numbers are %d and %d!" % (a, b)
print(s)

# Method 4: Manually use string concatenation, etc.
s = "Your lucky numbers are " + str(a) + " and " + str(b) + "!"
print(s)

# Also see https://docs.python.org/3.9/library/string.html#formatspec &
# https://docs.python.org/3.9/library/stdtypes.html#old-string-formatting

# ---------------------------------------------------------------------
print("2. Reading and writing files...")

with open("file1.txt", "r") as f:   # 'with' ensures files always close
    data = f.read(10)                              # Read 10 characters
    print(data)
    data = f.read(10)        # Reading continues from where it left off
    print(data)
    data = f.readline()      # Reads the rest of the line, including \n
    print(data)
    data = f.read()      # Reads the rest of the file, including all \n
    print(data)
    f.seek(0)          # Sets the pointer back to the start of the file
    data = f.readlines()      # Reads each line as an element of a list
    print(data)                                   # Note it includes \n
    f.seek(0)
    for line in f:                 # Iterating over the lines in a file
        print(line)                               # Note it includes \n
# Due to the use of 'with', the file automatically closes now

with open("file2.txt", "w") as f:         # 'w' for writing; overwrites
    x = "This is a test.\n"
    y = ["This is longer test ", "with multiple strings ", "inserted."]
    f.write(x)                                        # Writes one line
    f.writelines(y)                # Writes list elements, concatenated
    print(f.tell())              # Returns the current pointer position
# Note that any \n must be manually added to the strings!

import json
with open("file3.json", "w") as f:             # Writing to a json file
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    data_json = json.dumps(data)   # Converts any object to JSON string
    f.write(data_json)

with open("file3.json", "r") as f:                # Reading a json file
    data = json.load(f)         # Converts JSON string to Python object
    print(data)

# See also: https://docs.python.org/3.9/library/pickle.html