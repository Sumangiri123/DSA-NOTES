class Solution(object):
    def permute(self, nums):
        # Define a helper function to generate permutations
        def permutation(nums, left, right, arr):
            # Base case: if left index is equal to right, it means we have a permutation
            if left == right:
                # Append a copy of the current permutation to the result array
                arr.append(nums[:])
                return

            # Iterate over the range from left to right (inclusive)
            for i in range(left, right+1):
                # Swap the elements at the left and current index
                nums[left], nums[i] = nums[i], nums[left]
                # Recursively generate permutations for the rest of the array
                permutation(nums, left+1, right, arr)
                # Swap back the elements to restore the original array for the next iteration
                nums[left], nums[i] = nums[i], nums[left]

        # Initialize an empty list to store the permutations
        arr = []
        # Call the helper function to start generating permutations
        permutation(nums, 0, len(nums)-1, arr)
        # Return the list of all permutations
        return arr



# The time complexity of the provided code for generating all permutations of a list is O(n!). This is because there are 
# n! (n factorial) permutations of a list of n elements, and the algorithm generates each of these permutations once. The #
# factorial function grows very quickly, so the time complexity is exponential in the size of the input list 125.

# The space complexity of the algorithm is also O(n!). This is because the algorithm needs to store all n! permutations in memory.
# Each permutation is a list of n elements, and since there are n! permutations, the total space required to store all permutations
# is proportional to n!