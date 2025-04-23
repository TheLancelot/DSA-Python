class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute force is o(n2) //TLE
        # ans=nums[0]

        # for i in range(len(nums)):
        #     cur=0
        #     for j in range(i,len(nums)):
        #         cur+=nums[j]
        #         ans=max(ans,cur)
        
        # return ans


        #optimal is kadane's algorithm- o(n)
        #basically if current sum is less than zero then we dont need it in the subarry for next element as sum will just decrease as compared to taking that nth element on its own
        
        curr=0
        ans=nums[0]

        for i in nums:
            curr+=i
            ans=max(curr,ans)

            if curr<0:
                curr=0
    
        return ans
