# Recursive Fibonacci (Part A) 
def recursive_fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def main():
    # Ask user for input
    while True:
        try:
            n = int(input("Enter a non-negative integer n: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number (0 or more).")

    # Compute and print
    result = recursive_fibonacci(n)
    print(f"\nF({n}) = {result}")

# Run the program
if __name__ == "__main__":
    main()

