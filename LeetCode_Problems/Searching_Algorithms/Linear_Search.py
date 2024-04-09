class Solution(object):
    def search(self, nums, target):
        # Iterate through each number in the list
        for i in range(len(nums)):
            # Check if the current number is equal to the target
            if nums[i] == target:
                # If the target is found, return its index
                return i
        # If the target is not found after checking all numbers, return -1
        return -1


# Time Complexity:

    # O(N): The time complexity is linear, where N is the number of items in the list. This is because the algorithm iterates through each element in the list once.

# Space Complexity:

    # O(1): The space complexity is constant, as the algorithm uses a fixed amount of space to store the index and does not use any additional data structures that grow with the size of the input list.

# This linear search algorithm is straightforward and effective for finding the index of a target number in a list. It's particularly
# useful for small datasets or when the list is not sorted, as it does not require any preprocessing or sorting of the list
