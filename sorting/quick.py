arr=(input("Input an array: "))
arr= list(map(int, arr.split()))
print("Array is:", arr)

def partition(arr,low,high): #this will take the array, swap elements such that the first elements are lesser than pivot and rest are higher than pivot, we consider last element as pivot
    pivot=arr[high]
    j=low-1

    for i in range(low,high):
        if arr[i]<pivot:
            j+=1
            arr[i],arr[j]=arr[j],arr[i] #group elements smaller than pivot to the left
            
    arr[high],arr[j+1]=arr[j+1],arr[high] #finally swap the pivot element into its position

    return j+1

def quick(arr,low=0,high=None):
    if high == None:
        high=len(arr)-1
    
    if low<high:
        pivot_idx=partition(arr,low,high)

        quick(arr,low,pivot_idx-1)
        quick(arr,pivot_idx+1,high)

quick(arr)
print(f"Sorted Array: {arr}")

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)