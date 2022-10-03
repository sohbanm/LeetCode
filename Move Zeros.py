class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=[]
        count=0
        while count<len(nums):
            if nums[count] == 0:
                nums.pop(count)
                zeros.append(0)
            else:
                count+=1
            

        nums.extend(zeros)
        