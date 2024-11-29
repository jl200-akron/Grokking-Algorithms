def count(arr):
    """Compute the number of elements in the arr using recursion"""
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])

# Example usage:
my_arr = [1, 2, 3, 4, 5, 6, 7]
result = count(my_arr)
print(f"There are {result} elements in the array.")