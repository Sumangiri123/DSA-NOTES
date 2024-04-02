# Define a function named 'fact' that takes an integer 'n' as an argument
def fact(n):
    # Base case: if 'n' is 0, return 1 because the factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: return the product of 'n' and the factorial of 'n-1'
    # This is the essence of recursion, where the function calls itself with a smaller argument
    return n * fact(n-1)

# Assign the value 5 to the variable 'n'
n = 5
# Print the result of calling the 'fact' function with 'n' as the argument
print(fact(n))


# Recurrence Relation :

# Time Complexity :
# Space Complexity :