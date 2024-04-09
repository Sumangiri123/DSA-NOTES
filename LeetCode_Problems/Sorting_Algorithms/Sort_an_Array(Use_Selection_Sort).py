class Solution(object):
    def sortArray(self, nums):
        # Iterate over each element in the list
        for i in range(len(nums)):
            # Assume the current element is the smallest
            min_index = i
            # Iterate over the unsorted part of the list
            for j in range(i, len(nums)):
                # If a smaller element is found, update min_index
                if nums[j] < nums[min_index]:
                    min_index = j
            # Swap the current element with the smallest found in the unsorted part
            nums[i], nums[min_index] = nums[min_index], nums[i]
        # Return the sorted list
        return nums



# Selection Sort has a time complexity of (O(n^2)), where 'n' is the number of elements in the list. This makes it inefficient
#  for large lists compared to more advanced sorting algorithms like QuickSort or MergeSort. However, it has the advantage of
#  being easy to understand and implement, and it performs well for small lists or lists that are already partially sorted.