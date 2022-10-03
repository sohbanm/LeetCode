class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k= k % len(nums)

        slice = len(nums) - k
        start = nums[:slice]
        del nums[:slice]
        nums.extend(start)
        print(nums)
    
s1= Solution()
s1.rotate(nums = [1,2,3,4,5,6,7], k = 3)

