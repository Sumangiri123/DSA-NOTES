# Python program to display the Fibonacci sequence

def recur_fibo(n):
    # Base case: if 'n' is less than or equal to 1, return 'n'
    # This is because the first two numbers in the Fibonacci sequence are 0 and 1
    if n <= 1:
        return n
    else:
        # Recursive case: return the sum of the (n-1)th and (n-2)th Fibonacci numbers
        # This is the essence of recursion, where the function calls itself with smaller arguments
        return(recur_fibo(n-1) + recur_fibo(n-2))

# Number of terms to display
nterms = 10

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    result = []
    # Use a loop to print the first 'n' Fibonacci numbers
    for i in range(nterms):
        result.append(recur_fibo(i))

# printing the required result   
print(result)

# Recurrence Relation :

# Time Complexity :
# Space Complexity :