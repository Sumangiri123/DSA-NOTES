# Define a function named 'linear_search' that takes three arguments: 'arr' as the list to search, 'si' as the starting index, and 'target' as the value to find
def linear_search(arr, si, target):
    # Base case: if the starting index 'si' is greater than or equal to the length of 'arr', return -1
    # This indicates that the search has reached the end of the list without finding the target
    if si > len(arr) - 1:
        return -1
    # If the current element at index 'si' in 'arr' is equal to 'target', return a formatted string indicating the index position
    elif arr[si] == target:
        return f"Found at index position : {si}"
    # Recursive case: if the current element is not the target, call 'linear_search' with the next index 'si+1' and the same 'target'
    # This continues the search through the list
    else:
        return linear_search(arr, si + 1, target)

# Define a list 'arr' with the elements [1, 2, 3, 4, 5]
arr = [1, 2, 3, 4, 5]
# Define the target value to search for as 3
target = 3
# Define the starting index 'si' as 0
si = 0
# Call the 'linear_search' function with 'arr', 'si', and 'target' as arguments and print the result
print(linear_search(arr, si, target))




# Recurrence Relation :

# Time Complexity :
# Space Complexity :