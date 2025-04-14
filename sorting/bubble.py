print("bubble")
#How it works:

# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last.
# Go through the array as many times as there are values in the array.

arr=(input("Input an array: "))
arr= list(map(int, arr.split()))
print("Array is:", arr)

for i in range(len(arr)):
    #for every i the last i numbers will be sorted
    for j in range(0,(len(arr)-1-i)):
        if arr[j]>arr[j+1]: # < condition will do descending order
            arr[j+1],arr[j]=arr[j],arr[j+1]
        
print(f"Sorted Array: {arr}")
