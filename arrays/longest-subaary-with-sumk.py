# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k): 
        
        #pure brute force is O(n^3) (innermost is for calculating sum of subarray)
        #optimized brute force is O(n^2) (in the inner for while iterating through sub arrays just keep incrementing the sum)
        
        #better solutions
    
        #prefix sum
        # prefix=[0]*len(arr)
        # ans=0
        # sum=0
        # for idx,num in enumerate(arr):
        #     sum+=num
        #     prefix[idx]=sum
        # for idx,val in enumerate(reversed(prefix)):
        #     if((val-k) in prefix):
        #         ans= abs(len(arr)-1-(prefix.index(val-k))-idx)
            
        #     elif val==k:
        #         ans=len(arr)-idx
        #         break
                
        # return ans   
            
        prefix={}
        res=0
        sum=0
        for idx,num in enumerate(arr):
            sum+=num
            if not sum in prefix:
                prefix[sum]=idx
        
        prefSum=0       
        for i in range(len(arr)):
            prefSum += arr[i]
    
            # Check if the entire prefix sums to k

            if prefSum == k:
                res = i + 1
    
            # If prefixSum - k exists in the map then there exist such 
          	# subarray from (index of previous prefix + 1) to i.
            elif (prefSum - k) in prefix:
                res = max(res, i - prefix[prefSum - k])
                
        return res   


#for positive elements array
from typing import List

# def getLongestSubarray(a: [int], k: int) -> int:
#     n = len(a) # size of the array.

#     left, right = 0, 0 # 2 pointers
#     Sum = a[0]
#     maxLen = 0
#     while right < n:
#         # if sum > k, reduce the subarray from left
#         # until sum becomes less or equal to k:
#         while left <= right and Sum > k:
#             Sum -= a[left]
#             left += 1

#         # if sum = k, update the maxLen i.e. answer:
#         if Sum == k:
#             maxLen = max(maxLen, right - left + 1)

#         # Move forward the right pointer:
#         right += 1
#         if right < n: Sum += a[right]

#     return maxLen


# if __name__ == "__main__":
# 	a = [2, 3, 5, 1, 9]
# 	k = 10

# 	length = getLongestSubarray(a, k)
# 	print(f"The length of the longest subarray is: {length}")



