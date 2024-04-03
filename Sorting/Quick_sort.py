def quick_sort(arr):
    if 





def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high+1):
        if arr[j] <= pivot :
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]


arr = [5,4,0,-1,1]
partition(arr,0,len(arr)-1)
print(arr)