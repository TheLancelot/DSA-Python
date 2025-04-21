from collections import Counter 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # c=Counter(nums)
        # for key,value in c.items():
        #     if value==1:
        #         return key
        #O(n)/O(n)

        xor=0
        for ele in nums:
            xor=xor^ele
        return xor

        