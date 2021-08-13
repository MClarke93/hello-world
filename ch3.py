# ---------------------------------------------------------------------
a = 3 + 2                              # =5  (Addition)
b = 9 - a                              # =4  (Subtraction)
c = b * 2                              # =8  (Multiplication)
d = 24 / c                             # =3  (Division)
e = 5 % d                              # =2  (Modulo)
f = 13 // e                            # =6  (Integer division)
g = f ** 2                             # =36 (Exponentation)
h = (f * d - g // a) ** e % c + b / 2  # Order of operations

print(f"1. a = {a} | b = {b} | c = {c} | d = {d} | e = {e} | f = {f} "
f"| g = {g} | h = {h}")

# ---------------------------------------------------------------------
a, b = 3+2J, 2-3J              # Complex numbers & multiple assignment
c, d, e = a + b, a - b, a * b  # Operations on complex numbers

print(f"2. a = {a} | b = {b} | c = {c} | d = {d} | e = {e}")

# ---------------------------------------------------------------------
a = "Hello world"                  # Double quote
b = 'Hello world'                  # Single quote
c = "Hello's world"                # Double quote + single quote
d = 'Hello\'s world'               # Single quote + escape single quote
e = '"Hello world", they said'     # Single quote + double quote
f = "\"Hello world\", they said"   # Double quote + escape double quote
g = r"\"Hello world\", they said"  # Raw string

print(f"3. a = {a} | b = {b} | c = {c} | d = {d} | e = {e} | f = {f} "
f"| g = {g}")

# ---------------------------------------------------------------------
a = 'a' + 'b' + 'c'  # String addition
b = 'a' 'b' 'c'      # Adj literal strings automatically concatenate
c = ('a'
'b'
'c')                 # Brackets to concatenate across multiple lines
d = 3 * 'a'          # String scalar multiplication
e = (a + b + c) * 2  # String expression

print(f"4. a = {a} | b = {b} | c = {c} | d = {d} | e = {e}")

# ---------------------------------------------------------------------
a = "abcdefgh"
b, c = a[0], a[2]      # Single character at index (0 = 1st char)
d, e = a[-1], a[-3]    # From back end (-1 = Last char)
f, g = a[1:4], a[3:7]  # Slices; [a:b] means "[a,b)", so [1:4] = 1,2,3
h, i = a[0:3], a[:3]   # Empty first slot = 0
j, k = a[3:8], a[3:]   # Empty last slot = len()
l, m = a[-3:], a[:-3]  # Indexing from back still slices left to right
n = len(a)             # Returns string length

print(f"5. a = {a} | b = {b} | c = {c} | d = {d} | e = {e} | f = {f} "
f"| g = {g} | h = {h} | i = {i} | j = {j} | k = {k} | l = {l} "
f"| m = {m} | n = {n}")

# ---------------------------------------------------------------------
a = [1, 2, 3, 4]
b, c = a[1], a[-1]                # List indexing
d, e, f = a[:3], a[2:], a[-3:-1]  # List slicing

print(f"6. a = {a} | b = {b} | c = {c} | d = {d} | e = {e} | f = {f}")

# ---------------------------------------------------------------------
a[0], a[2] = 5, 6  # Modifying single values
b = a              # This makes B just another name for A!
c = a.copy()       # This makes C a copy of A, rather than literally A
d = a[1:3]         # Slices are always copies. a[:] equiv to a.copy()
b[1:3] = [7, 8]    # Modifying a slice (also changes A, since B=A!)

print(f"7. a = {a} | b = {b} | c = {c} | d = {d}")

# ---------------------------------------------------------------------
a = [1, 2, 3]
b = a + [4, 5]  # List addition (DOES create a new list)
a[0] = 6        # Changing A does not impact B
c = a * 2       # List multiplication (DOES create a new list)
a[1:] = [7]     # Shrink list (2 element slice -> 1)
a[:1] = [8, 9]  # Grow list (1 element slice -> 2)
d = a.copy()    # Snapshot of A before deletion
a[1:2] = []     # Delete slices
e = a.copy()    # Snapshot of A before wipe
a = []          # Clears list
f = e.copy()
f.append(10)    # Adds element to end of list

print(f"8. a = {a} | b = {b} | c = {c} | d = {d} | e = {e}")

# ---------------------------------------------------------------------
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = a[0][1]         # Indexing into nested list
c = a[1][1:]        # Slicing at a deeper layer
d = a + [10, 11]    # Mixed depth list
d[4] = [12, 13]     # Assigning list to one element nests it inside
d.append([14, 15])  # Appending only adds one element; causes nesting
e = len(d)          # Returns outermost list length

print(f"9. a = {a} | b = {b} | c = {c} | d = {d} | e = {e}")

# ---------------------------------------------------------------------
b = a.copy()        # Returns SHALLOW copy because list is nested!      
b[0][0] = 10        # Modifying nested list in B changes it in A too!
b[2] = [11, 12, 13] # New sublists only happen in B, however.

print(f"10. a = {a} | b = {b} ")

# ---------------------------------------------------------------------
a, b = 3, 5
a, b = b, a                    # Multiassigns evaluate before assigning
a, b = a + b, a - b            # Can even do expressions
c = d = e = 4                  # Can chain assignments like this
e = 7                          # Here, changing E doesn't change C & D
f, g = [9, 10]                 # Lists are 'unpacked' across variables
h, *i = [11, 12, 13]           # *i scoops up remaining nums into list
*j, k = [14, 15, 16]           # Works the other way too
l, [m, n] = [17, [18, 19]]     # Works with nested lists & assignments
*o, [*p] = [20, 21, [22, 23]]  # Nesting and asterisks together

print(f"11. a = {a} | b = {b} | c = {c} | d = {d} | e = {e} | f = {f} "
f"| g = {g} | h = {h} | i = {i} | j = {j} | k = {k} | l = {l} "
f"| m = {m} | n = {n} | o = {o} | p = {p}")
