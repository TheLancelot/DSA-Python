#How it works:

# Go through the array to find the lowest value.
# Move the lowest value to the front of the unsorted part of the array.
# Go through the array again as many times as there are values in the array

arr=(input("Input an array: "))
arr= list(map(int, arr.split()))
print("Array is:", arr)

for i in range(len(arr)-1):

    smallest=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[smallest]: #finds the index of the lowest element
            smallest=j
        
        arr[i],arr[smallest]=arr[smallest],arr[i] #brings lowest element to the front

print(f"Sorted Array: {arr}")

