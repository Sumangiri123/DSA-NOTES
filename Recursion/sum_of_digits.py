# Define a function named 'sum_of_digits' that takes an integer 'n' as an argument
def sum_of_digits(n):
    # Base case: if 'n' is less than 10, return 'n' directly
    # This is because for single-digit numbers, their sum is the number itself
    if n < 10:
        return n 
    # Recursive case: return the sum of the last digit of 'n' and the sum of the digits of 'n' excluding the last digit
    # This is achieved by using the modulo operator (%) to get the last digit and integer division (//) to remove the last digit
    # The function calls itself recursively with the remaining digits of 'n'
    return (n % 10) + sum_of_digits(n // 10)

# Assign the value 123 to the variable 'n'
n = 123
# Print the result of calling the 'sum_of_digits' function with 'n' as the argument
print(sum_of_digits(n))

# Recurrence Relation :

# Time Complexity :
# Space Complexity :