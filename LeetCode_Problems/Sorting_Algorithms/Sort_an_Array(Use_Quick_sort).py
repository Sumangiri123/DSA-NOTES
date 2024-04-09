class Solution(object):
    def sortArray(self, nums):
        # Function to partition the array around a pivot
        def partition(arr, low, high):
            # Choose the last element as pivot
            pivot = arr[high]
            # Pointer for greater element
            i = low - 1
            # Traverse through all elements
            for j in range(low, high):
                # If current element is smaller than or equal to pivot
                if arr[j] <= pivot:
                    # Increment index of smaller element
                    i += 1
                    # Swap the found element with the element at index i
                    arr[i], arr[j] = arr[j], arr[i]
            # Swap the pivot element with the element at index i+1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            # Return the index of the pivot element
            return i + 1

        # Function to perform QuickSort
        def QuickSort(nums, low, high):
            # Base case: if low index is greater than or equal to high index, return
            if low >= high:
                return
            # Partition the array and get the pivot index
            pi = partition(nums, low, high)
            # Recursively sort elements before partition and after partition
            QuickSort(nums, low, pi - 1)
            QuickSort(nums, pi + 1, high)

        # Call QuickSort on the entire array
        QuickSort(nums, 0, len(nums) - 1)
        # Return the sorted array
        return nums



# Time Complexity

    # Best and Average Case: The average-case time complexity of QuickSort is O(n log(n)). This is because, on average, the partitioning process divides the array into two roughly equal parts, leading to a balanced recursion tree. The time complexity is linear in the number of elements due to the partitioning process and logarithmic in the number of levels of recursion, which is proportional to the number of elements 12.
    # Worst Case: The worst-case time complexity is O(n^2). This occurs when the pivot choice consistently results in unbalanced partitions, leading to a skewed recursion tree where one side of the partition is much larger than the other. This scenario is rare but can significantly degrade performance 12.

# Space Complexity

    # Best and Average Case: The space complexity in the best and average cases is O(log(n)). This is due to the depth of the recursion tree, which is proportional to the number of levels of recursion, which is logarithmic in the number of elements. The space is used by the call stack to store the recursive function calls 12.
    # Worst Case: In the worst case, the space complexity can become O(n). This happens when the partitioning is highly unbalanced, leading to a deep recursion stack that requires a call stack of size proportional to the number of elements. This scenario is rare but can occur if the pivot selection strategy is not effective 12.

# In summary, QuickSort is an efficient sorting algorithm with a favorable average-case time complexity of
# O(n log(n)) and a space complexity of O(log(n)) in the best and average cases. However, its performance
# can degrade to O(n^2) time complexity and O(n) space complexity in the worst case, making it important 
# to choose a good pivot selection strategy to avoid these worst-case scenarios