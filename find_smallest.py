def findSmallest(arr):
    """Find the smallest index in the arr"""
    # Initialize the smallest element/index
    smallest, smallest_index = arr[0], 0
    
    # Traverse through all elements in the array
    for i in range(1, len(arr)):
        
        # Compare the minimum element with current element
        if arr[i] < smallest:
            
            # Swap the current element with the previous minimum element
            smallest = arr[i]
            smallest_index = i
            
    return smallest_index   # Return the index of the smallest element
    
 
# Example usage
my_arr = [5, 3, 6 ,2, 10]

my_index = findSmallest(my_arr)

print(f"The index of the smallest element is {my_index}.")