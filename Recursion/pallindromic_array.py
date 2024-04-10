def check_pallindromic_array(arr, si, ei):
    # Base case: If the start index is greater than the end index,
    # it means we've checked all elements and haven't found any mismatch,
    # so the array is a palindrome.
    if si > ei:
        return True
    
    # If the elements at the start and end indices are not equal,
    # the array is not a palindrome.
    elif arr[si] != arr[ei]:
        return False
    
    # Recursive case: If the elements at the start and end indices are equal,
    # check the rest of the array by moving the start index one step forward
    # and the end index one step backward.
    else:
        return check_pallindromic_array(arr, si+1, ei-1)

# Example usage: Check if the array [1, 2, 3, 4, 1] is a palindrome.
arr = [1, 2, 3, 4, 1]
print(check_pallindromic_array(arr, 0, len(arr)-1))



# Time Complexity
    
    # The time complexity of the check_pallindromic_array function is O(n) because it performs a constant 
    # amount of work for each element in the array. Specifically, it compares two elements and then recursively
    # calls itself to check the rest of the array. Since the function is called n times (where n is the 
    # number of elements in the array), the total time complexity is proportional to n, making it O(n).

# Space Complexity
    
    # The space complexity of the check_pallindromic_array function is O(n) because it uses recursion. Each
    # recursive call adds a level to the call stack, and the maximum depth of the recursion is n (the number
    # of elements in the array). Therefore, the space complexity is proportional to the depth of the recursion
    # tree, which is n. This means that the function requires additional space for the call stack, making 
    # the space complexity O(n).

# In summary, the check_pallindromic_array function has a time complexity of O(n) due to the linear number
# of operations it performs, and a space complexity of O(n) due to the recursive nature of the function.
