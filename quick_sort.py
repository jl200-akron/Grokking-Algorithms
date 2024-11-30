def quick_sort(arr):
    """Sort (low to high) the arr using quick sort method"""
    if len(arr) < 2:
        return arr  # 0 or 1 element
    else:
        # Choose 1st element as the pivot
        pivot = arr[0]
        # Subarr with elements lower than pivot
        lower = [i for i in arr[1:] if i <= pivot]
        # Subarr with elements highter than pivot
        higher = [i for i in arr[1:] if i > pivot]
        
        # Recursively apply quick_sort to the subarrs, and combine them with the pivot
        return quick_sort(lower) + [pivot] + quick_sort(higher)

# Example usage:
my_arr = [5, 6, 3, 9, 2, 10, 99, 11, 123]
result = quick_sort(my_arr)
print("Original arrary: ", my_arr)
print("Sorted array: ", result)
    