class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #brute force o(n) time and space
        # c=Counter(nums)
        # for i in range(len(nums)):
        #     if i<c[0]:
        #         nums[i]=0
        #     elif i<(c[0]+c[1]):
        #         nums[i]=1
        #     else:
        #         nums[i]=2

        #two pass constant space
        # z=0
        # o=0
        # for i in nums:
        #     if i==0:
        #         z+=1
        #     elif i==1:
        #         o+=1
        # for i in range(len(nums)):
        #     if i<z:
        #         nums[i]=0
        #     elif i<(o+z):
        #         nums[i]=1
        #     else:
        #         nums[i]=2
        
        #single pass constant space
        i=0
        j=0
        k=len(nums)-1
        while j<=k:
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[j]==2:
                nums[k],nums[j]=nums[j],nums[k]
                k-=1
            else:
                j+=1

