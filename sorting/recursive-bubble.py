arr=[9,8,7,6,5,4,3,2,1]
    #for using recursion the idea will be to recall the function for a smaller set of arrays? like one length smaller, because after every turn the largest number will go till the end, so maybe at every recurse call we can put the largest number at the end 

#here initially i just took arr as input, in for loop was using len arr, and then i was recursing on a a subset of array, so it was not updating the main array just the parameter, thats why we need to pass len(arr) as well, and the arr as it self instead of arr[0:n-1], also in my first approach i kept swapping inside the for if loop (because we used to do that in bubble sort), but here to optimize we can just find the max and swap it with the last element, so that we can reduce the number of swaps

#the time complexity of this approach is O(n^2) and space complexity is O(n) because of recursion stack, but we can reduce the space complexity to O(1) by using iterative approach

def bubble(arr,idx):

    if idx==1:
        return
    
    max=0
    for i in range(idx):
        if arr[i]>arr[max]:
            max=i

    arr[max],arr[idx-1]=arr[idx-1],arr[max]
    print(arr)
    bubble(arr,idx-1)

bubble(arr,len(arr))
print(f"Sorted Array: {arr}")

#we can have a slightly modified approach where we use the old repeated swap logic, but incase no swap occur in one iteration means list is sorted, so we can break the loop and return, this will reduce the time complexity to O(n) in best case scenario, but still O(n^2) in worst case scenario when swaps keep happening etc

def bubble_sort(arr, n):
    # Base case: only one element left
    if n == 1:
        return

    did_swap = False  # Flag to detect swap

    # Single pass: move the largest to the end
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            did_swap = True

    # If no swaps occurred, list is already sorted
    if not did_swap:
        return

    # Recurse on the smaller array
    bubble_sort(arr, n - 1)
