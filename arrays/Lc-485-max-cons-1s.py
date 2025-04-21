class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final=0
        window=0
        for i in range(len(nums)):
            if nums[i]==1:
                window+=1
            
                if window>final:
                    final=window
            
            else:
                window=0
        
        return final
            