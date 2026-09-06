arr=(input("Input an array: "))
arr= list(map(int, arr.split()))
print("Array is:", arr)

a1=[1,3,5,8]
a2=[2,4,6]
def merge(a1,a2): #takes 2 sorted arrays and merges them
    final=[]
    n1=len(a1)
    n2=len(a2)

    i,j=0,0
    # for _ in range(n1+n2): 
    #theres one issue here for loop runs exactly n1 + n2 times. However, your comparison logic is nested inside if (i < n1 and j < n2). As soon as one array runs out of elements, that condition becomes False. The loop keeps spinning for the remaining iterations, but it does absolutely nothing. in worst case it will go to n1+n2 but in all other cases the loop spins for no reason
    # we can change the for loop to a while loop to avoid this problem
    while i<n1 and j<n2:
        # if(i<n1 and j<n2):
            if a1[i]<a2[j]:
                final.append(a1[i])
                i+=1

            else:
                final.append(a2[j])
                j+=1

    #need to append the remaining parts if any (one of the two will be empty)
    final.extend(a1[i:])
    final.extend(a2[j:])

    return final

def mergeSort(arr):
    #important to visualise here which part to use the recursion aspect and where to use the merge function
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    
    return merge(sortedLeft, sortedRight)


print(f"Sorted Array: {mergeSort(arr)}")