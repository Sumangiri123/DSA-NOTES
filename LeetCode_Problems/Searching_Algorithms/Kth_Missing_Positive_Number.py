class Solution(object):
    def findKthPositive(self, arr, k):
        # Initialize an empty list to store missing elements
        missing_elements = []
        
        # Start from the first positive integer
        i = 1
        
        # Continue until we reach positive infinity
        while i < float('inf'):
            # Check if the current integer is not in the array
            if i not in arr:
                # If not, add it to the list of missing elements
                missing_elements.append(i)
            
            # Move to the next integer
            i += 1
            
            # If we have found k missing elements, stop the loop
            if len(missing_elements) == k:
                break

        # Return the kth missing element
        return missing_elements[k-1]


# Time Complexity:

    # Best Case: O(n) - This occurs when the first k missing elements are found early in the iteration.
    # Average Case: O(n) - On average, the algorithm will need to iterate through the entire array to find the kth missing element.
    # Worst Case: O(n) - The worst-case scenario is when the kth missing element is the last element in the array, requiring the algorithm to iterate through the entire array.

# Space Complexity:

    # Best Case: O(1) - This occurs when the first k missing elements are found early in the iteration, and no additional space is needed.
    # Average Case: O(n) - In the average case, the algorithm may need to store up to n missing elements in the list.
    # Worst Case: O(n) - The worst-case scenario is when the kth missing element is the last element in the array, requiring the algorithm to store up to n missing elements.

# This solution is straightforward and effective for finding the kth missing positive integer in an array. However, it's worth 
# noting that the time complexity could be improved by using a more efficient data structure or algorithm, such as binary search 
# or a set, to check for the presence of integers in the array
