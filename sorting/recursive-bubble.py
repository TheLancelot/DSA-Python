arr=[9,8,7,6,5,4,3,2,1]

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