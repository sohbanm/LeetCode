class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
        print(nums)

s1=Solution()
s1.moveZeroes(nums = [0])