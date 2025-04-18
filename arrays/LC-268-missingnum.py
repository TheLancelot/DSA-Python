class Solution:
    def missingNumber(self, nums: List[int]) -> int:
 
        return ((len(nums)*(len(nums)+1))//2)-sum(nums)

        #brute force is o(n^2)
        #another approach is first create hash and then check if the number is present or not complexity is o(2n)

        #optimal 1 is sum approach
        #optimal 2 is xor approach
        #in xor approach 