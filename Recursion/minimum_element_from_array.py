# Define a function named 'minimum_element' that takes a list 'arr' as an argument
def minimum_element(arr):
    # Base case: if the length of 'arr' is 1, return the first element
    # This is because the minimum element in a list with only one element is that element itself
    if len(arr) == 1:
        return arr[0]
    # Recursive case: return the minimum of the first element of 'arr' and the minimum of the rest of the list
    # This is achieved by calling the 'minimum_element' function recursively with the rest of the list (excluding the first element)
    # The 'min' function is used to find the minimum of the first element and the result of the recursive call
    return min(arr[0], minimum_element(arr[1:]))

# Define a list 'arr' with the elements [5, 3, 8, 9, 7]
arr = [5, 3, 8, 9, 7]
# Print the result of calling the 'minimum_element' function with 'arr' as the argument
print(minimum_element(arr))


# Recurrence Relation :

# Time Complexity :
# Space Complexity :