class Solution(object):
    def findMin(self, nums):
        # Initialize the minimum index to the first element
        min_index = 0
        # Initialize the left and right pointers
        left = 0
        right = len(nums)-1
        # Binary search loop
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left)//2
            # If the middle element is less than the current minimum, update the minimum index
            if nums[mid] < nums[min_index]:
                min_index = mid
            # If the middle element is greater than the rightmost element, the minimum must be in the right half
            elif nums[mid] > nums[right]: 
                left = mid + 1
            # Otherwise, the minimum must be in the left half
            else:
                right = mid - 1
        # Return the minimum element found
        return nums[min_index]



# Time Complexity Analysis:

    # The time complexity of this algorithm is (O(log n)), where 'n' is the number of elements in the array. This is because 
    # the algorithm uses a binary search approach, which halves the search space in each iteration. The binary search algorithm is
    # efficient for finding the minimum element in a rotated sorted array because it exploits the fact that the array is sorted, 
    # just rotated.

# Space Complexity Analysis:

    # The space complexity of this algorithm is (O(1)), which means it uses a constant amount of extra space. This is because the
    #  algorithm only uses a fixed number of variables (min_index, left, right, and mid) and does not use any additional data 
    # structures whose size depends on the input size.