class Solution:
    def containsDuplicate(self, nums) -> bool:

        return 1
        # if len(nums)==len(set(nums)):
        #     return False
        # else:
        #     return True
        
    #brute force is O(n^2)
    #can use sorting and then check adjacent elements complexity is O(nlogn)
    #optimal is O(n) by using set, but space is O(n)