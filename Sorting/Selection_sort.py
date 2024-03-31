def Selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

    return arr

    
# Initialize an array with unsorted elements.
arr = [5,8,1,6,2,4,3]
# Print the sorted array by calling the 'Bubble_sort' function.
print(Selection_sort(arr))