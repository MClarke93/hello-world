# ---------------------------------------------------------------------
print("Importing module 2.")         # Always runs when module imported

def triangle(n: int) -> int:          # Returns the nth triangle number
    return (n * (n + 1)) // 2

def fizzbuzz(n: int) -> str:           # Returns fizzbuzz callout for n
    if n % 3 != 0 and n % 5 != 0:
        return str(n)
    elif n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    else:
        return "FizzBuzz"

if __name__ == "__main__":          # Runs ONLY if executed as a script
    import sys
    _, n = sys.argv              # Gets the first command line argument
    print(triangle(int(n)), fizzbuzz(int(n)))