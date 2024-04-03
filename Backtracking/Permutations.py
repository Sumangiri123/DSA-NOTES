# Function to generate all permutations of a given string
def permute(chr_arr, left, right):
    # Base case: If left index is equal to right, we have a valid permutation
    if left == right:
        # Print the permutation
        print("".join(chr_arr))
        return
    else:
        # Iterate over each character in the substring from left to right
        for i in range(left, right+1):
            # Swap the character at the left index with the character at index i
            chr_arr[left], chr_arr[i] = chr_arr[i], chr_arr[left]
            # Recursively call permute for the remaining substring
            permute(chr_arr, left+1, right)
            # Swap the characters back to restore the original string
            chr_arr[left], chr_arr[i] = chr_arr[i], chr_arr[left]

# Example usage
s = "ABC"
# Convert the string to a list of characters
chr_arr = list(s)
# Call the permute function to generate all permutations
permute(chr_arr, 0, len(chr_arr)-1)


# Recurrence Relation :

# Time Complexity :
# Space Complexity :