# Function to perform counting sort on an array
def count_sort(arr):
    # Find the maximum element in the array to determine the size of the count array
    M = max(arr)
    # Initialize the count array with zeros, size is M+1 to account for zero-based indexing
    count_arr = [0]*(M+1)
    # Count the occurrence of each element in the array
    for num in arr:
        count_arr[num] += 1 
    # Modify the count array to store the cumulative count of elements
    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]
    # Initialize the output array with zeros, same size as the input array
    output_arr = [0]*len(arr)
    # Place each element in the output array based on its count
    for i in range(len(arr)-1,-1,-1):
        # Find the correct position in the output array for the current element
        output_arr[count_arr[arr[i]]-1] = arr[i]
    # Return the sorted array
    return output_arr

# Example usage
arr = [5,4,3,8,7]
print(count_sort(arr))

# Count sort is used to sort arrayof numbers
# Count sort can be used  to sort array conatining smaller elements


# Time Complexity :
# Space Complexity :

