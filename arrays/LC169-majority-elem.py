class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # this is o(n) in space and time
        # print(nums)
        # ctr=Counter(nums)
        # for key,val in ctr.items():
        #     if val>len(nums)//2:
        #         return key
        # return -1
        #can also sort obviously

        #optimal will be o(1) space 
        #also called as boyer moore
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

        