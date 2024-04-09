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
