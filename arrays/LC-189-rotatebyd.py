class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #10^5 meaning need to do in O(n)
        # rotated = [0] * len(nums)
        # for i in range(len(nums)):

        #         idx=(i+k)%len(nums)
        #         rotated[idx]=nums[i]
        # for i in range(len(nums)):
        #     nums[i] = rotated[i]

        # nums[k:],nums[:k]=nums[:-k],nums[-k:]

        k=k%len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        