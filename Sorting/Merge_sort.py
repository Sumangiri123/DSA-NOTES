# Function to perform merge sort on an array
def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) == 1:
        return 
    # Find the middle index of the array
    mid = len(arr) // 2
    # Split the array into two halves
    left = arr[:mid]
    right = arr[mid:]
    # Recursively sort the left half
    merge_sort(left)
    # Recursively sort the right half
    merge_sort(right)
    # Merge the sorted halves
    merge(arr, left, right)

# Function to merge two sorted halves of an array
def merge(arr, left, right):
    i = 0 # Index for left array
    j = 0 # Index for right array
    k = 0 # Index for merged array
    # Merge the left and right arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # Copy the remaining elements of left, if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    # Copy the remaining elements of right, if any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
arr = [5, 4, 3, 2, 1]
merge_sort(arr)
print(arr)



# Time Complexity :
# Space Complexity :