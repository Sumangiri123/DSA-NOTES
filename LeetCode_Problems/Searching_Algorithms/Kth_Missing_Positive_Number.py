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
