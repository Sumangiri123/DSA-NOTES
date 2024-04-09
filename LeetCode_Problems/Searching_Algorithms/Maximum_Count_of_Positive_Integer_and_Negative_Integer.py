class Solution(object):
    def maximumCount(self, nums):
        # Initialize counters for positive and negative numbers
        pos = 0 
        neg = 0
        
        # Iterate through each number in the list
        for i in range(len(nums)):
            # Check if the current number is positive
            if nums[i] > 0:
                pos += 1
            # Check if the current number is negative
            elif nums[i] < 0:
                neg += 1

        # Return the maximum count of positive or negative numbers
        return max(pos, neg)
