class Solution(object):
    def search(self, arr, target):  
        # Initialize the left and right pointers to the start and end of the array
        low = 0
        high = len(arr) - 1
        
        # Continue the search as long as the left pointer is less than or equal to the right pointer
        while low <= high:
            # Calculate the middle index
            mid = low + (high - low) // 2
            
            # If the target is found at the middle index, return the index
            if arr[mid] == target:
                return mid
            
            # If the left half is sorted
            if arr[low] <= arr[mid]:
                # If the target is in the left half
                if arr[low] <= target < arr[mid]:
                    # Search in the left half
                    high = mid - 1
                else:
                    # Search in the right half
                    low = mid + 1
            else:
                # If the right half is sorted
                if arr[mid] < target <= arr[high]:
                    # Search in the right half
                    low = mid + 1
                else:
                    # Search in the left half
                    high = mid - 1

        # If the target is not found, return -1
        return -1
