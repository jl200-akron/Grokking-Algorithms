def binary_search(arr, target):
    """find the position of the item within the sorted list using binary search"""
    # Initialize the low and high pointers
    low = 0                     
    high = len(arr) - 1          
    
    while low <= high:  
        # Find the index of the middle element
        mid = (low + high) // 2 
        
        # Check if the target is at the middle
        if arr[mid] == target:     
            return mid  # Target found, return the index
        
        # If the target is smaller, ignore the right half        
        if arr[mid] > target:      
            high = mid - 1
            
        # If the target is larger, ignore the left half
        else:                   
            low = mid + 1       
    return -1   # Target not found, return -1

# Example usage
my_arr = [1, 3, 5, 7, 9]
my_target = 5

result = binary_search(my_arr, my_target)

if result != -1:
    print(f"Target found at index {result}.")
else:
    print("Target not found")