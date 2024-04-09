class Solution(object):
    def sortColors(self, nums):
        # Iterate over the list from the last element to the first
        for i in range(len(nums)-1, 0, -1):
            # Iterate over the unsorted part of the list
            for j in range(i):
                # If the current element is greater than the next element
                if nums[j] > nums[j+1]:
                    # Swap the elements
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        # Return the sorted list
        return nums



# This implementation of Bubble Sort is straightforward and easy to understand, making it a good choice for small datasets or 
# when simplicity is preferred over efficiency. However, it's important to note that Bubble Sort has a worst-case and average 
# time complexity of (O(n^2)), where 'n' is the number of elements in the list. This makes it inefficient for large datasets 
# compared to more advanced sorting algorithms like QuickSort or MergeSort.