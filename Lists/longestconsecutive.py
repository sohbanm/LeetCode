# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums)==0:
#             return 0
#         numSet = set(nums)
#         high = 1
#         i = 0
#         while i<len(nums):
#             if nums[i]-1 not in numSet:
#                 if nums[i]+1 in numSet:
#                     temp = 2
#                     for x in range(2,len(nums)):
#                         if nums[i]+x in numSet:
#                             temp+=1
#                         else:
#                             break
#                     high = max(high, temp)
#             i+=1
#         return high

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                temp = 0
                while (n + temp) in numSet:
                    temp+=1
                longest = max(temp, longest)

        return longest