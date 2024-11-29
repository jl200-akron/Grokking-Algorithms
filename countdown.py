def countDown(i):
    """Recursion"""
    print(i)
    if i <= 1:
        return
    else:
        countDown(i-1)

# Example usage
countDown(30)