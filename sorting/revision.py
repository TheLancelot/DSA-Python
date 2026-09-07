# The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

# Take the first value from the unsorted part of the array.
# Move the value into the correct place in the sorted part of the array.
# Go through the unsorted part of the array again as many times as there are values.

arr=[523, 77, 23, 411, 1234, 99, 7]

# merge sort

a1=[1,2,3,4,5]
a2=[6,7,8]

# for i in range(len(arr)):
#     #for every i the last i numbers will be sorted
#     for j in range(0,(len(arr)-1-i)):
#         if arr[j]>arr[j+1]: # < condition will do descending order
#             arr[j+1],arr[j]=arr[j],arr[j+1]

def bubble(arr,n):
    #for using recursion the idea will be to recall the function for a smaller set of arrays? like one length smaller, because after every turn the largest number will go till the end, so maybe at every recurse call we can put the largest number at the end 

    if n==1:
        return
    
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]

    # print(arr)

    return bubble(arr,n-1)

bubble(arr,len(arr))
print("Sorted Array", arr)
