class Solution(object):
    def reverseString(self, s):
        # Define a nested function to perform the reversal recursively
        def reverse(start, end):
            # Base case: If the start index is greater than or equal to the end index,
            # it means we've reached the middle of the string or the end, so we return.
            if start >= end:
                return
            # Swap the characters at the start and end indices
            s[start], s[end] = s[end], s[start]
            # Recursively call the reverse function with the next start and previous end indices
            # to continue reversing the string
            reverse(start+1, end-1)
        # Call the reverse function with the initial start index as 0 and the end index as the last index of the string
        reverse(0, len(s)-1)


# This approach efficiently searches for the target in the matrix with a time complexity of O(log(m * n)), as it reduces the
# search space by half in each iteration of the binary search. The space complexity is O(1) since it only uses a constant amount
# of space for variables and does not require any additional data structures.