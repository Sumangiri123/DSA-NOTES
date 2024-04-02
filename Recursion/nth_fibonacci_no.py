# Define a function named 'nth_fib' that takes an integer 'n' as an argument
def nth_fib(n):
    # Base case: if 'n' is less than or equal to 1, return 'n' directly
    # This is because the first two numbers in the Fibonacci sequence are 0 and 1
    if n <= 1:
        return n 
    # Recursive case: return the sum of the (n-1)th and (n-2)th Fibonacci numbers
    # This is the essence of recursion, where the function calls itself with smaller arguments
    return nth_fib(n-1) + nth_fib(n-2)

# Assign the value 5 to the variable 'n'
n = 5
# Print the result of calling the 'nth_fib' function with 'n' as the argument
print(nth_fib(n))



# Recurrence Relation :

# Time Complexity :
# Space Complexity :