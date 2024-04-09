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
