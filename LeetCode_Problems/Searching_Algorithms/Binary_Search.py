class Solution(object):
    def search(self, arr, target):
        # Initialize the left and right pointers to the start and end of the array
        left = 0
        right = len(arr) - 1
        
        # Continue the search as long as the left pointer is less than or equal to the right pointer
        while (left <= right):
            # Calculate the middle index
            mid = left + (right - left) // 2
            
            # If the target is found at the middle index, return the index
            if arr[mid] == target:
                return mid
            
            # If the target is greater than the middle element, search in the right half
            elif arr[mid] < target:
                left = mid + 1
            
            # If the target is less than the middle element, search in the left half
            else:
                right = mid - 1
        
        # If the target is not found, return -1
        return -1


# Time Complexity:

#   Best Case: O(1) - This occurs when the target is at the middle of the array.
#   Average Case: O(log n) - On average, the algorithm divides the search space in half with each iteration, leading to a logarithmic time complexity.
#   Worst Case: O(log n) - Even in the worst case, the binary search algorithm performs well with a logarithmic time complexity.

# Space Complexity:

#   Best Case: O(1) - The space complexity is constant because the algorithm only uses a fixed amount of space to store the pointers and the target value.
#   Worst Case: O(1) - The space complexity remains constant regardless of the size of the input array.