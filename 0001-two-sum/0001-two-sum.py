class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #brute force is O(n^2)
        # for idx,val in enumerate(nums):
        #     for j in range(idx+1,len(nums)):
        #         if val+nums[j]==target:
        #             return [idx,j]

        #optimal way is to have a map with element and index, then iterate thorugh the array, and if target-element is in map, return the indices

        map={}
        for i in range(len(nums)):
            if(nums[i] not in map):
                map[nums[i]]=i
            
            if target-nums[i] in map and i!=map[target-nums[i]]:
                print("in")
                return [i,map[target-nums[i]]]
