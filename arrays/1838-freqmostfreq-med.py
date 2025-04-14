from typing import List
class Solution:
    def maxFrequency(nums: List[int], k: int) -> int:

        
        nums.sort()
        ans=1

        #bruteforce O(N^2) TLE for 52/73 test cases
        # for i in reversed(range(len(nums))):
        #     dummy=k
        #     inner_ans=1

        #     for j in reversed(range(0,i)):

        #         diff=nums[i]-nums[j]

                
        #         if diff<=dummy:
        #             dummy=dummy-diff
        #             inner_ans+=1
                
        #     if inner_ans>ans:
        #         ans=inner_ans
            
        # return ans
    
        # Sliding Window Final Approach
        #my initial approach of take the entire window and keep decreasing it failed unfortunately
        
        l=r=0
        current_window_sum=0
        ans=0
        while r<len(nums):
            current_window_sum+=nums[r] 
        
            while((r-l+1)*nums[r]-current_window_sum)>k:
                print("in")
                current_window_sum-=nums[l]
                l+=1

            ans=max(ans,r-l+1)
            r+=1

        return ans