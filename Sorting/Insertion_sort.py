def insertion_sort(arr):
    # Iterate over the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # Store the current element as the value to be inserted in the correct position
        v = arr[i]
        # Initialize the index for the element to be compared with
        j = i
        # Continue comparing the current element with the previous elements
        while j >= 1 and arr[j-1] > v:
            # If the previous element is greater, shift it to the right
            arr[j] = arr[j-1]
            # Move to the previous element
            j -= 1
        # Insert the current element in its correct position
        arr[j] = v
    # Return the sorted array
    return arr


# Example usage
arr = [5, 4, 1, 3, 2]
print(insertion_sort(arr))


# Time Complexity : O(n^2) where n denotes size of array -- Due to use of nested loops
# Space Complexity : O(1) -- As no external data structure is used in this code

# Stable Sorting -- As there is chance of change in relative position of same element

# # Comparisions directly proportional to n^2
# Swapping directly proportional to n^2

# Why we use Insertion sort inspite of not having better time complexity than Buuble sort?
# Insertion Sort is an online algorithm, meaning it can sort elements as they are received, without needing to have all 
# the data upfront. This is particularly useful in scenarios where data is coming in a stream and needs to be sorted in real-time.
