def rotate_array(arr, k):
    # Calculate the length of the array.
    n = len(arr)
    
    # Adjust k to be within the range of the array length.
    # This is effective for very large values of K.
    k = k % n
    
    # Initialize a counter for the loop.
    j = 1
    
    # Base case: If k is 0, the array is already rotated.
    if k == 0:
        print(arr)
        return
    else:
        # Swap the first element with the last element.
        prev = arr[0]
        curr = arr[0]
        arr[0] = arr[n-1]
        
        # Rotate the rest of the array by moving each element to the previous position.
        while j < n:
            curr = arr[j]
            arr[j] = prev
            prev = curr
            j += 1
        
        # Recursively rotate the array for the remaining k-1 rotations.
        rotate_array(arr, k-1)

# Example usage: Rotate the array [1, 2, 3, 4, 5] by 2 positions.
arr = [1, 2, 3, 4, 5]
k = 2 # rotate 2 times
rotate_array(arr, k)



# Time Complexity

    # The time complexity of the rotate_array function is O(nk) because it performs a constant amount of 
    # work for each element in the array for each rotation. Specifically, it swaps elements and then 
    # recursively calls itself to rotate the array for the remaining k-1 rotations. Since the function is 
    # called n times (where n is the number of elements in the array) for each rotation, and there are k 
    # rotations, the total time complexity is proportional to nk, making it O(nk) 3.

# Space Complexity
    
    # The space complexity of the rotate_array function is O(n) because it uses recursion. Each recursive 
    # call adds a level to the call stack, and the maximum depth of the recursion is n (the number of 
    # elements in the array). Therefore, the space complexity is proportional to the depth of the recursion 
    # tree, which is n. This means that the function requires additional space for the call stack, making 
    # the space complexity O(n) 3.

# In summary, the rotate_array function has a time complexity of O(nk) due to the linear number of operations
# it performs for each rotation, and a space complexity of O(n) due to the recursive nature of the function.