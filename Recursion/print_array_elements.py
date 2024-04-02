# Define a function named 'print_array' that takes a list 'arr' as an argument
def print_array(arr):
    # Base case: if the length of 'arr' is 0, return immediately
    # This is because there are no elements to print
    if len(arr) == 0:
        return
    # Print the first element of 'arr'
    print(arr[0])
    # Recursive case: call 'print_array' with the rest of the list (excluding the first element)
    # This is done by slicing 'arr' from the second element onwards
    print_array(arr[1:])


# Define a list 'arr' with the elements [1, 2, 3, 4]
arr = [1, 2, 3, 4]
# Call the 'print_array' function with 'arr' as the argument
print_array(arr)



# Recurrence Relation :

# Time Complexity :
# Space Complexity :
