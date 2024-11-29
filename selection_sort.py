def selection_sort(arr):
    """Sort the arr using selection method"""
    n = len(arr)    # Get the length of the arr
    
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in unsorted part of the array
        min_index = i
        
        # Traverse through the rest of elements in the array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
# Example usage:
my_arr = [64, 25, 12, 22, 11]
print("Original array:", my_arr)
sorted_arr = selection_sort(my_arr)
print("Sorted array:", sorted_arr)