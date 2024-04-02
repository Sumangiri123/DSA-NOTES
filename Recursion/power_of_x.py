# Define a function named 'power' that takes two arguments: 'x' as the base and 'n' as the exponent
def power(x, n):
    # Base case: if 'n' is 0, return 1
    # This is because any number raised to the power of 0 is 1
    if n == 0:
        return 1
    else:
        # Calculate the midpoint of 'n' by performing integer division by 2
        mid = n // 2
        # Recursive case: calculate the power of 'x' raised to the 'mid' power
        # This is done by calling the 'power' function recursively
        result = power(x, mid)
        # Calculate the final result by squaring the result of the recursive call
        final_result = result * result

        # Check if 'n' is even
        if n % 2 == 0:
            # If 'n' is even, return the squared result
            return final_result
        else:
            # If 'n' is odd, return the product of 'x' and the squared result
            # This accounts for the case where the exponent is odd
            return x * final_result


# Assign the value 2 to the variable 'x'
x = 2
# Assign the value 3 to the variable 'n'
n = 3
# Print the result of calling the 'power' function with 'x' and 'n' as the arguments
print(power(x, n))



# Recurrence Relation :

# Time Complexity :
# Space Complexity :