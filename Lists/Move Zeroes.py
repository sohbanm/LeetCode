class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Two Pointers Method
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1

        ##Remove and Add
        # zeros=[]
        # count=0
        # while count<len(nums):
        #     if nums[count] == 0:
        #         nums.pop(count)
        #         zeros.append(0)
        #     else:
        #         count+=1
        # nums.extend(zeros)

s1=Solution()
s1.moveZeroes(nums = [0])