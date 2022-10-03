#This method will only work with python
# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             return -1

#this is the classical way to do the problem
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

s1=Solution()
s1.search(nums = [-1,0,3,5,9,12], target = 9)
