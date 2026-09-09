# The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

# Take the first value from the unsorted part of the array.
# Move the value into the correct place in the sorted part of the array.
# Go through the unsorted part of the array again as many times as there are values.

arr=[523, 77, 23, 411, 1234, 99, 7]

# insertion sort 
for i in range(1,len(arr)):
    j=i
    val=arr[i]
    while(j>0 and arr[j-1]>val):
        arr[j]=arr[j-1]
        
    arr[j]=val

#recursive insertion sort
def insertion_sort(arr,n):
    
