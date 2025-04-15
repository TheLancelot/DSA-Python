arr=(input("Input an array: "))
arr= list(map(int, arr.split()))
print("Array is:", arr)

a1=[1,3,5,8]
a2=[2,4,6]
def merge(a1,a2):
    final=[]
    i,j=0,0
    while i<len(a1) and j<len(a2):

        if a1[i]<a2[j]:
            final.append(a1[i])
            i+=1
        else:
            final.append(a2[j])
            j+=1

    final.extend(a1[i:])
    final.extend(a2[j:]) 

    return final


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    
    return merge(sortedLeft, sortedRight)

print(f"Sorted Array: {mergeSort(arr)}")