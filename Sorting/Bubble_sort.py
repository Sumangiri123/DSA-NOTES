# Define a function named 'Bubble_sort' that takes a list 'arr' as input.
def Bubble_sort(arr):
    # Iterate through the list in reverse order, starting from the last element.
    for i in range(len(arr)-1, -1, -1):
        # For each element, iterate through the list up to the current index.
        for j in range(i):
            # If the current element is greater than the next element, swap them.
            if arr[j] > arr[j+1]:
                # Swap the elements using tuple unpacking.
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Return the sorted list.
    return arr

# Initialize an array with unsorted elements.
arr = [5,8,1,6,2,4,3]
# Print the sorted array by calling the 'Bubble_sort' function.
print(Bubble_sort(arr))
