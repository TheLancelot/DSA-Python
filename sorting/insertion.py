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
# for i in range(1,len(arr)):
#     val=arr[i]
#     j=i
#     while(j>0 and arr[j-1]>arr[j] ): #contiuously swap until ith element goes in corect slot, or you can find the index and then insert that there
#         arr[j-1],arr[j]=arr[j],arr[j-1]
#         j-=1

#both the above implementations (2 fors, 1 for 1 while) are a bit expensive -- because we are swapping at every comparison - high memory overhead and redundant writes 

#the better way will be do the while loop till the condition doesnt satisfy and only then swap - but swap with watch, if we swap with the current index we lose out on the middle info as our goal is to insert the element in the correct spot (swap will not move the remaining elements (the one on the right of the correct spot) they will retain their spot we want to shift them by one) -- so the best optimal version is to save the current unsorted element and repeated to move the previous sorted list element by 1 until condition doesnt match and then place the currect unsorted element at that index (this will sort as we have moved the larger elements by one index to the right)

for i in range(1,len(arr)):
    j=i
    val=arr[i]
    while(j>0 and arr[j-1]>val):
        arr[j]=arr[j-1]
        j-=1
        
    arr[j]=val


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