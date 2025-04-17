'''Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.'''

from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:

        #brute force (for all rotations check if its sorted (n-1 total rotations) do it by building new array)
        rotated=[]
        
        for i in range(len(nums)):
            flag=True
            rotated=nums[i:]+nums[:i]
            print(i,rotated)
            for i in range(len(rotated)-1):
                if not rotated[i]<=rotated[i+1]:
                    flag=False
            if flag:
                return True
        return False

        #(this my approach doest work because multiple 6 10 6 keliye how to decide smallest so L)
        # smallest=0
        # for i in range(1,len(nums)):
        #     if(nums[i]<nums[smallest]):
        #         smallest=i

        # print(smallest)
        # l=nums[smallest:]
        # r=nums[:smallest]
        
        # l.extend(r)
        # print(l)

        # for i in range(len(l)-1):
        #     if not l[i]<=l[i+1]:
        #         return False
        # return True

        #at the most one inversion of irder 2,1,3 (because ascending order except one all elements should be increasing meaing a[i+1]>a[i])

        inversions=0

        for i in range(1,len(nums)):
            if(nums[i-1]>nums[i]):
                inversions+=1
        
        if(nums[len(nums)-1]>nums[0]):
            inversions+=1

        if inversions>1:
            return False

        else:
            return True