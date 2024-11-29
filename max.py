def max(arr):
    """Find the max in the array using recursion"""
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# Example usage:
my_arr = [1, 2, 3, 9, 5, 6, 7]
result = max(my_arr)
print(f"The max is {result}.")