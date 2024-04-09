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



# Time Complexity:

    # O(N): The time complexity is linear, where N is the number of items in the list. This is because the algorithm iterates through each element in the list once.

# Space Complexity:

    # O(1): The space complexity is constant, as the algorithm uses a fixed amount of space to store the counters for positive and negative numbers.

# This solution is efficient for counting the maximum number of positive or negative integers in a list, making it suitable for 
# various programming problems that involve analyzing the distribution of positive and negative numbers in a dataset.