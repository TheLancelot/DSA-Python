class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        #brute force approach (O(n) space and time 2 passes)
        # pos=[]
        # neg=[]
        # for i in nums:
        #     pos.append(i) if i>0 else neg.append(i)

        # j=0
        # for i in range(0,len(nums)//2):
        #     nums[j]=pos[i]
        #     nums[j+1]=neg[i]
        #     j+=2

        # return nums

        #optimal (single pass)
        fin=[0]*len(nums)

        p=0
        n=1
        for i in range(len(nums)):
            if nums[i]>0:
                fin[p]=nums[i]
                p+=2
            
            else:
                fin[n]=nums[i]
                n+=2
                
        return fin




        