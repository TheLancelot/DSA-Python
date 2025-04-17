class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nonzero = [0] * len(nums)
        # j=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nonzero[j]=nums[i]
        #         j+=1

        # for i in range(len(nums)):
        #     nums[i]=nonzero[i]

        #two pointers, swap non zero element with zero element, increment index of zero and non zero
        i=0
        j=0
        for right in range(len(nums)):
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i]!=0:
                i+=1
                j+=1
            else:
                j+=1

        # left=0
        # for right in range(len(nums)):
        #     if nums[right]!=0:
        #         nums[left],nums[right]=nums[right],nums[left]
        #         left+=1
            
            
                

        