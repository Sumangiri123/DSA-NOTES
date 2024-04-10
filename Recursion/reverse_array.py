def reverse_array(arr, si, ei):
    # Base case: If the start index is greater than or equal to the end index,
    # it means we've reached the middle of the array or the array is empty,
    # so there's nothing to reverse.
    if si >= ei:
        return
    
    # Swap the elements at the start and end indices.
    arr[si], arr[ei] = arr[ei], arr[si]
    
    # Recursive call to reverse the rest of the array.
    # Move the start index one step forward and the end index one step backward.
    return reverse_array(arr, si+1, ei-1)

# Example usage: Reverse the array [5, 4, 3, 2, 1].
arr = [5, 4, 3, 2, 1]
reverse_array(arr, 0, len(arr)-1)
print(arr)



# Time Complexity

    # The time complexity of the reverse_array function is O(n) because it performs a constant amount of
    # work for each element in the array. Specifically, it swaps two elements and then recursively calls 
    # itself to reverse the rest of the array. Since the function is called n times (where n is the number
    # of elements in the array), the total time complexity is proportional to n, making it O(n) 1.

# Space Complexity

    # The space complexity of the reverse_array function is O(n) because it uses recursion. Each recursive
    # call adds a level to the call stack, and the maximum depth of the recursion is n (the number of 
    # elements in the array). Therefore, the space complexity is proportional to the depth of the 
    # recursion tree, which is n. This means that the function requires additional space for the call stack,
    # making the space complexity O(n) 1.

# In summary, the reverse_array function has a time complexity of O(n) due to the linear number of 
# operations it performs, and a space complexity of O(n) due to the recursive nature of the function.