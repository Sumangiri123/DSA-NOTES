class Solution(object):
    def isPalindrome(self, x):
        # Check if x is negative. Negative numbers cannot be palindromes.
        if x < 0:
            return False
        
        # Define a nested function to reverse the digits of x
        def reverse(x):
            # Base case: if x is a single digit, return its string representation
            if x < 10:
                return str(x)
            # Recursive case: append the last digit of x to the reversed string of the rest of x
            return str(x % 10) + reverse(x // 10)

        # Compare the original number with its reversed string representation
        # If they are equal, x is a palindrome
        if x == int(reverse(x)):
            return True
        else:
            return False



# Time Complexity

    # The time complexity of the code is O(N), where N is the number of digits in the integer x. This is 
    # because the recursive function reverse is called for each digit in x, and each call processes one 
    # digit. Since the number of digits in x is directly proportional to the size of x, the time 
    # complexity is linear.

# Space Complexity

    # The space complexity of the code is O(1). This is because the recursive function reverse does not 
    # use any additional space that scales with the input size. The space used by the function call stack
    #  is constant and does not depend on the size of x. Therefore, the space complexity is constant.

# In summary, the provided code has a linear time complexity due to the recursive nature of the reverse 
# function, which processes each digit of x once. The space complexity is constant because the function 
# call stack does not grow with the size of x