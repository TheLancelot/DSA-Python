
arr=(input("Input an array: "))
arr= list(map(int, arr.split()))
print("Array is:", arr)


def secondLargestandsmallest(arr):
    # nlogn
    # arr.sort()
    # return arr[-2],arr[1]

    #2n
    # max=arr[0]
    # min=arr[0]

    # for i in range(len(arr)):
    #     if arr[i]>max:
    #         max=arr[i]
    #     if arr[i]<min:
    #         min=arr[i]

    # small=float('inf')
    # large=float('-inf')

    # for i in range(len(arr)):
    #     if(arr[i]<small and arr[i]!=min):
    #         small=arr[i]
        
    #     if(arr[i]>large and arr[i]!=max):
    #         large=arr[i]
    
    # return small,large
    
    #in a single pass, no need to precompute
    smallest=arr[0]
    second=float('inf')
    for i in range(1,len(arr)):
        if(arr[i]<second and arr[i]>smallest):
            second=arr[i]
        elif(arr[i]<smallest):
            second=smallest
            smallest=arr[i]

    return second
    
print(secondLargestandsmallest(arr))



