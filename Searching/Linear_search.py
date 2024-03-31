# Define a function named 'Linear_search' that takes two parameters: 'arr' which is the list to be searched, and 'target' which is the value to be found.
def Linear_search(arr, target):
    # Iterate through each index in the list 'arr'.
    for i in range(len(arr)):
        # Check if the current element at index 'i' is equal to the 'target' value.
        if arr[i] == target:
            # If the target is found, return a formatted string indicating the index position where the target was found.
            return f"Found At Index Position : {i}"
    # If the target is not found after checking all elements, return -1 to indicate that the target is not present in the list.
    return -1


# Initialize an array with some elements.
arr = [1,2,8,5,4]
# Define the target value to be searched in the array.
target = 8
# Call the 'Linear_search' function with the array and target value, and print the result.
print(Linear_search(arr, target))
