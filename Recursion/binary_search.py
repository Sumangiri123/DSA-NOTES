# Define the binary search function
def binary_search(arr, si, ei, target):
    # Base case: if the start index is greater than the end index, the target is not in the array
    if si > ei:
        return -1
    # Calculate the middle index
    mid = si + (ei-si)//2
    # Check if the target is at the middle index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search in the left half
    elif arr[mid] > target:
        return binary_search(arr, si, mid - 1, target)
    # If the target is greater than the middle element, search in the right half
    else:
        return binary_search(arr, mid + 1, ei, target)

# Example usage
arr = [1,2,3,4,5]
target = 5
si = 0
ei = len(arr) - 1
print(binary_search(arr, si, ei, target))


# Time Complexity :
# Space Complexity :
