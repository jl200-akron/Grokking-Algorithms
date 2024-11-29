def sum(arr):
    """Compute the sum of the arr using recursion"""
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])

# Example usage:
my_arr = [1, 2, 3, 4, 5, 6, 7]
result = sum(my_arr)
print("Sum = ", result)