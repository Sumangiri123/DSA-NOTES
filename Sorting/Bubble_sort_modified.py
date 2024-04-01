def modified_bubble_sort(arr):
    # Iterate over the array from the last element to the first
    for i in range(len(arr)-1, 0, -1):
        # Assume the array is sorted until proven otherwise
        is_sorted = True
        # Iterate over the array from the first element to the current index
        for j in range(i):
            # If the current element is greater than the next element
            if arr[j] > arr[j+1]:
                # Mark the array as not sorted
                is_sorted = False
                # Swap the current element with the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # If the array is sorted, print a message and break the loop
        if is_sorted:
            print("Sorting is Completed")
            break
    # Return the sorted array
    return arr

# Example usage
arr = [1, 2, 6, 5, 4]
print(modified_bubble_sort(arr))

# Time Complexity : O(n^2)  where n is the size of the array -- Due to use of nested loops
# Space complexity : O(1) -- As no external Data structure used in this code

# Stable sorting -- In this Algorithm there is no change of relative Position of same element

# Comparisions directly proportional to n^2
# Swapping directly proportional to n^2

# Modified bubble sort is mainly used for sorted and nearly sorted array(Best Case)
# Time Complexity : O(n) for best case
