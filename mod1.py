# ---------------------------------------------------------------------
print("Importing module 1.")         # Always runs when module imported

def collatz(n: int) -> list:       # Returns Collatz chain for number n
    current, history = n, [n]
    while current > 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1
        history.append(current)
    return history

if __name__ == "__main__":          # Runs ONLY if executed as a script
    import sys
    _, n = sys.argv              # Gets the first command line argument
    print(collatz(int(n)))