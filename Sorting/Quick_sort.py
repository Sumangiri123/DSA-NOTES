def quick_sort(arr, low, high):
    # Base case: if the subarray has one or no elements, it's already sorted
    if low >= high:
        return
    
    # Partition the array around the pivot
    pi = partition(arr, low, high)

    # Recursively sort the elements before the pivot
    quick_sort(arr, low, pi - 1)

    # Recursively sort the elements after the pivot
    quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]
    i = low - 1
    
    # Partition the array around the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at the partition index
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the partition index
    return i + 1

arr = [5, 4, 0, -1, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


# Time Complexity :
# Space Complexity :