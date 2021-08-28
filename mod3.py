# ---------------------------------------------------------------------
print("Importing module 3.")         # Always runs when module imported

def strodds(text: str) -> str:      # Returns odd position chars in str
    return text[::2]

def strevens(text: str) -> str:    # Returns even position chars in str
    return text[1::2]

if __name__ == "__main__":          # Runs ONLY if executed as a script
    import sys
    _, txt = sys.argv            # Gets the first command line argument
    print(strodds(txt), strevens(txt))