# Define a function named 'Selection_sort' that takes a list 'arr' as input.
def Selection_sort(arr):
    # Iterate through each index in the list 'arr'.
    for i in range(len(arr)):
        # Assume the current index is the minimum.
        min = i
        # Iterate through the rest of the list starting from the next index.
        for j in range(i+1, len(arr)):
            # If a smaller element is found, update the minimum index.
            if arr[j] < arr[min]:
                min = j
        # Swap the element at the current index with the smallest element found.
        arr[i], arr[min] = arr[min], arr[i]
    # Return the sorted list.
    return arr


# Initialize an array with unsorted elements.
arr = [5,8,1,6,2,4,3]
# Print the sorted array by calling the 'Selection_sort' function.
print(Selection_sort(arr))
