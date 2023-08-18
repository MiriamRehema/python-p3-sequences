#!/usr/bin/env python3

#def print_fibonacci(length):
def print_fibonacci(length):
   
    if length == 0:
        print("[]")
        return
    elif length == 1:
        print("[0]")
        return
    
    fibonacci_sequence = [0,1]
    
    while len(fibonacci_sequence) < length:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    
    print("[" + ", ".join(map(str, fibonacci_sequence)) + "]")

# Example usage
print_fibonacci(0)   # Prints []
print_fibonacci(10)  # Prints Fibonacci sequence up to length 10

#print_fibonacci(10)  # Prints Fibonacci sequence up to length 10

    