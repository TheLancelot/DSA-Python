# The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

# Take the first value from the unsorted part of the array.
# Move the value into the correct place in the sorted part of the array.
# Go through the unsorted part of the array again as many times as there are values.

arr=(input("Input an array: "))
arr= list(map(int, arr.split()))
print("Array is:", arr)

# for i in range(1,len(arr)):
#     for j in range(i,0,-1):
#         print(i,j)
#         if arr[j]<arr[j-1]:
#             arr[j],arr[j-1]=arr[j-1],arr[j]
#         else:
#             break
#         print(arr)

#easier interpretation with while loop
for i in range(1,len(arr)):
    val=arr[i]
    j=i
    while(j>0 and arr[j-1]>arr[j] ): #contiuously swap until ith element goes in corect slot, or you can find the index and then insert that there
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1


##using python fancy functions
# for i in range(1,len(arr)):
#     # val=arr.pop()
#     val=arr[i]
#     insert=i
#     for j in range(i-1,-1,-1):

#         if arr[j]>val:
#             arr[j+1]=arr[j]
#             insert=j

#         else:
#             break

#     arr[insert]=val
    # arr.insert(insert,val) #but this insert uses a lot of shifts because all elements will be shifted, what we can do while comparing the values it self if its greater we can update the value

print(f"Sorted Array: {arr}")