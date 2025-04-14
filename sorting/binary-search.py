from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while (l<=r):
            mid=(l+r)//2

            if target==nums[mid]:
                return mid

            else:
                if target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1

        return -1
    
arr=(input("Input an array: "))
arr= list(map(int, arr.split()))

target=(input("Input a target for the above array: "))

print("Target found at index:", Solution().search(arr,int(target)))