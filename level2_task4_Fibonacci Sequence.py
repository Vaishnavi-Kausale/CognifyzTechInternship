def generate_fibonacci(num_terms):
    # Validate the input
    if num_terms <= 0:
        print("Please enter a positive integer.")
        return
    
    # Initialize the Fibonacci sequence
    fib_sequence = []
    a, b = 0, 1

    for _ in range(num_terms):
        fib_sequence.append(a)
        a, b = b, a + b

    # Display the Fibonacci sequence
    print("Fibonacci sequence:")
    print(fib_sequence)

def main():
    print("Fibonacci Sequence Generator")
    try:
        num_terms = int(input("Enter the number of terms: "))
        generate_fibonacci(num_terms)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Run the Fibonacci sequence generator
main()
