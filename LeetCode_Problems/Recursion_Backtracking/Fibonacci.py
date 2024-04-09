class Solution(object):
    def fib(self, n):
        # Base case: If n is 0 or 1, return n.
        # This is because the first two numbers in the Fibonacci sequence are 0 and 1.
        if n <= 1:
            return n
        
        # Recursive case: Return the sum of the (n-1)th and (n-2)th Fibonacci numbers.
        # This is the core of the Fibonacci sequence, where each number is the sum of the two preceding ones.
        return self.fib(n-1) + self.fib(n-2)



# Time Complexity

    # The time complexity of the recursive Fibonacci function is O(2^n). This is because each function call branches into two new
    # calls (for n-1 and n-2), leading to an exponential growth in the number of function calls. The base case of n <= 1 does not
    # significantly affect the overall complexity because it is reached after a significant number of recursive calls have been made.
    # The recurrence relation for the time complexity can be expressed as:
    # [T(n) = T\left(\frac{n}{2}\right) + O(1)]
    # This recurrence relation represents the binary search process, where at each step, the search space is halved, and a constant
    #  amount of work is done to compare the middle element and update the search pointers. Solving this recurrence relation gives us (O(\log n)) as the time complexity

# Space Complexity
    # The space complexity of the recursive Fibonacci function is O(n). This is because the maximum depth of the recursion tree is
    #  proportional to n. The recursion tree for calculating the Fibonacci sequence grows in a way that each level of the tree has
    #  twice as many nodes as the previous level, but the total number of nodes (which corresponds to the maximum depth of the 
    # recursion tree) is n. This is because each node in the tree represents a function call, and the tree's height (or depth) is 
    # the maximum number of nested calls before reaching the base case.

# The space complexity is determined by the maximum depth of the recursion tree, which is n. This is because each recursive call
# adds a new layer to the call stack, and the maximum depth of the call stack is directly proportional to the input size n.The 
# space required for each call is constant, but the total space is proportional to the depth of the recursion tree, which is n 12.

# In summary, the recursive Fibonacci function has a time complexity of O(2^n) and a space complexity of O(n).