# Define the binary search function
def binary_search(arr, target):
    # Initialize the start index to 0
    si = 0
    # Initialize the end index to the last index of the array
    ei = len(arr) - 1
    # Continue the search as long as the start index is less than or equal to the end index
    while si <= ei:
        # Calculate the middle index
        mid = si + (ei-si)//2
        # Check if the target is at the middle index
        if arr[mid] == target:
            # If the target is found, return the middle index
            return mid
        # If the target is less than the middle element, adjust the end index to search the left half
        elif arr[mid] > target:
            ei = mid - 1
        # If the target is greater than the middle element, adjust the start index to search the right half
        else:
            si = mid + 1
    # If the target is not found, return the array itself
    return arr

# Example usage
arr = [1,2,3,4,5]
target = 4
print(binary_search(arr, target))

target = 4
print(binary_search(arr, target))


# Time Complexity :
# Space Complexity :

