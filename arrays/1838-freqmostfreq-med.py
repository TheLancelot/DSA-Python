from typing import List
class Solution:
    def maxFrequency(nums: List[int], k: int) -> int:

        
        nums.sort()
        ans=1

# x-y
# x-z

# y-z
        #bruteforce O(N^2) TLE for 52/73 test cases
        for i in reversed(range(len(nums))):
            dummy=k
            inner_ans=1

            for j in reversed(range(0,i)):

                diff=nums[i]-nums[j]

                
                if diff<=dummy:
                    dummy=dummy-diff
                    inner_ans+=1
                
            if inner_ans>ans:
                ans=inner_ans
            
        return ans
    
        # count=Counter(nums)
        # print(count)