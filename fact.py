def fact(x):
    """Call stack & Recursion"""
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

# Example usage
my_x = 5
result = fact(my_x)
print(f"Factorial of {my_x} is {result}.")